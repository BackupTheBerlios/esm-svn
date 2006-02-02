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

from ViewMemberTemplate import ViewMemberTemplate
from SqlObjects.Member import Member

class MemberView(ViewMemberTemplate):
    
    section = 'member'
    
    activeMenuPoint = 'Member'
    activeSubmenuPoint = 'MemberView'

    transferPrefix = 'MI'
    
    subMenuPoints = [
      {'tmpl':'MemberView',
        'condition':1,
        'title':'Info',
        'link':''
      },
      {'tmpl':'MemberLedger',
        'condition':1,
        'title':'Account',
        'link':'MemberLedger?account=%s#echo $request.field("accountNb","")[:-1] #0' % transferPrefix
      },
      {'tmpl':'MemberNew',
        'condition':1,
        'title':'MemberNew',
        'link':'MemberNew',
        'role':'editor'
      },
      {'tmpl':'MemberNewFamily',
        'condition':1,
        'title':'MemberNewFamily',
        'link':'MemberNew?accountNb=#echo $request.field("accountNb","")[:-1] #0',
        'role':'editor'
      },
      {'tmpl':'MemberModify',
        'condition':'self.request().field("accountNb","")[-1:] == "0"',
        'title':'MemberModify',
        'link':'MemberModify?accountNb=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberOfFamilyModify',
        'condition':'self.request().field("accountNb","")[-1:] != "0"',
        'title':'Ändern',
        'link':'MemberOfFamilyModify?accountNb=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberAustritt',
        'condition':1,
        'title':'MemberAustritt',
        'link':'MemberAustritt?accountNb=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberReactivate',
        'condition':'self.request().field("accountNb","")[-1:] == "0"',
        'title':'MemberReactivate',
        'link':'MemberReactivate?accountNb=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberReactivate2',
        'condition':'self.request().field("accountNb","")[-1:] != "0"',
        'title':'MemberReactivate',
        'link':'MemberReactivate2?accountNb=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberFee',
        'condition':'self.request().field("accountNb","")[-1:] == "0"',
        'title':'MemberFee',
        'link':'MemberFee?accountNb=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberToFamily',
        'condition':'self.request().field("accountNb","")[-1:] == "0"',
        'title':'MemberToFamily',
        'link':'MemberToFamily?MitgliedsNr=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberToSingle',
        'condition':'self.request().field("accountNb","")[-1:] != "0"',
        'title':'MemberToSingle',
        'link':'MemberToSingle?MitgliedsNr=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberToPersonal',
        'condition':1,
        'title':'MemberToPersonal',
        'link':'MemberToPersonal?MitgliedsNr=$request.field("accountNb","")',
        'role':'editor'
      },
      {'tmpl':'MemberPrintEintritt',
        'condition':1,
        'title':'MemberPrintEintritt',
        'link':'MemberPrintEintritt?MitgliedsNr=$request.field("accountNb","")',
        'role':'editor'
      },
    ]
    
    viewTitle = 'Mitglied'

    def search(self, pattern='', context=''):
        return Member.search(pattern,context)
