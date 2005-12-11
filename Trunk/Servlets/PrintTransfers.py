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

class PrintTransfers(PDFDownload):

  description = []
  subTitle = ''
  bank = 0

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.title = 'Kontoauszug %s' % self.subTitle
    self.pageinfo = "Währung bis 31.12.2001 in DM und ab dem 01.01.2002 in Euro -- %s" % self.organisation

  def accountTable(self,account,transferObjects,year):
    #
    # table title
    #
    if self.bank:
      data = [['Datum','Konto','Beschreibung','Verwendungszweck','Haben','Soll','Saldo']]
    else:
      data = [['Datum','Konto','Beschreibung','Verwendungszweck','Soll','Haben','Saldo']]
    #
    saldo = 0.0
    #
    # add Transfers
    #
    for x in transferObjects:
      attrs = x.allAttrs(0)
      if (attrs['Konto1'] == account) and (attrs['Konto2'] == account):
        soll = attrs['Soll']
        haben = attrs['Haben']
        konto = attrs['Konto1']
      elif attrs['Konto1'] == account:
        soll = attrs['Soll']
        haben = attrs['Haben']
        konto = attrs['Konto2']
      else:
        soll = attrs['Haben']
        haben = attrs['Soll']
        konto = attrs['Konto1']
      if self.bank:
        t = haben
        haben = soll
        soll = t
      saldo = saldo + haben - soll
      data.append([
        attrs['Datum'].strftime(self.dateFormat)[:10],
        konto,
        attrs['Who'][:19],
        attrs['Beschreibung'][:19],
        string.replace('%5.2f' % soll,'.',','),
        string.replace('%5.2f' % haben,'.',','),
        string.replace('%5.2f' % saldo,'.',',')
        ])
    data.append([' ',' ','Summe',account,' ',' ',string.replace('%5.2f' % saldo,'.',',')])
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
      ('ALIGN',(0,1),(-4,-1),'LEFT'),
      ('ALIGN',(-3,1),(-1,-1),'RIGHT'),
      ]))
    return t
  
  def buildTitle(self,attrs,keys):
    title = ''
    for x in keys:
      if title and attrs.has_key(x) and attrs[x]:
        title = "%s, %s" % (title,attrs[x])
      elif attrs.has_key(x) and attrs[x]:
        title = attrs[x]
    return title

  def buildStory(self,story):
    year = self.transaction.session().value('accountYear',DateTime.now().year)
    accounts = self.transaction.request().field('accounts','')
    allTransferObjects = self.store.fetchObjectsOfClass('Transfers','WHERE Jahr="%s" ORDER BY Datum,Who' % year)
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
    pattern = string.split(accounts)
    for x in pattern:
      if '*' in x:
        accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'ORDER BY ID')
        for y in accountObjects:
          attrs = y.allAttrs(0)
          account = attrs['ID']
          if transferObjects.has_key(account):
            story.append(Paragraph('%s - %s' % (attrs['ID'],self.buildTitle(attrs,self.description)), self.styleH2))
            story.append(Spacer(1,0.2*inch))
            story.append(self.accountTable(account,transferObjects[account],year))
      else:
        account = x
        if transferObjects.has_key(account):
          accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'WHERE ID="%s"' % x)
          attrs = accountObjects[0].allAttrs(0)
          story.append(Paragraph('%s - %s' % (attrs['ID'],self.buildTitle(attrs,self.description)), self.styleH2))
          story.append(Spacer(1,0.2*inch))
          story.append(self.accountTable(account,transferObjects[account],year))
    return story

