#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/templates/LedgerTemplate.tmpl $
# Version:   $Rev: 15 $
# Changed:   $Date: 2005-05-09 15:06:11 +0200 (Mon, 09 May 2005) $
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
__revision__ = "$Rev: 15 $"[6:-2]

from EditMemberTemplate import EditMemberTemplate
from Member import Member
from Id import Id
    
class MemberNew(EditMemberTemplate):
    activeMenuPoint = 'Member'
    activeSubmenuPoint = 'MemberNew'
    searchPage = 'MemberSearch'
    editPage = 'MemberChange'
    
    subMenuPoints = [
        {'tmpl':'MemberNew','condition':1,'title':'Neues Mitglied','link':'MemberNew'}
    ]
    
    editTitle1 = 'neues Mitglied'
    editTitle2 = 'Mitgliedsdaten'
    
    inheritAttributesFrom0 = ['lastName','guardianFirstName','guardianLastName',
        'addressExtension','street','city','zipCode','countryCode',
        'telefonPrivate','telefonOffice','telefonMobile','fax','email']
    
    inputForm = [
      {
        'name':"accountNb",
        'type':"hidden"
      },
      {
        'title':"Vorname",
        'name':"firstName",
        'type':"text",
        'size':64
      },
      {
        'title':"Nachname",
        'name':"lastName",
        'type':"text",
        'size':64
      },
      {
        'title':"Vorname gV",
        'name':"guardianFirstName",
        'type':"text",
        'size':64
      },
      {
        'title':"Nachname gV",
        'name':"guardianLastName",
        'type':"text",
        'size':64
      },
      {
        'title':"Titel",
        'name':"title",
        'type':"text",
        'size':32
      },
      {
        'title':"Geburtsdatum",
        'name':"birthdate",
        'type':"date",
      },
      {
        'title':"Geschlecht",
        'name':"gender",
        'type':"select",
        'options':[
          {"value":"m","title":"männlich"},
          {"value":"w","title":"weiblich"}
          ]
      },
      {
        'title':"Adresszusatz",
        'name':"addressExtension",
        'type':"text",
        'size':32
      },
      {
        'title':"Strasse",
        'name':"street",
        'type':"text",
        'size':64
      },
      {
        'title':"Ort",
        'name':"city",
        'type':"text",
        'default':'Berlin',
        'size':64
      },
      {
        'title':"Land",
        'name':"countryCode",
        'type':"text",
        'default':'de',
        'size':2
      },
      {
        'title':"PLZ",
        'name':"zipCode",
        'type':"text",
        'size':10
      },
      {
        'title':"Telefon (Privat)",
        'name':"telefonPrivate",
        'type':"text",
        'size':32
      },
      {
        'title':"Telefon (Dienst)",
        'name':"telefonOffice",
        'type':"text",
        'size':32
      },
      {
        'title':"Telefon (Mobil)",
        'name':"telefonMobile",
        'type':"text",
        'size':32
      },
      {
        'title':"FAX",
        'name':"fax",
        'type':"text",
        'size':32
      },
      {
        'title':"E-Mail",
        'name':"email",
        'type':"text",
        'size':64,
        'max':128
      },
      {
        'title':"Beitragsart",
        'name':"membershipKind1",
        'type':"select",
        'options':[
          {"value":"10Ju","title":"Jugendliche"},
          {"value":"10Er","title":"Erwachsene"},
          {"value":"10Fa","title":"Familie mit 1 Erwachsenen"},
          {"value":"10Fi","title":"Familie mit 2 Erwachsenen"},
          {"value":"10pa","title":"Passives Mitglied"},
          {"value":"10F","title":"Fördermitglied"},
          {"value":"10Em","title":"Ehrenmitglied"},
          {"value":"10Jg","title":"Jugendliche (Trainer)"},
          {"value":"10Ew","title":"Erwachsene (Trainer)"},
          {"value":"10Fm","title":"Familie mit 1 Erwachsenen (Trainer)"},
          {"value":"10Fl","title":"Familie mit 2 Erwachsenen (Trainer)"},
          {"value":"10ps","title":"Passives Mitglied (Trainer)"},
          {"value":"10AT","title":"Aushilfstrainer"},
          ]
      },
      {
        'title':"Eintritt am",
        'name':"startFrom",
        'type':"date",
      },
      {
        'title':"Zahlungsart",
        'name':"payBy",
        'type':"select",
        'options':[
          {"value":"Lastschrift","title":"Lastschrift"},
          {"value":"Rechnung","title":"Rechnung"}
          ]
      },
      {
        'title':"Lastschrift ab",
        'name':"automaticPayFrom",
        'type':"date",
      },
      {
        'title':"Rechnung ab",
        'name':"invoiceFrom",
        'type':"date",
      },
      {
        'title':"Bankverbindungen",
        'type':"table",
        'number':2,
        'fieldlist':['bankAccountNb','bankCode','bankName','bankAccountOwner'],
        'fieldType':{
          'bankAccountNb':'text',
          'bankCode':'text',
          'bankName':'text',
          'bankAccountOwner':'text'
        },
        'fieldTitle':{
          'bankAccountNb':'KontoNr',
          'bankCode':'BLZ',
          'bankName':'Bank',
          'bankAccountOwner':'Kontoinhaber'
        }
      },
      {
        'title':"Kommentare",
        'name':"newComment",
        'type':"textarea",
        'size':5
      },
      {
        'title':"Wiedervorlage am",
        'name':"FollowUpDate",
        'type':"date",
      }
    ]
    
    helpText = ""
    
    def search(self, pattern='', context=''):
        return Member.search(pattern,context)
            
    def getAttrs(self, accountNb=''):
        '''
            returns all predefined attributes for the new member
        '''
        attrs = {}
        if accountNb:
            #
            # if accountNb is given, a new family member is requested
            #
            
            # copy the attributes to be inherited from the main record of the family
            mainRecord = self.search('%s0' % accountNb[:-1])
            iAttrs = mainRecord[0].allAttrs()
            for x in self.inheritAttributesFrom0:
                attrs[x] = iAttrs[x]
            
            # calculate next accountNb for the new family member
            familyRecords = self.search('%s_' % accountNb[:-1])
            nbOfFamilyMember = familyRecords.count()
            attrs['accountNb'] = accountNb[:-1] + str(nbOfFamilyMember)
        else:
            #
            # new main member
            #

            # get next free member id
            memberId = Id.search('Member')[0]
            memberId.lastId = memberId.lastId + 10
            attrs['accountNb'] = str(memberId.lastId)
        return attrs
