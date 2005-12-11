#
# File:      $URL$
# Version:   $Rev$
# Changed:   $Date$
#
# Homepage:  http://esm.berlios.de
# Copyright: GNU Public License Version 2 (see license.txt)
#
# E-Sportmanager (esm)
#
# Copyright (C) 2005 Jan Gottschick
#
#   This program is free software; you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#   or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#   for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the
#
#   Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
__author__ = "Jan Gottschick"
__revision__ = "$Rev$"[6:-2]

from SiteContent import SiteContent
from mx import DateTime
from MySQLdb import OperationalError,Warning
from Middle.AccountsMI import AccountsMI
from WebUtils.Funcs import urlEncode
from GlobalState import ID
from MySQLdb import OperationalError,Warning
import string

true = 1 == 1
false = 1 != 1

memberType = 0
MemberRequired = 1
memberFields = {
  'ID':['string',1],
  'MitgliedsNr':['string',1],
  'NeueMitgliedsNr':['string',0],
  'Vorname':['string',1],
  'Nachname':['string',1],
  'Titel':['string',0],
  'Adresszusatz':['string',0],
  'Strasse':['string',1],
  'Ort':['string',1],
  'Countrycode':['string',1],
  'PLZ':['string',1],
  'TelefonPrivat':['string',0],
  'TelefonDienst':['string',0],
  'Mobiltelefon':['string',0],
  'FAX':['string',0],
  'EMail':['string',0],
  'Geburtsdatum':['date',1],
  'Geschlecht':['string',1],
  'KontoNr1':['string',0],
  'BLZ1':['string',0],
  'Bank1':['string',0],
  'Kontoinhaber1':['string',0],
  'KontoNr2':['string',0],
  'BLZ2':['string',0],
  'Bank2':['string',0],
  'Kontoinhaber2':['string',0],
  'Beitragsart1':['string',0],
  'BeitragsartAb1':['date',0],
  'BeitragsartFreiAb1':['date',0],
  'BeitragsartErhebungAb1':['date',0],
  'Beitragsart2':['string',0],
  'BeitragsartAb2':['date',0],
  'BeitragsartFreiAb2':['date',0],
  'BeitragsartErhebungAb2':['date',0],
  'Beitragsart3':['string',0],
  'BeitragsartAb3':['date',0],
  'BeitragsartFreiAb3':['date',0],
  'BeitragsartErhebungAb3':['date',0],
  'Beitragsart4':['string',0],
  'BeitragsartAb4':['date',0],
  'BeitragsartFreiAb4':['date',0],
  'BeitragsartErhebungAb4':['date',0],
  'Beitragsart5':['string',0],
  'BeitragsartAb5':['date',0],
  'BeitragsartFreiAb5':['date',0],
  'BeitragsartErhebungAb5':['date',0],
  'Zahlungsart':['string',0],
  'LastschriftAb':['date',0],
  'RechnungAb':['date',0],
  'Eintrittsdatum':['date',1],
  'Kommentare':['string',1],
  'Austrittsdatum':['date',0],
  'Austrittsgrund':['string',0]
  }

memberAttrs = memberFields.keys()
standardAttrs = ['ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

Anzahl_Beitragsarten = 5

class MemberMove(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsMI'

  def writeContent(self, trans=None):
    #
    # this servlet creates Member data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # create member object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    if self.transaction.request().field('MitgliedsNr',None)[-1:] == "0":
      storeObjects = store.fetchObjectsOfClass('IDs','WHERE %s = "%s"' % ('Tablename',self.storeName))
      if (len(storeObjects) == 1) and self.transaction.request().field('ID',None):
        id = storeObjects[0]
        id.setLastID(int(self.transaction.request().field('MitgliedsNr',None)))
    member = AccountsMI()
    #
    # change member object
    #
    for attr in memberAttrs:
      if attr not in standardAttrs:
        if memberFields[attr][memberType] == 'string':
          print self.transaction.request().field(attr,'')
          member.setValueForKey(attr, self.transaction.request().field(attr,''))
        elif memberFields[attr][memberType] == 'float':
          member.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,'0,0'),',','.')))
        elif (memberFields[attr][memberType] == 'datetime') and self.request.field(attr,''):
          member.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
        elif (memberFields[attr][memberType] == 'date') and self.transaction.request().field(attr,''):
          member.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
    #
    # set fee dates
    #
    member.setValueForKey('BeitragsartFreiAb1', None)
    member.setValueForKey('BeitragsartErhebungAb1', DateTime.DateTimeFrom(self.transaction.request().field('BeitragsartAb1','')))
    #
    # set standard attributes
    #
    member.setErsteingabeAm(DateTime.now())
    member.setChangedBy(self.transaction.session().value('authenticated_user',''))
    member.setChangedAt(DateTime.now())
    member.setChangedOn(self.getSite())
    #
    # store member in database
    #
    store.addObject(member)
    #
    # set new MitgliedsNr in old member record
    #
    storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE %s = "%s"' % ('MitgliedsNr',self.transaction.request().field('oldMitgliedsNr',None)))
    oldMember = storeObjects[0]
    oldMember.setNeueMitgliedsNr(self.transaction.request().field('MitgliedsNr',None))
    oldMember.setAustrittsdatum(DateTime.DateTimeFrom(self.transaction.request().field('BeitragsartAb1',None)))
    oldMember.setAustrittsgrund(self.transaction.request().field('Austrittsgrund',None))
    try:
      store.saveChanges()
    except OperationalError,x:
      store.discardEverything()
      errorCode,errorText = x
      #
      # back to error page
      #
      self.transaction.response().sendRedirect('Error?problem=Daten+konnten+nicht+gespeichert+werden!&reason=' + urlEncode(str(errorText)))
    except Warning,x:
      pass
    #
    # back to member page
    #
    self.transaction.response().sendRedirect('MemberView?index=' + account[2:])
