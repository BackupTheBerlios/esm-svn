#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/classes/skel/GlobalState.py $
# Version:   $Rev: 15 $
# Changed:   $Date: 2005-05-09 15:06:11 +0200 (Mon, 09 May 2005) $
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
__revision__ = "$Rev: 15 $"[6:-2]

from sqlobject.main import *
from sqlobject.col import *
from sqlobject.styles import *
from GlobalState import dbConnection,Version
from mx import DateTime

class BankCode(SQLObject):
    '''
        SQLObject for the bank codes database
    '''
    
    _connection = dbConnection
    
    bankName = StringCol(length=26)
    bankCode = StringCol(length=64)
    
    changedAt = DateTimeCol(default= DateTime.now())
    changedAtSite = StringCol(length=2, varchar=False, default = '  ')
    changedBy = StringCol(length=32, default = '')

class blz(SQLObject):
    '''
        SQLObject for the MiddleKit database format
    '''

    _connection = dbConnection
    _fromDatabase = True
    _idName = 'bLZId'
    _style = MixedCaseStyle(longID=True)

#
# Transform and update database if required
#

# which is the actual version
v = Version.selectBy(context='bankcode')
if v.count() == 1:
    versionNb = v[0].versionNb
else:
    versionNb = 0
    Version(context='bankcode',versionNb=0)

# transform database to SQLObject format
if versionNb <= 0:
    BankCode.createTable(ifNotExists=True)
    for x in blz.select():
        print x.bank
        BankCode(
            bankName=x.bank,
            bankCode=x.bLZ,
            changedAt=x.changedAt,
            changedAtSite=x.changedOn,
            changedBy=x.changedBy)

# store actual version number
versionNb = 1
v = Version.selectBy(context='bankcode')
v[0].versionNb = versionNb