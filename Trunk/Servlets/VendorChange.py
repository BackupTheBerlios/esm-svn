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
from MySQLdb import OperationalError,Warning
from Middle.Transfers import Transfers
import string

true = 1 == 1
false = 1 != 1

vendorType = 0
VendorRequired = 1
vendorFields = {
  'ID':['string',1],
  'VendorNr':['string',1],
  'Firma':['string',0],
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

class VendorChange(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsVE'
    self.indexField = 'ID'

  def writeContent(self, trans=None):
    #
    # this servlet changes Vendor data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # retrieve vendor object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE %s = "%s"' % (self.indexField,account))
    if len(storeObjects) == 1:
      vendor = storeObjects[0]
      #
      # change vendor object
      #
      for attr in vendorAttrs:
        if (attr not in standardAttrs) and self.transaction.request().field(attr,None) != None:
          if vendorFields[attr][vendorType] == 'string':
            vendor.setValueForKey(attr, self.transaction.request().field(attr,''))
          elif vendorFields[attr][vendorType] == 'float':
            vendor.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,''),',','.')))
          elif vendorFields[attr][vendorType] == 'datetime':
            if self.transaction.request().field(attr,''):
              vendor.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              vendor.setValueForKey(attr, None)
          elif vendorFields[attr][vendorType] == 'date':
            if self.transaction.request().field(attr,''):
              vendor.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              vendor.setValueForKey(attr, None)
      #
      # set standard attributes
      #
      vendor.setChangedBy(self.transaction.session().value('authenticated_user',''))
      vendor.setChangedAt(DateTime.now())
      vendor.setChangedOn(self.getSite())
      #
      # store vendor in database
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
    # back to vendor page
    #
    self.transaction.response().sendRedirect('VendorView?index=' + account[2:])
