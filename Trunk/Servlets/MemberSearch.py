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

from SearchTemplate import SearchTemplate
from SqlObjects.Member import Member

class MemberSearch(SearchTemplate):

    subMenuPoints = [
        {'tmpl':'MemberNew','condition':1,'title':'Neues Mitglied','link':'MemberNew','role':'editor'},
        {'tmpl':'PrintTransfers','condition':1,'title':'Ausdruck','link':'PrintMemberTransfers?accountNb=*','role':'editor'},
        {'tmpl':'PrintSaldos','condition':1,'title':'Saldos','link':'PrintMemberSaldos?accountNb=*','role':'editor'},
    ]

    activeMenuPoint = 'Member'
    activeSubmenuPoint = 'MemberSearch'
    searchPage = 'MemberSearch'

    fieldkeys = ['accountNb','newAccountNb','firstName','lastName','birthDate','telefonPrivate','startFrom','endsAt']
    fields = {
        'accountNb':{'title':'MNr','width':'5%','type':''},
        'newAccountNb':{'title':'Neu','width':'5%','type':'','format':'"%s"[2:]'},
        'firstName':{'title':'Vorname','width':'20%','type':''},
        'lastName':{'title':'Nachname','width':'20%','type':''},
        'birthDate':{'title':'Geburtstag','width':'10%','type':'date'},
        'telefonPrivate':{'title':'Telefon','width':'15%','type':''},
        'startFrom':{'title':'Ein','width':'10%','type':'date'},
        'endsAt':{'title':'Aus','width':'10%','type':'date'}
    }

    tableTitle = 'Mitglieder'

    linkFields = ['accountNb','newAccountNb']
    linkPattern = 'MemberView?accountNb='

    def search(self, pattern='', context=''):
        return Member.search(pattern,context)
