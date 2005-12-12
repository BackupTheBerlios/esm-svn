#
# File:      $URL$
# Version:   $rev$
# Changed:   $date$
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
__revision__ = "$Rev$"[4,-2]

from SiteContent import SiteContent
from mx import DateTime
from Middle.AccountsVE import AccountsVE
from WebUtils.Funcs import urlEncode
from MySQLdb import OperationalError
import string

true = 1 == 1
false = 1 != 1

vendorType = 0
VendorRequired = 1
vendorFields = {
  'ID':['string',1],
  'VendorNr':['string',1],
  'Firma':['string',1],
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
  'KontoNr1':['string',0],
  'BLZ1':['string',0],
  'Bank1':['string',0],
  'Kontoinhaber1':['string',0],
  'KontoNr2':['string',0],
  'BLZ2':['string',0],
  'Bank2':['string',0],
  'Kontoinhaber2':['string',0],
  'Kommentare':['string',1],
  }

vendorAttrs = vendorFields.keys()
standardAttrs = ['ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class VendorCreate(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsVE'

  def writeContent(self, trans=None):
    #
    # this servlet creates Vendor data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # create vendor object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    if self.transaction.request().field('VendorNr',None)[-1:] == "0":
      storeObjects = store.fetchObjectsOfClass('IDs','WHERE %s = "%s"' % ('Tablename',self.storeName))
      if (len(storeObjects) == 1) and self.transaction.request().field('ID',None):
        id = storeObjects[0]
        id.setLastID(int(self.transaction.request().field('VendorNr',None)))
    vendor = AccountsVE()
    #
    # change vendor object
    #
    for attr in vendorAttrs:
      if attr not in standardAttrs:
        if vendorFields[attr][vendorType] == 'string':
          vendor.setValueForKey(attr, string.strip(self.transaction.request().field(attr,'')))
        elif vendorFields[attr][vendorType] == 'float':
          vendor.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,'0,0'),',','.')))
        elif (vendorFields[attr][vendorType] == 'datetime') and self.request.field(attr,''):
          vendor.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
        elif (vendorFields[attr][vendorType] == 'date') and self.transaction.request().field(attr,''):
          vendor.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
    #
    # set standard attributes
    #
    vendor.setErsteingabeAm(DateTime.now())
    vendor.setChangedBy(self.transaction.session().value('authenticated_user',''))
    vendor.setChangedAt(DateTime.now())
    vendor.setChangedOn(self.getSite())
    #
    # store vendor in database
    #
    store.addObject(vendor)
    try:
      store.saveChanges()
      #
      # back to vendor page
      #
      self.transaction.response().sendRedirect('VendorView?index=' + account[2:])
    except OperationalError,x:
      store.discardEverything()
      errorCode,errorText = x
      #
      # back to error page
      #
      self.transaction.response().sendRedirect('Error?problem=Daten+konnten+nicht+gespeichert+werden!&reason=' + urlEncode(str(errorText)))
