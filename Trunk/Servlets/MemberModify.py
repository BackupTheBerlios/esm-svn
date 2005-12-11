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
#  or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#   for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the
#
#   Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
__author__ = "Jan Gottschick"
__revision__ = "$Rev: 14 $"[6:-2]

from EditMemberTemplate import EditMemberTemplate
from Member import Member

class MemberModify(EditMemberTemplate):
    
    activeMenuPoint = 'Member'
    activeSubmenuPoint = 'MemberEdit'
    searchPage = 'MemberSearch'
    editPage = 'MemberChange'
    transferPrefix = 'MI'
    
    subMenuPoints = [
      {'tmpl':'MemberView','condition':1,'title':'Info','link':'MemberView?accountNb=$request.field("accountNb","")'},
      {'tmpl':'LedgerTemplate','condition':1,'title':'Konto','link':'MemberLedger?account=%s$request.field("accountNb","")' % transferPrefix},
      ]
    
    editTitle1 = 'Mitglieder'
    editTitle2 = 'Mitgliedsdaten ändern'
    
    inputForm = [
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
        'title':"Titel",
        'name':"title",
        'type':"text",
        'size':32
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
        'title':"Geburtsdatum",
        'name':"birthDate",
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
        'size':64
      },
      {
        'title':"Land",
        'name':"countryCode",
        'type':"text",
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
        'name':"comments",
        'type':"noedit",
      },
      {
        'title':"Neuer Kommentar",
        'name':"newComment",
        'type':"textarea",
        'size':2
      },
      {
        'title':"Wiedervorlage am",
        'name':"FollowUpDate",
        'type':"date",
      }
      ]
    
    helpText = ""

    def getAttrs(self, accountNb=''):
        if accountNb:
            records = Member.search(str(accountNb))
            return records[0].allAttrs()
        else:
            return None
