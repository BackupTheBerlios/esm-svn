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

import logging
from Config import loggingLevel

class Log:

  def __init__(self, *args, **KWs):
    #
    # use the standard logging package
    # log all messages into files
    #
    self.myLogger = logging.getLogger('esm')
    hdlr = logging.FileHandler('Logs/esm.log')
    if loggingLevel == logging.DEBUG:
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
    else:
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    self.myLogger.addHandler(hdlr) 
    self.myLogger.setLevel(loggingLevel)
    
    # self.myLogger.critical("set logging level = %s." % loggingLevel)
    
    self.myLogger.info("esm started.")
    
  def logger(self):
    return self.myLogger
    
Log = Log()
