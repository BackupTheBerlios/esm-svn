#
# File:      $URL$
# Version:   $rev$
# Changed:   $date$
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
__revision__ = "$Rev$"[4,-2]

from SiteTemplate import SiteTemplate
from mx import DateTime

class SetYear(SiteTemplate):

  def __init__(self, *args, **KWs):
    SiteTemplate.__init__(self, *args, **KWs)

  def writeContent(self, trans=None):
    year = int(self.transaction.request().field('year',DateTime.now().year))
    self.transaction.session().setValue('accountYear',year)
    page = self.transaction.request().field('page','Main')
    self.transaction.response().sendRedirect(page)
