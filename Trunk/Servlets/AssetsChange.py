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
import string

true = 1 == 1
false = 1 != 1

AssetsType = 0
AssetsRequired = 1
AssetsFields = {
  'ID':['string',1],
  'Nr':['string',1],
  'Name':['string',1],
  'Kommentare':['string',0],
  }

AssetsAttrs = AssetsFields.keys()
standardAttrs = ['ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class AssetsChange(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsVV'
    self.indexField = 'ID'

  def writeContent(self, trans=None):
    #
    # this servlet changes Assets data
    #

    account = self.transaction.request().field('account','')
    page = self.transaction.request().field('page','Main')
    #
    # retrieve Assets object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE %s = "%s"' % (self.indexField,account))
    if len(storeObjects) == 1:
      Assets = storeObjects[0]
      #
      # change Assets object
      #
      for attr in AssetsAttrs:
        if (attr not in standardAttrs) and self.transaction.request().field(attr,None) != None:
          if AssetsFields[attr][AssetsType] == 'string':
            Assets.setValueForKey(attr, self.transaction.request().field(attr,''))
          elif AssetsFields[attr][AssetsType] == 'float':
            Assets.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,''),',','.')))
          elif AssetsFields[attr][AssetsType] == 'datetime':
            if self.transaction.request().field(attr,''):
              Assets.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              Assets.setValueForKey(attr, None)
          elif AssetsFields[attr][AssetsType] == 'date':
            if self.transaction.request().field(attr,''):
              Assets.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
            else:
              Assets.setValueForKey(attr, None)
      #
      # set standard attributes
      #
      Assets.setChangedBy(self.transaction.session().value('authenticated_user',''))
      Assets.setChangedAt(DateTime.now())
      Assets.setChangedOn(self.getSite())
      #
      # store Assets in database
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
    # back to Assets page
    #
    self.transaction.response().sendRedirect('AssetsView?index=' + account[2:])
