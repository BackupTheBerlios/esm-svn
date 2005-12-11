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
from GlobalState import ID
import string

class TransferDelete(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)

  def writeContent(self, trans=None):
    #
    # this servlet deletes a Transfer
    #

    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    
    account = self.transaction.request().field('account','')
    taid = self.transaction.request().field('taid','')
    index = self.transaction.request().field('index',0)
    page = self.transaction.request().field('page','Main')
    #
    # get and delete transfer object
    #
    transferObjects = store.fetchObjectsOfClass('Transfers','WHERE TAID="%s"' % taid)
    transfer = transferObjects[0]
    store.deleteObject(transfer)
    #
    # store changes in database
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
    # back to old page
    #
    if index:
      self.transaction.response().sendRedirect(page + '?account=%s&index=%s' % (account,index))
    else:
      self.transaction.response().sendRedirect(page + '?account=%s' % account)
