#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/classes/skel/GlobalState.py $
# Version:   $Rev: 24 $
# Changed:   $Date: 2005-05-22 18:39:44 +0200 (Sun, 22 May 2005) $
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
__revision__ = "$Rev: 24 $"[6:-2]

import string

from sqlobject.main import *
from sqlobject.col import *
from sqlobject.mysql.mysqlconnection import *

from Libs.Config import *

from SqlObjects.Version import Version

class Setting(SQLObject):
    '''
        This class implements the database access using the SQL Object library.
        The table "setting" stores the customer specific settings for the actual
        sport club represented by the database.
    '''
    
    _lazyUpdate = True # update records on demand
    _connection = dbConnection

    context = StringCol()
    value = StringCol()
    
    def search(self, pattern='', context=''):
        pattern = string.replace(string.lower(pattern),'*','%')
        pattern = string.replace(string.lower(pattern),'?','_')
        if pattern:
            return self.select("context LIKE '%s'" % pattern, orderBy="context")
        else:
            return self.select(orderBy="context")
            
    search = classmethod(search)
        
    def allAttrs(self):
        attrs = {}
        attrs['context'] = self.context
        attrs['value'] = self.value
        return attrs

# upgrade "setting" table

# which is the actual version
v = Version.selectBy(context='setting')
if v.count() == 1:
    versionNb = v[0].versionNb
else:
    versionNb = 0
    Version(context='setting',versionNb=0)

# transform database to SQLObject format
if versionNb <= 0:
    Setting.createTable(ifNotExists=True)
    if isinstance(dbConnection,MySQLConnection):
        dbConnection.query('ALTER TABLE %s.`member` TYPE = MYISAM;' % dbConnection.db)
    Setting(context="site",value="office")
    Setting(context="organisation",value="My Sport Club")
    Setting(context="link",value="www.my_sport_club.org")
    Setting(context="mailAddress",value="support@my_sport_club.org")
    Setting(context="mailHost",value="")
    Setting(context="mailUser",value="")
    Setting(context="mailPassword",value="")
    Setting(context="title",value="My Sport Club Office")

# store actual version number
versionNb = 1
v = Version.selectBy(context='setting')
v[0].versionNb = versionNb
