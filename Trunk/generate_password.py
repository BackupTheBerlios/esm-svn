#! /usr/bin/python
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
__revision__ = "$Rev$"[4,-2]

import sys
import sha

password = sys.argv[1]
pw = sha.new(password).hexdigest()

if len(sys.argv) == 2:
    print pw
if len(sys.argv) == 3:
    f = open(sys.argv[2],"w")
    f.write(pw)
    f.close()