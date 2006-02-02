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

from LedgerTemplate import LedgerTemplate
from SqlObjects.Member import Member

class MemberLedger(LedgerTemplate):

    section = 'member'
    
    activeMenuPoint = 'Member'
    activeSubmenuPoint = 'MemberLedger'

    subMenuPoints = [
      {'tmpl':'MemberView',
        'condition':1,
        'title':'Info',
        'link':'MemberView?accountNb=#echo $request.field("account",$transaction.session.value("account",""))[2:]#'
      },
      {'tmpl':'MemberLedger',
        'condition':1,
        'title':'Account',
        'link':''
      },
      {'tmpl':'Member',
        'title':'Credit',
        'condition':1,
        'link':'MemberTransferEin?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'Debit',
        'condition':1,
        'link':'MemberTransferAus?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'Cancel',
        'condition':1,
        'link':'MemberTransferStorno?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'Swimming',
        'condition':1,
        'link':'MemberTransfer11Sc?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'Reminder',
        'condition':1,
        'link':'MemberTransferMahn?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'Management',
        'condition':1,
        'link':'MemberTransferVerw?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'CreditNewmember',
        'condition':1,
        'link':'MemberTransferGutAuf?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'CreditMembership',
        'condition':1,
        'link':'MemberTransferGutBei?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'CreditCourse',
        'condition':1,
        'link':'MemberTransferGutKu?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'CreditCancel',
        'condition':1,
        'link':'MemberTransferGutSto?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'CreditReminder',
        'condition':1,
        'link':'MemberTransferGutMahn?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'PayStepByStep',
        'condition':1,
        'link':'MemberTransferRaten?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member',
        'title':'Gift',
        'condition':1,
        'link':'MemberTransferSpende?id=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'PrintTransfers',
        'title':'Print',
        'condition':1,
        'link':'PrintMemberTransfers?accounts=#echo $request.field("account",$transaction.session.value("account",""))#&amp;index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
    ]

    titles = [
      {"title":'date',"width":'10%'},
      {"title":'transferCode-account',"width":'10%'},
      {"title":'receiver-comment',"width":'56%'},
      {"title":'debit',"width":'8%'},
      {"title":'credit',"width":'8%'},
      {"title":'saldo',"width":'8%'}
    ]

    fields1 = [
      {"name":'bookingDate',"type":'date',"width":'10%'},
      {"name":'transferCode',"type":'string',"width":'10%'},
      {"name":'who',"type":'string',"width":'56%'},
      {"name":'debit',"type":'currency',"width":'8%'},
      {"name":'credit',"type":'currency',"width":'8%'},
      {"name":'NA1',"type":'',"width":'8%'}
    ]

    fields2 = [
      {"name":'NA1',"type":'editlink',"width":'10%'},
      {"name":'account',"type":'string',"width":'10%'},
      {"name":'description',"type":'string',"width":'56%'},
      {"name":'NA3',"type":'',"width":'8%'},
      {"name":'NA4',"type":'',"width":'8%'},
      {"name":'saldo',"type":'currency',"width":'8%'}
    ]

    accountFields = [
      {'name':'accountNb','width':'5%','type':''},
      {'name':'firstName','width':'20%','type':''},
      {'name':'lastName','width':'20%','type':'name'},
      {'name':'birthDate','width':'10%','type':'date'},
      {'name':'telefonPrivate','width':'15%','type':''},
      {'name':'startFrom','width':'10%','type':'date'},
      {'name':'endsAt','width':'10%','type':'date'}
    ]

    ledgerTitle = 'Kontoauszug'

    linkPattern = 'MemberLedger?account=MI'
    linkFields = ['accountNb']
    searchPage = 'MemberLedgerSearch'
    editLink = 'MemberTransferModify'
    deleteLink = 'MemberTransferDelete'
    
    #
    # which account and how to search
    #
    def search(self, pattern, context=''):
        return Member.search(pattern,context)
