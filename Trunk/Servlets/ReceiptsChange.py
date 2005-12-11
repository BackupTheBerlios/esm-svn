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

ReceiptsType = 0
ReceiptsRequired = 1
ReceiptsFields = {
  'ID':['string',1],
  'Nr':['string',1],
  'Name':['string',1],
  'Kommentare':['string',0],
  }

ReceiptsAttrs = ReceiptsFields.keys()
standardAttrs = ['ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class ReceiptsChange(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsEK'
    self.indexField = 'ID'

  def writeContent(self, trans=None):
    #
    # this servlet changes Receipts data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # retrieve Receipts object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE %s = "%s"' % (self.indexField,account))
    if len(storeObjects) == 1:
      Receipts = storeObjects[0]
      #
      # change Receipts object
      #
      for attr in ReceiptsAttrs:
        if (attr not in standardAttrs) and self.transaction.request().field(attr,None) != None:
          if ReceiptsFields[attr][ReceiptsType] == 'string':
            Receipts.setValueForKey(attr, self.transaction.request().field(attr,''))
          elif ReceiptsFields[attr][ReceiptsType] == 'float':
            Receipts.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,''),',','.')))
          elif ReceiptsFields[attr][ReceiptsType] == 'datetime':
            if self.transaction.request().field(attr,''):
              Receipts.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              Receipts.setValueForKey(attr, None)
          elif ReceiptsFields[attr][ReceiptsType] == 'date':
            if self.transaction.request().field(attr,''):
              Receipts.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              Receipts.setValueForKey(attr, None)
      #
      # set standard attributes
      #
      Receipts.setChangedBy(self.transaction.session().value('authenticated_user',''))
      Receipts.setChangedAt(DateTime.now())
      Receipts.setChangedOn(self.getSite())
      #
      # store Receipts in database
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
    # back to Receipts page
    #
    self.transaction.response().sendRedirect('ReceiptsView?index=' + account[2:])
