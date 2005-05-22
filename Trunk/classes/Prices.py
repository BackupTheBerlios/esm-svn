#!/usr/bin/env python
# 
#  File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/templates/BLZ.tmpl $
#  Version:   $Rev: 12 $
#  Changed:   $Date: 2005-04-19 11:07:15 +0200 (Tue, 19 Apr 2005) $
# 
#  Homepage:  http://esm.berlios.de
#  Copyright: GNU Public License Version 2 (see license.txt)
# 
#  E-Sportmanager (esm)
# 
#  Copyright (C) 2005 Jan Gottschick
# 
#    This program is free software; you can redistribute it and/or modify it
#    under the terms of the GNU General Public License as published by the
#    Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
# 
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#    for more details.
# 
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the
# 
#    Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
# 
__author__ = "Jan Gottschick"
__revision__ = "$Rev: 12 $"[6:-2]

from Tables import Tables
from Price import Price

class Prices(Tables):

    activeSubmenuPoint = 'Prices'
    searchPage = 'Prices'
    tableStore = 'Price'

    fieldkeys = ['transferCode','description','account','soll','haben','newFrom','newSoll','newHaben']
    fields = {
              'transferCode':{'title':'BKZ','width':'5%','type':''},
              'description':{'title':'Beschreibung','width':'45%','type':''},
              'account':{'title':'Konto','width':'8%','type':''},
              'soll':{'title':'Soll','width':'8%','type':'currency'},
              'haben':{'title':'Haben','width':'8%','type':'currency'},
              'newFrom':{'title':'Neu ab ->','width':'8%','type':'date'},
              'newSoll':{'title':'Soll','width':'8%','type':'currency'},
              'newHaben':{'title':'Haben','width':'8%','type':'currency'}
            }
    
    tableTitle = 'Mitgliedsbeiträge und Gebühren'

    helpText = '''
            Währung bis 31.12.2001 in DM und ab dem 01.01.2002 in Euro
        '''
        
    def search(self, pattern, context=''):
        return Price.search(pattern,context)
