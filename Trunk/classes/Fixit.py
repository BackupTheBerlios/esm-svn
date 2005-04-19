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

class Fixit(SiteTemplate):

  def __init__(self, *args, **KWs):
    SiteTemplate.__init__(self, *args, **KWs)

  def writeContent(self, trans=None):
    #
    # this servlet creates and stores a new Transfer
    #

    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    
    page = self.transaction.request().field('page','Main')
    #
    # change transfer object
    #
    transferObjects = store.fetchObjectsOfClass('Transfers','WHERE Konto2 like "10%"')
    for transfer in transferObjects:
      attrs = transfer.allAttrs(0)
      transfer.setKonto2(attrs['Konto1'])
      transfer.setKonto1('EK3000Ein')
      haben = attrs['Haben']
      transfer.setHaben(attrs['Soll'])
      transfer.setSoll(haben)
      #
      # store transfer in database
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

    transferObjects = store.fetchObjectsOfClass('Transfers','WHERE Konto2 like "11%"')
    for transfer in transferObjects:
      attrs = transfer.allAttrs(0)
      transfer.setKonto2(attrs['Konto1'])
      transfer.setKonto1('EK3100Ein')
      haben = attrs['Haben']
      transfer.setHaben(attrs['Soll'])
      transfer.setSoll(haben)
      #
      # store transfer in database
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
    self.transaction.response().sendRedirect(page)
