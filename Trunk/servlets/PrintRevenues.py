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

from PDFDownload import PDFDownload

import string
from reportlab.platypus import Paragraph, Spacer, Frame, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from mx import DateTime

class PrintRevenues(PDFDownload):

  description = []
  subTitle = ''
  bank = 0
  groups = []
  revenueAccountPrefix = ''

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.title = 'Übersicht %s' % self.subTitle
    self.pageinfo = "Währung bis 31.12.2001 in DM und ab dem 01.01.2002 in Euro -- %s" % self.organisation

  def accountSum(self,account,transferObjects):
    saldo = 0.0
    #
    # add Transfers
    #
    for x in transferObjects:
      attrs = x.allAttrs(0)
      soll = attrs['Soll']
      haben = attrs['Haben']
      if (attrs['Konto1'] == account) and (attrs['Konto2'][:len(self.revenueAccountPrefix)] == self.revenueAccountPrefix):
        if self.bank:
          saldo = saldo + soll
        else:
          saldo = saldo + haben
      elif (attrs['Konto2'] == account) and (attrs['Konto1'][:len(self.revenueAccountPrefix)] == self.revenueAccountPrefix):
        if self.bank:
          saldo = saldo + haben
        else:
          saldo = saldo + soll
    return saldo
  
  def buildStory(self,story):
    year = self.transaction.session().value('accountYear',DateTime.now().year)
    accounts = self.transaction.request().field('accounts','')
    allTransferObjects = self.store.fetchObjectsOfClass('Transfers','WHERE (Jahr="%s") ORDER BY Datum,Who' % (year))
    transferObjects = {}
    for x in allTransferObjects:
      attrs = x.allAttrs(0)
      if transferObjects.has_key(attrs['Konto1']):
        transferObjects[attrs['Konto1']].append(x)
      else:
        transferObjects[attrs['Konto1']] = [x]
      if transferObjects.has_key(attrs['Konto2']):
        transferObjects[attrs['Konto2']].append(x)
      else:
        transferObjects[attrs['Konto2']] = [x]
    p = string.split(accounts)
    if self.groups:
      patternset = []
      for x in self.groups:
        prefix = x[0]
        lenPrefix = len(prefix)
        pattern = []
        for y in p:
          if y[:lenPrefix] == prefix:
            pattern.append(y)
        patternset.append([x[1],pattern])
    else:
      patternset = [['',p]]
    total = 0.0
    print patternset
    for pattern in patternset:
      if pattern[0]:
        story.append(Paragraph('%s' % pattern[0], self.styleH2))
        story.append(Spacer(1,0.2*inch))
      data = [['Konto','Beschreibung','1.1.%s - 31.12.%s' % (year,year)]]
      subtotal = 0.0
      for x in pattern[1]:
        if '*' in x:
          accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'ORDER BY ID')
          for y in accountObjects:
            attrs = y.allAttrs(0)
            account = attrs['ID']
            if transferObjects.has_key(account):
              sum = self.accountSum(account,transferObjects[account])
              if self.description:
                description = attrs[self.description[0]]
                for x in self.description[1:]:
                  if attrs.has_key(x):
                    description = description + attrs[x]
                  else:
                    description = description + x
              data.append([attrs['ID'],description,string.replace('%5.2f' % sum,'.',',')])
              subtotal = subtotal + sum
              total = total + sum
        else:
          account = x
          if transferObjects.has_key(account):
            accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'WHERE ID="%s"' % x)
            attrs = accountObjects[0].allAttrs(0)
            sum = self.accountSum(account,transferObjects[account])
            if self.description:
              description = attrs[self.description[0]]
              for x in self.description[1:]:
                description = description + ', ' + attrs[x]
            data.append([attrs['ID'],description,string.replace('%5.2f' % sum,'.',',')])
            subtotal = subtotal + sum
            total = total + sum
      data.append([' ','Summe',string.replace('%5.2f' % subtotal,'.',',')])
      #
      # build table with stylesheet
      #
      t = Table(data,repeatRows=1)
      t.setStyle(TableStyle([
        ('FONTSIZE',(0,1),(-1,-2),9),
        ('TOPPADDING',(0,0),(-1,-1),1),
        ('BOTTOMPADDING',(0,0),(-1,-1),1),
        ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
        ('LINEABOVE',(0,-1),(-1,-1),0.25,colors.black),
        ('ALIGN',(-1,1),(-1,-1),'RIGHT'),
        ('VALIGN',(0,1),(0,-1),'TOP'),
        ]))
      story.append(t)
    if self.groups:
      if total >= 0.0:
        story.append(Paragraph(string.replace('Gewinn von %5.2f' % total,'.',','), self.styleH3))
      else:
        story.append(Paragraph(string.replace('Verlust von %5.2f' % total,'.',','), self.styleH3))
    return story

