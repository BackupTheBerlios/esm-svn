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
from Middle.Transfers import Transfers
from GlobalState import ID
import string

true = 1 == 1
false = 1 != 1

bankType = 0
BankRequired = 1
bankFields = {
  'ID':['string',1],
  'BankNr':['string',1],
  'Bank':['string',1],
  'KontoNr':['string',1],
  'BLZ':['string',1],
  'Adresszusatz':['string',0],
  'Strasse':['string',1],
  'Ort':['string',1],
  'Countrycode':['string',1],
  'PLZ':['string',1],
  'TelefonService':['string',0],
  'Ansprechpartner':['string',0],
  'TelefonAnsprechpartner':['string',0],
  'FAXAnsprechpartner':['string',0],
  'EMailAnsprechpartner':['string',0],
  'PINInternet':['string',0],
  'PINTelefon':['string',0],
  'Berechtigte':['string',0],
  'Kommentare':['string',0],
  }

bankAttrs = bankFields.keys()
standardAttrs = ['ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class BankChange(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsBK'
    self.indexField = 'ID'

  def writeContent(self, trans=None):
    #
    # this servlet changes Bank data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # retrieve bank object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE %s = "%s"' % (self.indexField,account))
    if len(storeObjects) == 1:
      bank = storeObjects[0]
      #
      # change bank object
      #
      for attr in bankAttrs:
        if (attr not in standardAttrs) and self.transaction.request().field(attr,None) != None:
          if bankFields[attr][bankType] == 'string':
            bank.setValueForKey(attr, self.transaction.request().field(attr,''))
          elif bankFields[attr][bankType] == 'float':
            bank.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,''),',','.')))
          elif bankFields[attr][bankType] == 'datetime':
            if self.transaction.request().field(attr,''):
              bank.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              bank.setValueForKey(attr, None)
          elif bankFields[attr][bankType] == 'date':
            if self.transaction.request().field(attr,''):
              bank.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              bank.setValueForKey(attr, None)
      #
      # set standard attributes
      #
      bank.setChangedBy(self.transaction.session().value('authenticated_user',''))
      bank.setChangedAt(DateTime.now())
      bank.setChangedOn(self.getSite())
      #
      # store bank in database
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
    # back to bank page
    #
    self.transaction.response().sendRedirect('BankView?index=' + account[2:])
