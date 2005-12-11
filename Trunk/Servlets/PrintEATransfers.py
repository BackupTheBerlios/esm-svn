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

class PrintEATransfers(PDFDownload):

  summaryAccounts = []

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.pageinfo = "Währung bis 31.12.2001 in DM und ab dem 01.01.2002 in Euro -- %s" % self.organisation
  
  def accountTable(self,account,transferObjects,year,summaryAccounts = []):
    #
    # table title
    #
    data = [['Datum','Konto','Beschreibung','Verwendungszweck','Betrag']]
    #
    saldo = 0.0
    #
    # add Transfers
    #
    for x in transferObjects:
      attrs = x.allAttrs(0)
      if attrs['Konto1'] == account:
        konto = attrs['Konto2']
        saldo = saldo + attrs['Haben']
        saldo = saldo - attrs['Soll']
        amount = attrs['Haben'] - attrs['Soll']
      else:
        konto = attrs['Konto1']
        saldo = saldo - attrs['Haben']
        saldo = saldo + attrs['Soll']
        amount = attrs['Soll'] - attrs['Haben']
      if account not in summaryAccounts:
        data.append([
          attrs['Datum'].strftime(self.dateFormat)[:10],
          konto,
          attrs['Who'][:30],
          attrs['Beschreibung'][:35],
          string.replace('%5.2f' % amount,'.',',')
          ])
    data.append([' ',' ','Summe',account,string.replace('%5.2f' % saldo,'.',',')])
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
    return t

  def buildStory(self,story):
    year = self.transaction.session().value('accountYear',DateTime.now().year)
    accounts = self.transaction.request().field('accounts','')
    pattern = string.split(accounts)
    for x in pattern:
      if '*' in x:
        accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'ORDER BY ID')
        for y in accountObjects:
          attrs = y.allAttrs(0)
          account = attrs['ID']
          transferObjects = self.store.fetchObjectsOfClass('Transfers','WHERE (Konto1="%s" OR Konto2="%s") AND Jahr="%s" ORDER BY Datum,Who' % (account,account,year))
          if transferObjects:
            story.append(Paragraph('%s - %s' % (attrs['ID'],attrs['Name']), self.styleH2))
            story.append(Spacer(1,0.2*inch))
            story.append(self.accountTable(account,transferObjects,year,self.summaryAccounts))
      else:
        account = x
        transferObjects = self.store.fetchObjectsOfClass('Transfers','WHERE (Konto1="%s" OR Konto2="%s") AND Jahr="%s" ORDER BY Datum,Who' % (account,account,year))
        if transferObjects:
          accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'WHERE ID="%s"' % x)
          attrs = accountObjects[0].allAttrs(0)
          story.append(Paragraph(x, self.styleH2))
          story.append(Spacer(1,0.2*inch))
          story.append(self.accountTable(account,transferObjects,year))
    return story

