#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/Servlets/skel/SiteBase.py $
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

from Cheetah.Templates._SkeletonPage import _SkeletonPage
from MiscUtils.Funcs import uniqueId

import sha
import os

from Libs.Config import *
from Libs.Settings import *
from Libs.Log import Log

from SqlObjects.Member import Member

#
# Constants
#
dateFormat = '%d.%m.%Y'
basicStyle = 'basic'
stylesDir = 'Styles'

rolesTable = {
    '':[],
    'member':['member'],
    'viewer':['member','viewer'],
    'editor':['member','viewer','editor'],
    'auditor':['member','viewer','editor','auditor'],
    'manager':['member','viewer','editor','auditor','manager'],
}

#
# read version file
#
f = open('Libs/version.txt','r')
version = f.readline()
f.close()

class LoginError(Exception):
    """Exception class for all errors during Login validation"""
    pass

class SiteBase(_SkeletonPage):

  role = ''

  def __init__(self, *args, **KWs):
    _SkeletonPage.__init__(self, *args, **KWs)
    #
    # provide global variables from Config and Settings
    #
    self.dateFormat = dateFormat
    self.organisation = organisation
    self.title = title
    self.link = link
    self.site = site
    self.mailAddress = mailAddress
    self.mailHost = mailHost
    self.mailUser = mailUser
    self.mailPassword = mailPassword
    #
    # provide logger
    #
    self.logger = Log.logger()
    
  #
  # provide logging functions
  #
  def debug(self, msg, *args, **kwargs):
      return self.logger.debug(msg, *args,**kwargs)
      
  def info(self, msg, *args, **kwargs):
      return self.logger.info(msg, *args, **kwargs)
      
  def warning(self, msg, *args, **kwargs):
      return self.logger.warning(msg, *args, **kwargs)
      
  def error(self, msg, *args, **kwargs):
      return self.logger.error(msg, *args, **kwargs)
      
  def critical(self, msg, *args, **kwargs):
      return self.logger.critical(msg,*args, **kwargs)

  def fatal(self, msg, *args, **kwargs):
      return self.logger.fatal(msg, *args, **kwargs)

  def exception(self, msg, *args, **kwargs):
      return self.logger.exception(msg, *args, **kwargs)

  def lazyCondition(self, condition):
    if condition:
      return eval(str(condition))
    else:
      return 0

  #
  # main function to validate user and password
  #
  def validateUserAndPassword(self, username, password):
    '''
        Looks first if the user is configured in the configuration file,
        e.g. standard users like the "manager" account. If not the user
        databases, like "Member", are checked. The encrypted password is
        validated.
    '''
    if (username, sha.new(password).hexdigest()) not in users:
        if len(username) >= 2:
            # which database to use for user authentification
            if username[:2].lower() == "mi":
                user= Member.search(username[2:])
            else:
                self.warning("wrong prefix for username '%s'" % username)
                raise LoginError, "WrongUsername"
            # check user exist and unique
            if user.count() == 0:
                self.warning("user '%s' not found" % username)
                raise LoginError, "WrongUsername"
            elif user.count() > 1:
                self.warning("User '%s' not unique" % username)
                raise LoginError, "WrongUsername"
            else:
                # check password
                if user[0].passwordHash == sha.new(password).hexdigest():
                    # correct user from Member database
                    self.info("User '%s' authorized" % username)
                else:
                    self.warning("Wrong password for user '%s' in Member database" % username)
                    raise LoginError, "WrongPassword"
        else:
            self.warning("Username '%s' to short" % username)
            raise LoginError, "WrongUsername"

  def getRolesOfUser(self,username):
      if username in roles:
        return roles[username]
      else:
        if len(username) >= 2:
            if username[:2].lower() == "mi":
                user = Member.search(username[2:])
            else:
                # wrong prefix of username
                return []
            if user.count() == 1:
                # get roles from database of user
                return rolesTable[user[0].role]
            else:
                # user not unique or doesn't exist
                return []
        else:
            # wrong user name
            return []

  def loginUser(self, username, password):
    username = username.lower()
    session = self.transaction.session()
    session.values().clear()
    if username and username[0].isdigit():
        username = "MI%s" % username
    # user is not authenticated
    session.setValue('authenticated_user', None)
    session.setValue('authenticated_roles', None)
    # validateUserAndPassword can fail with an LoginError exception
    self.validateUserAndPassword(username, password)
    # user is authenticated, now
    session.setValue('authenticated_user', username)
    session.setValue('authenticated_roles', self.getRolesOfUser(username))

  def getLoggedInUser(self):
    # Gets the name of the logged-in user, or returns None if there is
    # no logged-in user.
    return self.transaction.session().value('authenticated_user', None)

  def getLanguage(self, dir, usage):
      langFiles = os.listdir("%s/%s" % (context,dir))
      langs = self.transaction.request().environ()['HTTP_ACCEPT_LANGUAGE'].split(',')
      for x in langs:
          l = x.split(';')[0]
          if '%s-%s' % (l,usage) in langFiles:
              return l
      return "_"
      
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

  def getMailAddress(self):
    return self.mailAddress

  def getMailHost(self):
    return self.mailHost

  def getMailUser(self):
    return self.mailUser

  def getMailPassword(self):
    return self.mailPassword

  def getVersion(self):
    return version

  def checkRole(self,requiredRole):
    #
    # After testing if a user is authenticated you must check if he has the required role.
    # If this is a login the session info will be
    # updated. Only the Login page is accessable without authentication. Further your
    # it is checked, if you have the required role.
    #
    if requiredRole:
      if self.transaction.request().field('action','') == 'login':
        try:
            self.loginUser(self.transaction.request().field('username',''), self.transaction.request().field('password',''))
            if requiredRole not in self.transaction.session().value('authenticated_roles',[]):
                self.transaction.response().sendRedirect('Main')
        except LoginError, e:
            self.transaction.response().sendRedirect('Login?error=%s' % e)
      elif not self.transaction.session().value('authenticated_user',None):
        self.transaction.response().sendRedirect('Login')
      elif requiredRole not in self.transaction.session().value('authenticated_roles',[]):
        self.transaction.response().sendRedirect('Main')
