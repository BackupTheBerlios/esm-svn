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

from sqlobject.main import *
from sqlobject.col import *
from sqlobject.mysql.mysqlconnection import *

from Config import dbConnection

class Version(SQLObject):
    '''
        This class implements the database access using the SQL Object library.
        The table "version" stores the actual deployed version of a table, used
        to store the transfers or account information. If the table structure of
        such a table changes the version number should be incremented. If the
        actual table is not up to date then the supporting code can upgrade the
        table content at startup time.
    '''
    
    _connection = dbConnection
    
    context = StringCol()
    versionNb = IntCol()

# create table
Version.createTable(ifNotExists=True)
dbConnection.query('ALTER TABLE %s.`version` TYPE = MYISAM;' % dbConnection.db)

# upgrade "version" table
v = Version.selectBy(context='version')
if v.count() == 1:
    versionNb = v[0].versionNb
else:
    versionNb = 0
    Version(context='version',versionNb=0)

versionNb = 1
v = Version.selectBy(context='version')
v[0].versionNb = versionNb
