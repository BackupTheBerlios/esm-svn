#
# File:      $URL: svn+ssh://jgottschick@svn.berlios.de/svnroot/repos/esm/Trunk/classes/skel/GlobalState.py $
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

import string

from sqlobject.main import *
from sqlobject.mysql.mysqlconnection import *
from sqlobject.styles import *
from sqlobject.col import *

from Config import dbConnection
from Version import Version
from mx import DateTime
    
class Member(SQLObject):
    '''
        SQLObject for member information
    '''
    
    _connection = dbConnection
    _lazyUpdate = True # update records on demand
    
    accountNb = IntCol(unique=True)
    newAccountNb = IntCol(default=0)
    
    # personal info
    birthDate = DateCol(default= None)
    gender = StringCol(length=1, varchar=False, default = 'm')
    firstName = StringCol(length=64)
    lastName = StringCol(length=64)
    guardianFirstName = StringCol(length=64, default = '')
    guardianLastName = StringCol(length=64, default = '')
    title = StringCol(length=32, default = '')

    # contact info
    addressExtension = StringCol(length=64, default = '')
    street = StringCol(length=64, default = '')
    city = StringCol(length=64, default = '')
    countryCode = StringCol(length=2, varchar=False, default = 'de')
    zipCode = StringCol(length=10, default = '')
    telefonPrivate = StringCol(length=32, default = '')
    telefonOffice = StringCol(length=32, default = '')
    telefonMobile = StringCol(length=32, default = '')
    fax = StringCol(length=32, default = '')
    email = StringCol(length=128, default = '')
        
    # bank account
    bankAccountNb1 = StringCol(length=20, default = '')
    bankCode1 = StringCol(length=10, default = '')
    bankName1 = StringCol(length=32, default = '')
    bankAccountOwner1 = StringCol(length=32, default = '')
    bankAccountNb2 = StringCol(length=20, default = '')
    bankCode2 = StringCol(length=10, default = '')
    bankName2 = StringCol(length=32, default = '')
    bankAccountOwner2 = StringCol(length=32, default = '')
    
    # member fees
    membershipKind1 = StringCol(length=32, default = '')
    membershipFrom1 = DateCol(default= None)
    membershipEndFrom1 = DateCol(default= None)
    membershipPayNextFrom1 = DateCol(default= None)
    membershipKind2 = StringCol(length=32, default = '')
    membershipFrom2 = DateCol(default= None)
    membershipEndFrom2 = DateCol(default= None)
    membershipPayNextFrom2 = DateCol(default= None)
    membershipKind3 = StringCol(length=32, default = '')
    membershipFrom3 = DateCol(default= None)
    membershipEndFrom3 = DateCol(default= None)
    membershipPayNextFrom3 = DateCol(default= None)
    membershipKind4 = StringCol(length=32, default = '')
    membershipFrom4 = DateCol(default= None)
    membershipEndFrom4 = DateCol(default= None)
    membershipPayNextFrom4 = DateCol(default= None)
    membershipKind5 = StringCol(length=32, default = '')
    membershipFrom5 = DateCol(default= None)
    membershipEndFrom5 = DateCol(default= None)
    membershipPayNextFrom5 = DateCol(default= None)
    
    # payments
    payBy = StringCol(length=16, default = '')
    automaticPayFrom = DateCol(default= None)
    invoiceFrom = DateCol(default= None)
    reminderLevel = IntCol(default=0)
    lastReminderAt = DateTimeCol(default= None)
    
    # membership dates
    startFrom = DateCol(default= None)
    endsAt = DateCol(default= None)
    terminationReason = StringCol(length=32, default = '')
    enteredFirstAt = DateTimeCol(default= None)
    comments = StringCol(default = '')
    
    # common for accounts
    followUpDate = DateCol(default= None)
    passwordHash = StringCol(length=32, default = '')
    role = StringCol(length=10, default = '')
    design = StringCol(length=10, default = '')
    
    # common attributes
    errorMessage = StringCol(length=16, default = '')
    changedAt = DateTimeCol(default= DateTime.now())
    changedAtSite = StringCol(length=2, varchar=False, default = '')
    changedBy = StringCol(length=32, default = '')
    
    def search(self, pattern='', context=''):
        pattern = string.replace(string.lower(pattern),'*','%')
        pattern = string.replace(string.lower(pattern),'?','_')
        if pattern:
            if pattern[0] in '0123456789':
                return self.select("account_nb LIKE '%s'" % pattern, orderBy="account_nb")
            else:
                if ',' in pattern:
                    names = string.split(pattern,',')
                    lnPattern = string.strip(names[0])
                    fnPattern = string.strip(names[1])
                    return self.select("last_name LIKE '%s' AND first_name LIKE '%s'" % (lnPattern,fnPattern), orderBy="last_name")
                else:
                    return self.select("last_name LIKE '%s'" % pattern, orderBy="last_name")
        else:
            return self.select(orderBy="account_nb")
            
    search = classmethod(search)
        
    def allAttrs(self):
        attrs = {}
        attrs['accountNb'] = self.accountNb
        attrs['newAccountNb'] = self.newAccountNb
        attrs['firstName'] = self.firstName
        attrs['lastName'] = self.lastName
        attrs['guardianFirstName'] = self.guardianFirstName
        attrs['guardianLastName'] = self.guardianLastName
        attrs['title'] = self.title
        attrs['addressExtension'] = self.addressExtension
        attrs['street'] = self.street
        attrs['city'] = self.city
        attrs['countryCode'] = self.countryCode
        attrs['zipCode'] = self.zipCode
        attrs['telefonPrivate'] = self.telefonPrivate
        attrs['telefonOffice'] = self.telefonOffice
        attrs['telefonMobile'] = self.telefonMobile
        attrs['fax'] = self.fax
        attrs['email'] = self.email
        attrs['birthDate'] = self.birthDate
        attrs['gender'] = self.gender
        attrs['bankAccountNb1'] = self.bankAccountNb1
        attrs['bankCode1'] = self.bankCode1
        attrs['bankName1'] = self.bankName1
        attrs['bankAccountOwner1'] = self.bankAccountOwner1
        attrs['bankAccountNb2'] = self.bankAccountNb2
        attrs['bankCode2'] = self.bankCode2
        attrs['bankName2'] = self.bankName2
        attrs['bankAccountOwner2'] = self.bankAccountOwner2
        attrs['membershipKind1'] = self.membershipKind1
        attrs['membershipFrom1'] = self.membershipFrom1
        attrs['membershipEndFrom1'] = self.membershipEndFrom1
        attrs['membershipPayNextFrom1'] = self.membershipPayNextFrom1
        attrs['membershipKind2'] = self.membershipKind2
        attrs['membershipFrom2'] = self.membershipFrom2
        attrs['membershipEndFrom2'] = self.membershipEndFrom2
        attrs['membershipPayNextFrom2'] = self.membershipPayNextFrom2
        attrs['membershipKind3'] = self.membershipKind3
        attrs['membershipFrom3'] = self.membershipFrom3
        attrs['membershipEndFrom3'] = self.membershipEndFrom3
        attrs['membershipPayNextFrom3'] = self.membershipPayNextFrom3
        attrs['membershipKind4'] = self.membershipKind4
        attrs['membershipFrom4'] = self.membershipFrom4
        attrs['membershipEndFrom4'] = self.membershipEndFrom4
        attrs['membershipPayNextFrom4'] = self.membershipPayNextFrom4
        attrs['membershipKind5'] = self.membershipKind5
        attrs['membershipFrom5'] = self.membershipFrom5
        attrs['membershipEndFrom5'] = self.membershipEndFrom5
        attrs['membershipPayNextFrom5'] = self.membershipPayNextFrom5
        attrs['payBy'] = self.payBy
        attrs['automaticPayFrom'] = self.automaticPayFrom
        attrs['invoiceFrom'] = self.invoiceFrom
        attrs['startFrom'] = self.startFrom
        attrs['endsAt'] = self.endsAt
        attrs['terminationReason'] = self.terminationReason
        attrs['enteredFirstAt'] = self.enteredFirstAt
        attrs['reminderLevel'] = self.reminderLevel
        attrs['lastReminderAt'] = self.lastReminderAt
        attrs['comments'] = self.comments
        attrs['followUpDate'] = self.followUpDate
        
        attrs['passwordHash'] = self.passwordHash
        attrs['role'] = self.role
        attrs['design'] = self.design

        attrs['errorMessage'] = self.errorMessage
        attrs['changedAt'] = self.changedAt
        attrs['changedAtSite'] = self.changedAtSite
        attrs['changedBy'] = self.changedBy
        return attrs

