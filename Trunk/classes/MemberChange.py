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

from SiteTemplate import SiteTemplate
from mx import DateTime
from MySQLdb import OperationalError,Warning
from Middle.Transfers import Transfers
from GlobalState import ID
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
  'Zahlungsart':['string',1],
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

class MemberChange(SiteTemplate):

  def __init__(self, *args, **KWs):
    SiteTemplate.__init__(self, *args, **KWs)
    self.storeName = 'AccountsMI'
    self.indexField = 'ID'

  def writeContent(self, trans=None):
    #
    # this servlet changes Member data
    #

    #
    # retrieving the parameters
    #
    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    beitragsart = string.strip(self.transaction.request().field('Beitragsart',''))
    beitragsartAb = string.strip(self.transaction.request().field('BeitragsartAb',''))
    beitragsartFreiAb = string.strip(self.transaction.request().field('BeitragsartFreiAb',''))
    austrittsdatum = string.strip(self.transaction.request().field('Austrittsdatum',''))
    
    #
    # calculating and setting the dates for "BeitragsartFreiAb"
    #
    #
    # if beitragsartFreiAb or beitragsartAb are not set, they are equal
    #
    if (beitragsartFreiAb == '') and (beitragsartAb != ''):
        beitragsFreiAb = beitragsartAb
    if (beitragsartFreiAb != '') and (beitragsartAb == ''):
        beitragsartAb = beitragsartFreiAb
    if (austrittsdatum != '') and (beitragsartFreiAb == ''):
        y =  DateTime.DateTimeFrom(austrittsdatum)+DateTime.DateTimeDelta(1)
        beitragsartFreiAb = y.date
        
    #
    # retrieve member object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE %s LIKE "%s_"' % (self.indexField,account[:-1]))
    print storeObjects
    for member in storeObjects:
        print "Change %s" % member.ID()
        print member
        if austrittsdatum and not member.Austrittsdatum():
            member.setAustrittsdatum(DateTime.DateTimeFrom(austrittsdatum))
            member.setAustrittsgrund(string.strip(self.transaction.request().field('Austrittsgrund','')))
        if member.valueForKey(self.indexField) == account:
          print "do it %s" % member.ID()
          #
          # change member object
          #
          for attr in memberAttrs:
            if (attr not in standardAttrs) and self.transaction.request().field(attr,None) != None:
              if memberFields[attr][memberType] == 'string':
                member.setValueForKey(attr, self.transaction.request().field(attr,''))
              elif memberFields[attr][memberType] == 'float':
                member.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,''),',','.')))
              elif memberFields[attr][memberType] == 'datetime':
                if self.transaction.request().field(attr,''):
                  member.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
                else:
                  member.setValueForKey(attr, None)
              elif memberFields[attr][memberType] == 'date':
                if self.transaction.request().field(attr,''):
                  member.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
                else:
                  member.setValueForKey(attr, None)
        if account[-1:] == "0":
            beitragsartNb = 0
            if beitragsartFreiAb != '':
                for x in range(1,Anzahl_Beitragsarten+1):
                  if (member.valueForKey('Beitragsart'+str(x)) != '') and (member.valueForKey('BeitragsartFreiAb'+str(x)) == None):
                    member.setValueForKey('BeitragsartFreiAb'+str(x), DateTime.DateTimeFrom(beitragsartFreiAb))
                    #
                    # fees with equal beitragsartAb and beitragsartFreiAb could be overwritten
                    #
                    if member.valueForKey('BeitragsartAb'+str(x)) == DateTime.DateTimeFrom(beitragsartFreiAb):
                      beitragsartNb = x - 1
                    else:
                      beitragsartNb = x
            elif beitragsartAb != '':
                for x in range(1,Anzahl_Beitragsarten+1):
                  if (member.valueForKey('Beitragsart'+str(x)) == '') and (beitragsartNb == 0):
                    beitragsartNb = x - 1
            #
            # set new fee in the next slot (2-5 and 1) respective slot 1, if no fee already exists
            #
            if beitragsart != '':
                member.setValueForKey('Beitragsart'+str(beitragsartNb % 5 + 1), beitragsart)
                member.setValueForKey('BeitragsartAb'+str(beitragsartNb % 5 + 1), DateTime.DateTimeFrom(beitragsartAb))
                member.setValueForKey('BeitragsartFreiAb'+str(beitragsartNb % 5 + 1), None)
                member.setValueForKey('BeitragsartErhebungAb'+str(beitragsartNb % 5 + 1), DateTime.DateTimeFrom(beitragsartAb))
                member.setValueForKey('Beitragsart'+str((beitragsartNb + 1) % 5 + 1), "")
                member.setValueForKey('BeitragsartAb'+str((beitragsartNb + 1) % 5 + 1), None)
                member.setValueForKey('BeitragsartFreiAb'+str((beitragsartNb + 1) % 5 + 1), None)
                member.setValueForKey('BeitragsartErhebungAb'+str((beitragsartNb + 1) % 5 + 1), None)
        #
        # set standard attributes
        #
        member.setChangedBy(self.transaction.session().value('authenticated_user',''))
        member.setChangedAt(DateTime.now())
        member.setChangedOn(self.getSite())
        #
        # store member in database
        #
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
