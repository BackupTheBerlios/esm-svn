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

class PrintSummary(PDFDownload):

  description = []
  subTitle = ''
  groups = []
  isSaldoSummary = 0
  excludeBKZ = []

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.title = 'Übersicht %s' % self.subTitle
    self.pageinfo = "Währung bis 31.12.2001 in DM und ab dem 01.01.2002 in Euro -- %s" % self.organisation

  def accountSum(self,account,transferObjects):
    saldo = 0.0
    gvsaldo = 0.0
    #
    # add Transfers
    #
    for x in transferObjects:
      attrs = x.allAttrs(0)
      soll = attrs['Soll']
      haben = attrs['Haben']
      if attrs['BKZ'] not in self.excludeBKZ:
        if attrs['Konto1'] == account:
          saldo = saldo + haben - soll
	  if attrs['BKZ'] not in ['SVS','SVH']:
            gvsaldo = gvsaldo + haben - soll
        elif attrs['Konto2'] == account:
          saldo = saldo - haben + soll
	  if attrs['BKZ'] not in ['SVS','SVH']:
            gvsaldo = gvsaldo - haben + soll
    return saldo,gvsaldo

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
      if attrs['Konto1'] != attrs['Konto2']:
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
    gvtotal = 0.0
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
              sum,gvsum = self.accountSum(account,transferObjects[account])
              if ('%0.2f' % sum) not in ['0.00','-0.00']:
                if attrs.has_key('Nr'):
                  nr = attrs['Nr']
                elif attrs.has_key('MitgliedsNr'):
                  nr = attrs['MitgliedsNr']
                elif attrs.has_key('VendorNr'):
                  nr = attrs['VendorNr']
                elif attrs.has_key('BankNr'):
                  nr = attrs['BankNr']
                if attrs.has_key('Name'):
                  name = attrs['Name']
                elif attrs.has_key('Firma') and attrs['Firma']:
                  name = attrs['Firma']
                elif attrs.has_key('Vorname'):
                  name = '%s, %s' % (attrs['Nachname'],attrs['Vorname'])
                elif attrs.has_key('Bank'):
                  name = attrs['Bank']
                data.append([nr,name,string.replace('%5.2f' % sum,'.',',')])
                subtotal = subtotal + sum
                total = total + sum
              gvtotal = gvtotal + gvsum
        else:
          account = x
          if transferObjects.has_key(account):
            accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'WHERE ID="%s"' % x)
            attrs = accountObjects[0].allAttrs(0)
            sum,gvsum = self.accountSum(account,transferObjects[account])
            if ('%0.2f' % sum) not in ['0.00','-0.00']:
              if attrs.has_key('Nr'):
                nr = attrs['Nr']
              elif attrs.has_key('MitgliedsNr'):
                nr = attrs['MitgliedsNr']
              elif attrs.has_key('VendorNr'):
                nr = attrs['VendorNr']
              elif attrs.has_key('BankNr'):
                nr = attrs['BankNr']
              if attrs.has_key('Name'):
                name = attrs['Name']
              elif attrs.has_key('Firma') and attrs['Firma']:
                name = attrs['Firma']
              elif attrs.has_key('Vorname'):
                name = '%s, %s' % (attrs['Nachname'],attrs['Vorname'])
              elif attrs.has_key('Bank'):
                name = attrs['Bank']
              data.append([nr,name,string.replace('%5.2f' % sum,'.',',')])
              subtotal = subtotal + sum
              total = total + sum
            gvtotal = gvtotal + gvsum
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
        ]))
      story.append(t)
    if self.groups:
      if self.isSaldoSummary:
        if gvtotal >= 0.0:
          story.append(Paragraph(string.replace('Verlust von %5.2f' % gvtotal,'.',','), self.styleH3))
        else:
          story.append(Paragraph(string.replace('Gewinn von %5.2f' % (-1.0 * gvtotal),'.',','), self.styleH3))
        if total >= 0.0:
          story.append(Paragraph(string.replace('Schulden von %5.2f' % total,'.',','), self.styleH3))
        else:
          story.append(Paragraph(string.replace('Vermögen von %5.2f' % (-1.0 * total),'.',','), self.styleH3))
      else:
        if total >= 0.0:
          story.append(Paragraph(string.replace('Gewinn von %5.2f' % total,'.',','), self.styleH3))
        else:
          story.append(Paragraph(string.replace('Verlust von %5.2f' % (-1.0 * total),'.',','), self.styleH3))
    return story