#
# old table and its class is only required if version <= 0
#
try:
    class accountsmi(SQLObject):
    
        _connection = dbConnection
        _fromDatabase = True
        _idName = 'accountsMIId'
        _style = MixedCaseStyle(longID=True)
except:
    pass

def neueMitgliedsNr2Int(s):
    if (s == None) or (s == "") or (s == 0):
        return None
    else:
        return int(s[2:])

def str2Int(s):
    if (s == None) or (s == ""):
        return 0
    else:
        return int(s)
    
#
# Transform and update database if required
#

# which is the actual version
v = Version.selectBy(context='member')
if v.count() == 1:
    versionNb = v[0].versionNb
else:
    versionNb = 0
    Version(context='member',versionNb=0)

# transform database to SQLObject format
if versionNb <= 0:
    Member.createTable(ifNotExists=True)
    if isinstance(dbConnection,MySQLConnection):
        dbConnection.query('ALTER TABLE %s.`member` TYPE = MYISAM;' % dbConnection.db)
    for x in accountsmi.select():
        Member(
            accountNb=int(x.mitgliedsNr),
            newAccountNb=neueMitgliedsNr2Int(x.neueMitgliedsNr),
            firstName=x.vorname,
            lastName=x.nachname,
            title=x.titel,
            addressExtension=x.adresszusatz,
            street=x.strasse,
            city=x.ort,
            countryCode=x.countrycode,
            zipCode=x.pLZ,
            telefonPrivate=x.telefonPrivat,
            telefonOffice=x.telefonDienst,
            telefonMobile=x.mobiltelefon,
            fax=x.fAX,
            email=x.eMail,
            birthDate=x.geburtsdatum,
            gender=x.geschlecht,
            bankAccountNb1=x.kontoNr1,
            bankCode1=x.bLZ1,
            bankName1=x.bank1,
            bankAccountOwner1=x.kontoinhaber1,
            bankAccountNb2=x.kontoNr2,
            bankCode2=x.bLZ2,
            bankName2=x.bank2,
            bankAccountOwner2=x.kontoinhaber2,
            membershipKind1=x.beitragsart1,
            membershipFrom1=x.beitragsartAb1,
            membershipEndFrom1=x.beitragsartFreiAb1,
            membershipPayNextFrom1=x.beitragsartErhebungAb1,
            membershipKind2=x.beitragsart2,
            membershipFrom2=x.beitragsartAb2,
            membershipEndFrom2=x.beitragsartFreiAb2,
            membershipPayNextFrom2=x.beitragsartErhebungAb2,
            membershipKind3=x.beitragsart3,
            membershipFrom3=x.beitragsartAb3,
            membershipEndFrom3=x.beitragsartFreiAb3,
            membershipPayNextFrom3=x.beitragsartErhebungAb3,
            membershipKind4=x.beitragsart4,
            membershipFrom4=x.beitragsartAb4,
            membershipEndFrom4=x.beitragsartFreiAb4,
            membershipPayNextFrom4=x.beitragsartErhebungAb4,
            membershipKind5=x.beitragsart5,
            membershipFrom5=x.beitragsartAb5,
            membershipEndFrom5=x.beitragsartFreiAb5,
            membershipPayNextFrom5=x.beitragsartErhebungAb5,
            payBy=x.zahlungsart,
            automaticPayFrom=x.lastschriftAb,
            invoiceFrom=x.rechnungAb,
            startFrom=x.eintrittsdatum,
            endsAt=x.austrittsdatum,
            terminationReason=x.austrittsgrund,
            enteredFirstAt=x.ersteingabeAm,
            reminderLevel=str2Int(x.mahnstufe),
            lastReminderAt=x.letzteMahnungAm,
            comments=x.kommentare,

            errorMessage=x.fehlercode,
            changedAt=x.changedAt,
            changedAtSite=x.changedOn,
            changedBy=x.changedBy
        )

# store actual version number
versionNb = 1
v = Version.selectBy(context='member')
v[0].versionNb = versionNb
