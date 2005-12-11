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

from Cheetah.Templates._SkeletonPage import _SkeletonPage
from MiscUtils.Funcs import uniqueId
from string import lower
import sha, os

#
# Constants
#
dateFormat = '%d.%m.%Y'
basicStyle = 'basic'
stylesDir = 'styles'

#
# read configuration file
#
f = open('@CONTEXT@/product.config','r')
config = eval(f.read())
f.close()
#
# and select required configuration information
#
roles = config['roles']
users = config['users']

site = config['site']
organisation = config['organisation']
link = config['link']
mail = config['mail']
title = config['title']

#
# read version file
#
f = open('@CONTEXT@/version.txt','r')
version = f.readline()
f.close()

class SiteBase(_SkeletonPage):

  role = ''

  def __init__(self, *args, **KWs):
    _SkeletonPage.__init__(self, *args, **KWs)
    self.dateFormat = dateFormat
    self.organisation = organisation
    self.title = title
    self.link = link
    self.site = site
    self.mail = mail

  def lazyCondition(self, condition):
    if condition:
      return eval(str(condition))
    else:
      return 0

  def isValidUserAndPassword(self, username, password):
    # Replace this with a database lookup, or whatever you're using for
    # authentication...
    return (username, sha.new(password).hexdigest()) in users

  def getRolesOfUser(self,user):
    return roles[user]

  def loginUser(self, username, password):
    username = lower(username)
    session = self.transaction.session()
    session.values().clear()
    if self.isValidUserAndPassword(username, password):
      session.setValue('authenticated_user', username)
      session.setValue('authenticated_roles', self.getRolesOfUser(username))
      return 1
    else:
      session.setValue('authenticated_user', None)
      session.setValue('authenticated_roles', None)
      return 0

  def getLoggedInUser(self):
    # Gets the name of the logged-in user, or returns None if there is
    # no logged-in user.
    return self.transaction.session().value('authenticated_user', None)

  def getStyle(self):
    style = self.transaction.session().value('style',None)
    if style:
        return style
    else:
        return basicStyle
        
  def getStylesDir(self):
    return "%s/%s" % (stylesDir,self.getStyle())
        
  def getAvailableStyles(self):
    return os.listdir(stylesDir)
      
  def getSite(self):
    return self.site

  def getTitle(self):
    return self.title

  def getOrganisation(self):
    return self.organisation

  def getLink(self):
    return self.link

  def getMail(self):
    return self.mail

  def getVersion(self):
    return version

  def checkRole(self,requiredRole):
    #
    # After looking if a user is authenticated you must check if he has the required role.
    # If this is a login the session info will be
    # updated. Only the Login page is accessable without authentication. Further your
    # it is checked, if you have the required role.
    #
    if requiredRole:
      if self.transaction.request().field('action','') == 'login':
        if not self.loginUser(self.transaction.request().field('username',''), self.transaction.request().field('password','')):
          self.transaction.response().sendRedirect('Login')
        elif requiredRole not in self.transaction.session().value('authenticated_roles',[]):
          self.transaction.response().sendRedirect('Main')
      elif not self.transaction.session().value('authenticated_user',None):
        self.transaction.response().sendRedirect('Login')
      elif requiredRole not in self.transaction.session().value('authenticated_roles',[]):
        self.transaction.response().sendRedirect('Main')
