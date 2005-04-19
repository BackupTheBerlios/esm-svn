#!/usr/bin/env python
#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/classes/__init__.py $
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

import sys
import getopt
import string
from mx.DateTime import *

def print_usage():
  print "usage: blz-bundesbank.py [ OPTIONS ] file"
  print "..."
  print "Optionen und Argumente:"
  print "--help           : detaillierte Beschreibung"
  print "--csv            : Ausgabe als Listenformat mit Kommata als Trennzeichen"
  print "--sql            : Ausgabe als SQL-Befehle zum Einfügen in eine Tabelle BLZ"
  print "file             : Dateiname der Textdatei von der Bundesbank"
  print

def print_help():
  print "Mit dem Programm 'blz-bundesbank.py' können Sie"

try:
  optlist, args = getopt.getopt(sys.argv[1:],'',['csv','sql'])
except:
  print_usage()
else:
  if ('--help','') in optlist:
    print_help()
  elif len(args) != 1:
    print_usage()
  else:
    f = open(args[0])
    lines = f.readlines()
    f.close()
    if ('--sql','') in optlist:
      print 'use esm;'
      print 'delete from BLZ;'
      for x in lines:
        if (len(x) > 8) and (x[8] == '1') and (x[0:8] != '00000000'):
          print "INSERT INTO BLZ (BLZ,Bank,ChangedOn,ChangedAt,ChangedBy) VALUES ('%s','%s','JG','%s','Jan Gottschick');" %  (x[0:8],string.strip(x[139:165]),now().strftime('%d.%m.%Y'))
    elif ('--csv','') in optlist:
      print 'BLZ objects,,'
      print 'BLZ,Bank,ChangedOn,ChangedAt,ChangedBy'
      for x in lines:
        if (len(x) > 8) and (x[8] == '1') and (x[0:8] != '00000000'):
          print "%s,%s,JG,%s,Jan Gottschick" %  (x[0:8],string.strip(x[139:165]),'03/21/2002')
    else:
      print "<ENTRIES table='blz'>"
      for x in lines:
        if (len(x) > 8) and (x[8] == '1') and (x[0:8] != '00000000'):
          print "  <ENTRY>"
          print "    <BLZ>%s</BLZ>" % x[0:8]
          print "    <BANK>%s</BANK>" % string.strip(x[139:165])
          print "  </ENTRY>"
      print "</ENTRIES>"
