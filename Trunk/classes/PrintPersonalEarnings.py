#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/classes/PrintPersonalRevenues.py $
# Version:   $Rev: 10 $
# Changed:   $Date: 2005-04-19 10:33:21 +0200 (Tue, 19 Apr 2005) $
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
__revision__ = "$Rev: 10 $"[6:-2]

from PrintRevenues import PrintRevenues

class PrintPersonalEarnings(PrintRevenues):

  description = ['Nachname',', ','Vorname','\n','Strasse','\n','PLZ',' ','Ort']
  revenueAccountPrefix = 'BK'
  bank = 1

  def __init__(self, *args, **KWs):
    PrintRevenues.__init__(self, *args, **KWs)
    self.title = 'Auszahlungen an Personal ( %s )' % self.organisation
