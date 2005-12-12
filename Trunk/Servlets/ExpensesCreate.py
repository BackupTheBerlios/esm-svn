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

from SiteContent import SiteContent
from mx import DateTime
from Middle.AccountsAK import AccountsAK
from WebUtils.Funcs import urlEncode
from MySQLdb import OperationalError
import string

true = 1 == 1
false = 1 != 1

ExpensesType = 0
ExpensesRequired = 1
ExpensesFields = {
  'Nr':['string',1],
  'Name':['string',1],
  'Kommentare':['string',0],
  }

ExpensesAttrs = ExpensesFields.keys()
standardAttrs = ['ID','ChangedBy','ChangedAt','ChangedOn','changedBy','changedAt','changedOn']

class ExpensesCreate(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'AccountsAK'

  def writeContent(self, trans=None):
    #
    # this servlet creates Expenses data
    #

    page = self.transaction.request().field('page','Main')
    #
    # create Expenses object
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    ExpensesNr=self.transaction.request().field('Nr','')
    Expenses = AccountsAK()
    #
    # change Expenses object
    #
    for attr in ExpensesAttrs:
      if attr not in standardAttrs:
        if ExpensesFields[attr][ExpensesType] == 'string':
          print self.transaction.request().field(attr,'')
          Expenses.setValueForKey(attr, self.transaction.request().field(attr,''))
        elif ExpensesFields[attr][ExpensesType] == 'float':
          Expenses.setValueForKey(attr, float(string.replace(self.transaction.request().field(attr,'0,0'),',','.')))
        elif (ExpensesFields[attr][ExpensesType] == 'datetime') and self.request.field(attr,''):
          Expenses.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
        elif (ExpensesFields[attr][ExpensesType] == 'date') and self.transaction.request().field(attr,''):
          Expenses.setValueForKey(attr, DateTime.DateTimeFrom(self.transaction.request().field(attr,'')))
    #
    # set standard attributes
    #
    Expenses.setID('AK'+ExpensesNr)
    Expenses.setErsteingabeAm(DateTime.now())
    Expenses.setChangedBy(self.transaction.session().value('authenticated_user',''))
    Expenses.setChangedAt(DateTime.now())
    Expenses.setChangedOn(self.getSite())
    #
    # store Expenses in database
    #
    store.addObject(Expenses)
    try:
      store.saveChanges()
      #
      # back to Expenses page
      #
      self.transaction.response().sendRedirect('ExpensesView?index=' + ExpensesNr)
    except OperationalError,x:
      store.discardEverything()
      errorCode,errorText = x
      #
      # back to error page
      #
      self.transaction.response().sendRedirect('Error?problem=Daten+konnten+nicht+gespeichert+werden!&reason=' + urlEncode(str(errorText)))
