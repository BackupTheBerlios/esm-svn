#
# File:      $URL$
# Version:   $Rev$
# Changed:   $Date$
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
__revision__ = "$Rev$"[6:-2]

from Change import Change
from Member import Member

from mx import DateTime
import string

nbOfMemberships = 5

class MemberChange(Change):

  def updateMemberFields(self,member):
    member.accountNb = self.getIntegerField('accountNb',member.accountNb)
    member.newAccountNb = self.getIntegerField('newAccountNb',member.newAccountNb)
    member.firstName = self.getStringField('firstName',member.firstName)
    member.lastName = self.getStringField('lastName',member.lastName)
    member.guardianFirstName = self.getStringField('guardianFirstName',member.guardianFirstName)
    member.guardianLastName = self.getStringField('guardianLastName',member.guardianLastName)
    member.title = self.getStringField('title',member.title)
    member.addressExtension = self.getStringField('addressExtension',member.addressExtension)
    member.street = self.getStringField('street',member.street)
    member.city = self.getStringField('city',member.city)
    member.countryCode = self.getStringField('countryCode',member.countryCode)
    member.zipCode = self.getStringField('zipCode',member.zipCode)
    member.telefonPrivate = self.getStringField('telefonPrivate',member.telefonPrivate)
    member.telefonOffice = self.getStringField('telefonOffice',member.telefonOffice)
    member.telefonMobile = self.getStringField('telefonMobile',member.telefonMobile)
    member.fax = self.getStringField('fax',member.fax)
    member.email = self.getStringField('email',member.email)
    member.birthDate = self.getDateField('birthDate',member.birthDate)
    member.gender = self.getStringField('gender',member.gender)
    member.bankAccountNb1 = self.getStringField('bankAccountNb1',member.bankAccountNb1)
    member.bankCode1 = self.getStringField('bankCode1',member.bankCode1)
    member.bankName1 = self.getStringField('bankName1',member.bankName1)
    member.bankAccountOwner1 = self.getStringField('bankAccountOwner1',member.bankAccountOwner1)
    member.bankAccountNb2 = self.getStringField('bankAccountNb2',member.bankAccountNb2)
    member.bankCode2 = self.getStringField('bankCode2',member.bankCode2)
    member.bankName2 = self.getStringField('bankName2',member.bankName2)
    member.bankAccountOwner2 = self.getStringField('bankAccountOwner2',member.bankAccountOwner2)
    member.membershipKind1 = self.getStringField('membershipKind1',member.membershipKind1)
    member.membershipFrom1 = self.getDateField('membershipFrom1',member.membershipFrom1)
    member.membershipEndFrom1 = self.getDateField('membershipEndFrom1',member.membershipEndFrom1)
    member.membershipPayNextFrom1 = self.getDateField('membershipPayNextFrom1',member.membershipPayNextFrom1)
    member.membershipKind2 = self.getStringField('membershipKind2',member.membershipKind2)
    member.membershipFrom2 = self.getDateField('membershipFrom2',member.membershipFrom2)
    member.membershipEndFrom2 = self.getDateField('membershipEndFrom2',member.membershipEndFrom2)
    member.membershipPayNextFrom2 = self.getDateField('membershipPayNextFrom2',member.membershipPayNextFrom2)
    member.membershipKind3 = self.getStringField('membershipKind3',member.membershipKind3)
    member.membershipFrom3 = self.getDateField('membershipFrom3',member.membershipFrom3)
    member.membershipEndFrom3 = self.getDateField('membershipEndFrom3',member.membershipEndFrom3)
    member.membershipPayNextFrom3 = self.getDateField('membershipPayNextFrom3',member.membershipPayNextFrom3)
    member.membershipKind4 = self.getStringField('membershipKind4',member.membershipKind4)
    member.membershipFrom4 = self.getDateField('membershipFrom4',member.membershipFrom4)
    member.membershipEndFrom4 = self.getDateField('membershipEndFrom4',member.membershipEndFrom4)
    member.membershipPayNextFrom4 = self.getDateField('membershipPayNextFrom4',member.membershipPayNextFrom4)
    member.membershipKind5 = self.getStringField('membershipKind5',member.membershipKind5)
    member.membershipFrom5 = self.getDateField('membershipFrom5',member.membershipFrom5)
    member.membershipEndFrom5 = self.getDateField('membershipEndFrom5',member.membershipEndFrom5)
    member.membershipPayNextFrom5 = self.getDateField('membershipPayNextFrom5',member.membershipPayNextFrom5)
    member.payBy = self.getStringField('payBy',member.payBy)
    member.automaticPayFrom = self.getDateField('automaticPayFrom',member.automaticPayFrom)
    member.invoiceFrom = self.getDateField('invoiceFrom',member.invoiceFrom)
    member.startFrom = self.getDateField('startFrom',member.startFrom)
    member.endsAt = self.getDateField('endsAt',member.endsAt)
    member.terminationReason = self.getStringField('terminationReason',member.terminationReason)
    member.enteredFirstAt = self.getDateField('enteredFirstAt',member.enteredFirstAt)
    member.reminderLevel = self.getIntegerField('reminderLevel',member.reminderLevel)
    member.lastReminderAt = self.getDateField('lastReminderAt',member.lastReminderAt)
    # new comments will be added to the beginning
    if self.getStringField('newComment'):
        member.comments = '%s (%s %s) // %s' % (self.getStringField('newComment'),
            self.transaction.session().value('authenticated_user',''),
            DateTime.now().strftime('%d.%m.%Y'),self.getStringField('comments',member.comments))
    else:
        member.comments = self.getStringField('comments',member.comments)
    member.followUpDate = self.getDateField('followUpDate',member.followUpDate)
    member.passwordHash = self.getStringField('passwordHash',member.passwordHash)
    member.role = self.getStringField('role',member.role)
    member.design = self.getStringField('design',member.design)
        
  def getMemberships(self, member):
    ms = {}
    ms['membershipKind1'] = member.membershipKind1
    ms['membershipFrom1'] = member.membershipFrom1
    ms['membershipEndFrom1'] = member.membershipEndFrom1
    ms['membershipPayNextFrom1'] = member.membershipPayNextFrom1
    ms['membershipKind2'] = member.membershipKind2
    ms['membershipFrom2'] = member.membershipFrom2
    ms['membershipEndFrom2'] = member.membershipEndFrom2
    ms['membershipPayNextFrom2'] = member.membershipPayNextFrom2
    ms['membershipKind3'] = member.membershipKind3
    ms['membershipFrom3'] = member.membershipFrom3
    ms['membershipEndFrom3'] = member.membershipEndFrom3
    ms['membershipPayNextFrom3'] = member.membershipPayNextFrom3
    ms['membershipKind4'] = member.membershipKind4
    ms['membershipFrom4'] = member.membershipFrom4
    ms['membershipEndFrom4'] = member.membershipEndFrom4
    ms['membershipPayNextFrom4'] = member.membershipPayNextFrom4
    ms['membershipKind5'] = member.membershipKind5
    ms['membershipFrom5'] = member.membershipFrom5
    ms['membershipEndFrom5'] = member.membershipEndFrom5
    ms['membershipPayNextFrom5'] = member.membershipPayNextFrom5
    return ms
    
  def updateMemberships(self,member,ms):
    member.membershipKind1 = ms['membershipKind1']
    member.membershipFrom1 = ms['membershipFrom1']
    member.membershipEndFrom1 = ms['membershipEndFrom1'] 
    member.membershipPayNextFrom1 = ms['membershipPayNextFrom1'] 
    member.membershipKind2 = ms['membershipKind2'] 
    member.membershipFrom2 = ms['membershipFrom2'] 
    member.membershipEndFrom2 = ms['membershipEndFrom2'] 
    member.membershipPayNextFrom2 = ms['membershipPayNextFrom2'] 
    member.membershipKind3 = ms['membershipKind3'] 
    member.membershipFrom3 = ms['membershipFrom3'] 
    member.membershipEndFrom3 = ms['membershipEndFrom3'] 
    member.membershipPayNextFrom3 = ms['membershipPayNextFrom3'] 
    member.membershipKind4 = ms['membershipKind4'] 
    member.membershipFrom4 = ms['membershipFrom4'] 
    member.membershipEndFrom4 = ms['membershipEndFrom4'] 
    member.membershipPayNextFrom4 = ms['membershipPayNextFrom4'] 
    member.membershipKind5 = ms['membershipKind5'] 
    member.membershipFrom5 = ms['membershipFrom5'] 
    member.membershipEndFrom5 = ms['membershipEndFrom5'] 

  def writeContent(self, trans=None):
    '''
      this servlet changes member record
    '''

    # retrieving the required parameters
    accountNb = int(self.transaction.request().field('accountNb','0'))
    print "nb: %s" % accountNb
    firstName = self.transaction.request().field('firstName','')
    print "fn: %s" % firstName
    lastName = self.transaction.request().field('lastName','')
    if not accountNb:
        print "no accountNb"
    if not firstName:
        print "no firstname"
    if not lastName:
        print "no lastname"

    # if it is a new account, create a new record
    storeObjects = Member.search(str(accountNb))
    if storeObjects.count() == 0:
        print "create new member"
        member = Member(accountNb=accountNb,firstName=firstName,lastName=lastName)
        member.sync()

    # calculating and setting the dates for "membershipEndFrom"
    membershipKind = string.strip(self.transaction.request().field('membershipKind',''))
    membershipFrom = string.strip(self.transaction.request().field('membershipFrom',''))
    membershipEndFrom = string.strip(self.transaction.request().field('membershipEndFrom',''))
    endsAt = string.strip(self.transaction.request().field('endsAt',''))

    # if membershipEndFrom or membershipFrom are not set, they are equal
    if (not membershipEndFrom) and (membershipFrom):
        membershipEndFrom = membershipFrom
    if (membershipEndFrom) and (not membershipFrom):
        membershipFrom = membershipEndFrom
    if (endsAt) and (not membershipEndFrom):
        y =  DateTime.DateTimeFrom(endsAt)+DateTime.DateTimeDelta(1)
        membershipEndFrom = y.date
        
    # retrieve accountNb's of all family members
    accounts = []
    accountObjects = Member.search("%s_" % str(accountNb)[:-1])
    for x in accountObjects:
        accounts.append(x.accountNb)
        
    #
    # Update all records of the family
    #
    for record in accounts:
        errors = ''
        storeObjects = Member.search(str(record))
        member = storeObjects[0]
        # if austrittsdatum and not member.Austrittsdatum():
        #     member.setAustrittsdatum(DateTime.DateTimeFrom(austrittsdatum))
        #     member.setAustrittsgrund(string.strip(self.transaction.request().field('Austrittsgrund','')))
        
        #
        # personal part of the record is only updated for the target member
        #
        if record == accountNb:
            #
            # change member object
            #
            self.updateMemberFields(member)
            
        #
        # membership status is only maintained for the main member of a family
        #
        if str(record)[-1:] == "0":
            ms = self.getMemberships(member)
            membershipNb = 0
            if membershipEndFrom != '':
                for x in range(1,nbOfMemberships+1):
                    if (ms['membershipKind'+str(x)]) and (not ms['membershipEndFrom'+str(x)]):
                        ms['membershipEndFrom'+str(x)] = DateTime.DateTimeFrom(membershipEndFrom)
                        #
                        # fees with equal membershipFrom and membershipEndFrom could be overwritten
                        #
                        if ms['membershipFrom'+str(x)] == DateTime.DateTimeFrom(membershipEndFrom):
                            membershipNb = x - 1
                        else:
                            membershipNb = x
            elif membershipFrom:
                for x in range(1,nbOfMemberships+1):
                    if (not ms['membershipKind'+str(x)]) and (membershipNb == 0):
                        membershipNb = x - 1
            #
            # set new fee in the next free slot (2-5 and 1) respective slot 1, if no fee already exists
            #
            if membershipKind:
                ms['membershipKind'+str(membershipNb % nbOfMemberships + 1)] = membershipKind
                ms['membershipFrom'+str(membershipNb % nbOfMemberships + 1)] = DateTime.DateTimeFrom(membershipFrom)
                ms['membershipEndFrom'+str(membershipNb % nbOfMemberships + 1)] = None
                ms['membershipPayNextFrom'+str(membershipNb % nbOfMemberships + 1)] = DateTime.DateTimeFrom(membershipFrom)
                ms['membershipKind'+str((membershipNb + 1) % nbOfMemberships + 1)] = ""
                ms['membershipFrom'+str((membershipNb + 1) % nbOfMemberships + 1)] = None
                ms['membershipEndFrom'+str((membershipNb + 1) % nbOfMemberships + 1)] = None
                ms['membershipPayNextFrom'+str((membershipNb + 1) % nbOfMemberships + 1)] = None
            self.updateMemberships(member,ms)

        self.updateStandardFields(member,errors)
        #
        # store updates in database
        #
        member.sync()
        
    #
    # back to member page
    #
    self.transaction.response().sendRedirect('MemberView?accountNb=' + str(accountNb))
