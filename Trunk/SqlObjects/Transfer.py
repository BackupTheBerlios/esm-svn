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
from sqlobject.col import *
from sqlobject.styles import *
from sqlobject.mysql.mysqlconnection import *

from Libs.Config import dbConnection
from SqlObjects.Version import Version
from mx import DateTime

class Transfer(SQLObject):
    '''
        SQLObject for the bank codes database
    '''
    
    _connection = dbConnection
    
    bookingId = StringCol(length=20)
    transferId = StringCol(length=20)
    transferCode = StringCol(length=10)
    debit = CurrencyCol(default=0.0)
    credit = CurrencyCol(default=0.0)
    bookingDate = DateTimeCol()
    receiptDate = DateTimeCol()
    year = IntCol()
    importDescription = StringCol(length=100, default='')
    description = StringCol(length=100, default='')
    importWho = StringCol(length=32)
    who = StringCol(length=32)
    account1 = StringCol(length=10)
    account2 = StringCol(length=10)
    
    changedAt = DateTimeCol(default= DateTime.now())
    changedAtSite = StringCol(length=2, varchar=False, default = '  ')
    changedBy = StringCol(length=32, default = '')
    
    def search(self, pattern='', context=''):
        pattern = string.replace(string.lower(pattern),'*','%')
        pattern = string.replace(string.lower(pattern),'?','_')
        if pattern:
            if pattern[0] in '0123456789':
                return self.select("transfer_code LIKE '%s'" % pattern, orderBy = 'bookingDate')
            else:
                return self.select("description LIKE '%s'" % pattern, orderBy = 'bookingDate')
        else:
            return self.select(orderBy = 'bookingDate')
            
    search = classmethod(search)
    
    def searchForAccount(self, year, account=''):
        account = string.replace(account,'*','%')
        account = string.replace(account,'?','_')
        if account:
            return self.select('(account1="%s" OR account2="%s") AND year="%s"' % (account,account,year), orderBy = 'bookingDate')
        else:
            return self.select(orderBy = 'bookingDate')
            
    searchForAccount = classmethod(searchForAccount)
        
    def allAttrs(self):
        attrs = {}
        attrs['bookingId'] = self.bookingId
        attrs['transferId'] = self.transferId
        attrs['transferCode'] = self.transferCode
        attrs['debit'] = self.debit
        attrs['credit'] = self.credit
        attrs['bookingDate'] = self.bookingDate
        attrs['receiptDate'] = self.receiptDate
        attrs['year'] = self.year
        attrs['importDescription'] = self.importDescription
        attrs['description'] = self.description
        attrs['importWho'] = self.importWho
        attrs['who'] = self.who
        attrs['account1'] = self.account1
        attrs['account2'] = self.account2

        attrs['changedAt'] = self.changedAt
        attrs['changedAtSite'] = self.changedAtSite
        attrs['changedBy'] = self.changedBy
        return attrs    

#
# old table and its class is only required if version <= 0
#
try:
    class transfers(SQLObject):
        '''
            SQLObject for the MiddleKit database format
        '''
    
        _connection = dbConnection
        _fromDatabase = True
        _idName = 'transfersId'
        _style = MixedCaseStyle(longID=True)
except:
    pass

#
# Transform and update database if required
#

# which is the actual version
v = Version.selectBy(context='transfer')
if v.count() == 1:
    versionNb = v[0].versionNb
else:
    versionNb = 0
    Version(context='transfer',versionNb=0)

# transform database to SQLObject format
if versionNb <= 0:
    Transfer.createTable(ifNotExists=True)
    if isinstance(dbConnection,MySQLConnection):
        dbConnection.query('ALTER TABLE %s.`transfer` TYPE = MYISAM;' % dbConnection.db)
    for x in transfers.select():
        Transfer(
            bookingId=x.tAID,
            transferId=x.transferID,
            transferCode=x.bKZ,
            debit=x.soll,
            credit=x.haben,
            bookingDate=x.datum,
            receiptDate=x.datum,
            year=x.jahr,
            importDescription=x.importBeschreibung,
            description=x.beschreibung,
            importWho=x.importWho,
            who=x.who,
            account1=x.konto1,
            account2=x.konto2,

            changedAt=x.changedAt,
            changedAtSite=x.changedOn,
            changedBy=x.changedBy)

# store actual version number
versionNb = 1
v = Version.selectBy(context='transfer')
v[0].versionNb = versionNb
