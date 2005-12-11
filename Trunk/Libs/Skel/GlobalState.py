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

#
# read configuration file
#
if os.path.exists('@CONTEXT@/product.config'):
    f = open('@CONTEXT@/product.config','r')
else:
    f = open('../product.config','r')
config = eval(f.read())
f.close()
#
# and select required configuration information
#
dbUser = config['dbUser']
dbPassword = config['dbPassword']

try:
  from MiddleKit.Run.MySQLObjectStore import MySQLObjectStore
except:
    pass
    
class Store:

  def __init__(self):
    # Do something
    self.store = None
    # self.store = MySQLObjectStore(user=dbUser, passwd=dbPassword)
    # self.store.readModelFileNamed('@CONTEXT@/Middle/@PRODUCT@')

  def __call__(self):
    return self

  def store(self):
    return self.store

Store = Store()

class ID:

  def __init__(self):
    self.id = 0

  def __call__(self):
    return self

  def id(self):
    return self.id

  def next(self):
    self.id = (self.id + 1) % 1000
    return self.id

ID = ID()

dbConnection = MySQLConnection(user=dbUser,passwd=dbPassword,db='@PRODUCT@')
