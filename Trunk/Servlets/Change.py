#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/classes/MemberChange.py $
# Version:   $Rev: 18 $
# Changed:   $Date: 2005-05-11 17:24:24 +0200 (Wed, 11 May 2005) $
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
__revision__ = "$Rev: 18 $"[6:-2]

from SiteContent import SiteContent
from mx import DateTime
import string

class Change(SiteContent):

  def getStringField(self, field, default = ''):
    fieldValue = self.transaction.request().field(field,None)
    if fieldValue:
        return fieldValue
    else:
        return default
    
  def getIntegerField(self, field, default = '0'):
    fieldValue = self.transaction.request().field(field,None)
    if fieldValue:
        return int(fieldValue)
    else:
        return default
    
  def getFloatField(self, field, default = '0,0'):
    fieldValue = self.transaction.request().field(field,None)
    if fieldValue:
        return float(string.replace(fieldValue,',','.'))
    else:
        return default
    
  def getDateField(self, field, default = DateTime.now()):
    fieldValue = self.transaction.request().field(field,None)
    if fieldValue:
        return DateTime.DateTimeFrom(fieldValue)
    else:
        return default

  def updateStandardFields(self, record, errors = ''):
    #
    # set standard attributes for the record
    #
    record.changedBy = self.getLoggedInUser()
    record.changedAt = DateTime.now()
    record.changedOn = self.getSite()
    record.errorMessage = errors
