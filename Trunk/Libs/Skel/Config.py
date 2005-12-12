#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/Servlets/skel/GlobalState.py $
# Version:   $Rev: 37 $
# Changed:   $Date: 2005-12-11 15:20:47 +0100 (So, 11 Dez 2005) $
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
__revision__ = "$Rev: 37 $"[6:-2]

from sqlobject.mysql.mysqlconnection import *

import os

context = "@CONTEXT@"

#
# read configuration file
#
if os.path.exists('Libs/product-@CONTEXT@.config'):
    f = open('Libs/product-@CONTEXT@.config','r')
else:
    f = open('../product-@CONTEXT@.config','r')
config = eval(f.read())
f.close()
#
# and select required configuration information
#
dbUser = config['dbUser']
dbName = config['dbName']
dbPassword = config['dbPassword']

roles = config['roles']
users = config['users']

site = config['site']
organisation = config['organisation']
link = config['link']
mail = config['mail']
title = config['title']

dbConnection = MySQLConnection(user=dbUser,passwd=dbPassword,db=dbName)
