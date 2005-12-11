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

import string

from sqlobject.main import *
from sqlobject.col import *
from sqlobject.styles import *
from sqlobject.mysql.mysqlconnection import *

from GlobalState import dbConnection
from Version import Version
from mx import DateTime

class Id(SQLObject):
    '''
        SQLObject for the bank codes database
    '''
    
    _connection = dbConnection
    
    tableName = StringCol(length=64)
    lastId = IntCol(default=0)
    lastschriften = StringCol(length=64, default='')
    
    def search(self, pattern='', context=''):
        return self.select("table_name LIKE '%s'" % pattern, orderBy = "table_name")
            
    search = classmethod(search)
        
    def allAttrs(self):
        attrs = {}
        attrs['tableName'] = self.tableName
        attrs['lastId'] = self.lastId
        attrs['lastschriften'] = self.lastschriften
        return attrs    

#
# old table and its class is only required if version <= 0
#
try:
    class ids(SQLObject):
        '''
            SQLObject for the MiddleKit database format
        '''
    
        _connection = dbConnection
        _fromDatabase = True
        _idName = 'iDsId'
        _style = MixedCaseStyle(longID=True)
except:
    pass

#
# Transform and update database if required
#

# which is the actual version
v = Version.selectBy(context='id')
if v.count() == 1:
    versionNb = v[0].versionNb
else:
    versionNb = 0
    Version(context='id',versionNb=0)

# transform database to SQLObject format
if versionNb <= 0:
    Id.createTable(ifNotExists=True)
    if isinstance(dbConnection,MySQLConnection):
        dbConnection.query('ALTER TABLE %s.`id` TYPE = MYISAM;' % dbConnection.db)
    for x in ids.select():
        Id(
            tableName=x.tablename,
            lastId=x.lastID,
            lastschriften=x.lastschriften)
    member = Id.search('AccountsMI')
    member[0].tableName = 'Member'
            
# store actual version number
versionNb = 1
v = Version.selectBy(context='id')
v[0].versionNb = versionNb
