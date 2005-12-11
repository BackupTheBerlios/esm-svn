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
from Middle.AccountsBK import AccountsBK
from WebUtils.Funcs import urlEncode
from GlobalState import ID
from MySQLdb import OperationalError
import string

true = 1 == 1
false = 1 != 1

BankType = 0
BankRequired = 1
BankFields = {
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

BankAttrs = BankFields.keys()
standardAttrs = ['ID','ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class BankCreate(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsBK'

  def writeContent(self, trans=None):
    #
    # this servlet creates Bank data
    #

    page = self.transaction.request().field('page','Main')
    #
    # create Bank object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    BankNr=self.transaction.request().field('BankNr','')
    Bank = AccountsBK()
    #
    # change Bank object
    #
    for attr in BankAttrs:
      if attr not in standardAttrs:
        if BankFields[attr][BankType] == 'string':
          print self.transaction.request().field(attr,'')
          Bank.setValueForKey(attr, self.transaction.request().field(attr,''))
        elif BankFields[attr][BankType] == 'float':
          Bank.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,'0,0'),',','.')))
        elif (BankFields[attr][BankType] == 'datetime') and self.request.field(attr,''):
          Bank.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
        elif (BankFields[attr][BankType] == 'date') and self.transaction.request().field(attr,''):
          Bank.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
    #
    # set standard attributes
    #
    Bank.setID('BK'+BankNr)
    Bank.setErsteingabeAm(DateTime.now())
    Bank.setChangedBy(self.transaction.session().value('authenticated_user',''))
    Bank.setChangedAt(DateTime.now())
    Bank.setChangedOn(self.getSite())
    #
    # store Bank in database
    #
    store.addObject(Bank)
    try:
      store.saveChanges()
      #
      # back to Bank page
      #
      self.transaction.response().sendRedirect('BankView?index=' + BankNr)
    except OperationalError,x:
      store.discardEverything()
      errorCode,errorText = x
      #
      # back to error page
      #
      self.transaction.response().sendRedirect('Error?problem=Daten+konnten+nicht+gespeichert+werden!&reason=' + urlEncode(str(errorText)))
