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
from Member import Member

class MemberLedger(LedgerTemplate):

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
        'title':'Konto',
        'link':''
      },
      {'tmpl':'Member','title':'> Einzahlung',
        'condition':1,
        'link':'MemberTransferEin?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Auszahlung',
        'condition':1,
        'link':'MemberTransferAus?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Stornierung',
        'condition':1,
        'link':'MemberTransferStorno?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Schwimmkurs',
        'condition':1,
        'link':'MemberTransfer11Sc?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Mahngebühr',
        'condition':1,
        'link':'MemberTransferMahn?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Verw. Gebühr',
        'condition':1,
        'link':'MemberTransferVerw?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Gut. Aufnahme',
        'condition':1,
        'link':'MemberTransferGutAuf?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Gut. Beitrag',
        'condition':1,
        'link':'MemberTransferGutBei?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Gut. Kursgebühr',
        'condition':1,
        'link':'MemberTransferGutKu?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Gut. Stornierung',
        'condition':1,
        'link':'MemberTransferGutSto?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Gut. Mahnung',
        'condition':1,
        'link':'MemberTransferGutMahn?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Ratenzahlung',
        'condition':1,
        'link':'MemberTransferRaten?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'Member','title':'> Spende',
        'condition':1,
        'link':'MemberTransferSpende?id=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
      {'tmpl':'PrintTransfers',
        'title':'> Ausdruck',
        'condition':1,
        'link':'PrintMemberTransfers?accounts=#echo $request.field("account",$transaction.session.value("account",""))#&index=#echo $request.field("index",$transaction.session.value("index",0))#',
        'role':'editor'
      },
    ]

    titles = [
      {"title":'Datum',"width":'10%'},
      {"title":'BKZ / Kto',"width":'10%'},
      {"title":'Empfänger / Bemerkung',"width":'56%'},
      {"title":'Soll',"width":'8%'},
      {"title":'Haben',"width":'8%'},
      {"title":'Saldo',"width":'8%'}
    ]

    fields1 = [
      {"name":'bookingDate',"type":'date'},
      {"name":'transferCode',"type":'string'},
      {"name":'who',"type":'string'},
      {"name":'debit',"type":'currency'},
      {"name":'credit',"type":'currency'},
      {"name":'NA1',"type":''}
    ]

    fields2 = [
      {"name":'NA1',"type":'editlink'},
      {"name":'account',"type":'string'},
      {"name":'description',"type":'string'},
      {"name":'NA3',"type":''},
      {"name":'NA4',"type":''},
      {"name":'saldo',"type":'currency'}
    ]

    accountFields = [
      {'name':'accountNb','title':'MNr','width':'5%','type':''},
      {'name':'firstName','title':'Name','width':'20%','type':''},
      {'name':'lastName','title':'','width':'20%','type':'name'},
      {'name':'birthDate','title':'Geb','width':'10%','type':'date'},
      {'name':'telefonPrivate','title':'Tel','width':'15%','type':''},
      {'name':'startFrom','title':'Ein','width':'10%','type':'date'},
      {'name':'endsAt','title':'Aus','width':'10%','type':'date'}
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
