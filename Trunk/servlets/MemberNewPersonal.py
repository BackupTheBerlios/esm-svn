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
from Middle.AccountsTR import AccountsTR
from WebUtils.Funcs import urlEncode
from MySQLdb import OperationalError,Warning
import string

true = 1 == 1
false = 1 != 1

personalType = 0
personalRequired = 1
personalFields = {
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
  'Lizenz1':['string',0],
  'LizenzNr1':['string',0],
  'LizenzBis1':['date',0],
  'LizenzZuschuss1':['float',0],
  'Lizenz2':['string',0],
  'LizenzNr2':['string',0],
  'LizenzBis2':['date',0],
  'LizenzZuschuss2':['float',0],
  'Lizenz3':['string',0],
  'LizenzNr3':['string',0],
  'LizenzBis3':['date',0],
  'LizenzZuschuss3':['float',0],
  'Lizenz4':['string',0],
  'LizenzNr4':['string',0],
  'LizenzBis4':['date',0],
  'LizenzZuschuss4':['float',0],
  'Lizenz5':['string',0],
  'LizenzNr5':['date',0],
  'LizenzBis5':['date',0],
  'LizenzZuschuss5':['float',0],
  'Lizenz6':['string',0],
  'LizenzNr6':['date',0],
  'LizenzBis6':['date',0],
  'LizenzZuschuss6':['float',0],
  'Fortbildungen':['string',0],
  'Honorar1':['string',0],
  'HonorarBetrag1':['float',0],
  'Honorar2':['string',0],
  'HonorarBetrag2':['float',0],
  'Honorar3':['string',0],
  'HonorarBetrag3':['float',0],
  'Honorar4':['string',0],
  'HonorarBetrag4':['float',0],
  'Honorar5':['string',0],
  'HonorarBetrag5':['float',0],
  'Honorar6':['string',0],
  'HonorarBetrag6':['float',0],
  'Training1':['string',0],
  'TrainingOrt1':['string',0],
  'TrainingTermin1':['string',0],
  'Training2':['string',0],
  'TrainingOrt2':['string',0],
  'TrainingTermin2':['string',0],
  'Training3':['string',0],
  'TrainingOrt3':['string',0],
  'TrainingTermin3':['string',0],
  'Training4':['string',0],
  'TrainingOrt4':['string',0],
  'TrainingTermin4':['string',0],
  'Training5':['string',0],
  'TrainingOrt5':['string',0],
  'TrainingTermin5':['string',0],
  'Training6':['string',0],
  'TrainingOrt6':['string',0],
  'TrainingTermin6':['string',0],
  'Training7':['string',0],
  'TrainingOrt7':['string',0],
  'TrainingTermin7':['string',0],
  'Training8':['string',0],
  'TrainingOrt8':['string',0],
  'TrainingTermin8':['string',0],
  'Training9':['string',0],
  'TrainingOrt9':['string',0],
  'TrainingTermin9':['string',0],
  'Training10':['string',0],
  'TrainingOrt10':['string',0],
  'TrainingTermin10':['string',0],
  'Kommentare':['string',1],
  'Seit':['date',1],
  'Bis':['date',0]
  }

personalAttrs = personalFields.keys()
standardAttrs = ['ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class MemberNewPersonal(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsTR'

  def writeContent(self, trans=None):
    #
    # this servlet creates Member data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # create personal object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    personal = AccountsTR()
    #
    # change personal object
    #
    for attr in personalAttrs:
      if attr not in standardAttrs:
        if personalFields[attr][personalType] == 'string':
          print self.transaction.request().field(attr,'')
          personal.setValueForKey(attr, self.transaction.request().field(attr,''))
        elif personalFields[attr][personalType] == 'float':
          if string.strip(self.transaction.request().field(attr,'')):
            personal.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,'0,00'),',','.')))
          else:
            personal.setValueForKey(attr, None)
        elif (personalFields[attr][personalType] == 'datetime') and self.request.field(attr,''):
          personal.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
        elif (personalFields[attr][personalType] == 'date') and self.transaction.request().field(attr,''):
          personal.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
    #
    # set standard attributes
    #
    personal.setErsteingabeAm(DateTime.now())
    personal.setChangedBy(self.transaction.session().value('authenticated_user',''))
    personal.setChangedAt(DateTime.now())
    personal.setChangedOn(self.getSite())
    #
    # store personal in database
    #
    store.addObject(personal)
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
    # back to personal page
    #
    self.transaction.response().sendRedirect('MemberView?index=' + account[2:])
