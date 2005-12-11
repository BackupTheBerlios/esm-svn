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
from BankCode import BankCode

class BLZ(Tables):

    activeSubmenuPoint = 'BLZ'
    searchPage = 'BLZ'
    tableStore = 'BankCode'

    fieldkeys = ['bankCode','bankName']
    fields = {
                'bankCode':{'title':'BLZ','width':'10%','type':''},
                'bankName':{'title':'Bank','width':'30%','type':''}
            }
    
    tableTitle = 'Bankleitzahlen'

    helpText = '''
            Die Bankleitzahlen stammen von der <a href="http://www.bundesbank.de">
            Bundesbank</a>.' +   'Zum Suchen können Muster angegeben werden. So
            kann * einen' +   'beliebigen Text ersetzen, während ? ein beliebiges
            Zeichen findet.
        '''
        
    def search(self, pattern, context=''):
        return BankCode.search(pattern,context)
