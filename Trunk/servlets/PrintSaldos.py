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

class PrintSaldos(PDFDownload):

  description = []
  subTitle = ''
  bank = 0

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.title = '%s' % self.subTitle
    self.pageinfo = "Währung bis 31.12.2001 in DM und ab dem 31.12.2001 in Euro -- %s" % self.organisation

  def accountLine(self,account,accountInfos,transferObjects,year):
    thisYear = 0.0
    nextYear = 0.0
    #
    # add Transfers
    #
    for x in transferObjects:
      attrs = x.allAttrs(0)
      if attrs['Konto1'] == account:
        soll = attrs['Soll']
        haben = attrs['Haben']
      elif attrs['Konto2'] == account:
        soll = attrs['Haben']
        haben = attrs['Soll']
      else:
        soll = 0.0
        haben = 0.0
      if attrs['Jahr'] == year:
        thisYear = thisYear + haben - soll
      else:
        nextYear = nextYear + haben - soll
    text = ''
    for part in self.description:
      if accountInfos.has_key(part):
        if text:
          text = text + accountInfos[part]
        else:
          text = accountInfos[part]
      else:
        if text:
          text = text + part
        else:
          text = part
    if ('%0.1f' % thisYear) in ['0.0','-0.0']:
      thisYear = 0.0
    if ('%0.1f' % nextYear) in ['0.0','-0.0']:
      nextYear = 0.0
    if thisYear or nextYear:
      return (text,thisYear,nextYear)

  def buildStory(self,story):
    year = self.transaction.session().value('accountYear',DateTime.now().year)
    thisYear = 0.0
    nextYear = 0.0
    data = [['Beschreibung','31.12.%d' % (year-1),'31.12.%d' % year]]
    accounts = self.transaction.request().field('accounts','')
    pattern = string.split(accounts)
    allTransferObjects = self.store.fetchObjectsOfClass('Transfers','WHERE (Jahr="%s" OR Jahr="%s") AND (BKZ="SVS" OR BKZ="SVH") ORDER BY Datum,Who' % (year,year+1))
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
    for x in pattern:
      if '*' in x:
        accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'ORDER BY ID')
        for y in accountObjects:
          attrs = y.allAttrs(0)
          account = attrs['ID']
          if transferObjects.has_key(account):
            line = self.accountLine(account,attrs,transferObjects[account],year)
            if line:
              if line[1] and not line[2]:
                thisYear = thisYear + line[1]
                data.append([line[0],string.replace('%5.2f' % line[1],'.',','),' '])
              elif not line[1] and line[2]:
                nextYear = nextYear + line[2]
                data.append([line[0],' ',string.replace('%5.2f' % line[2],'.',',')])
              elif line[1] and line[2]:
                thisYear = thisYear + line[1]
                nextYear = nextYear + line[2]
                data.append([line[0],string.replace('%5.2f' % line[1],'.',','),string.replace('%5.2f' % line[2],'.',',')])
      else:
        account = x
        if transferObjects.has_key(account):
          accountObjects = self.store.fetchObjectsOfClass('Accounts'+x[:2],'WHERE ID="%s"' % x)
          attrs = accountObjects[0].allAttrs(0)
          line = self.accountLine(account,transferObjects[account],year)
          if line:
            if line[1] and not line[2]:
              thisYear = thisYear + line[1]
              data.append([line[0],string.replace('%5.2f' % line[1],'.',','),' '])
            elif not line[1] and line[2]:
              nextYear = nextYear + line[2]
              data.append([line[0],' ',string.replace('%5.2f' % line[2],'.',',')])
            elif line[1] and line[2]:
              thisYear = thisYear + line[1]
              nextYear = nextYear + line[2]
              data.append([line[0],string.replace('%5.2f' % line[1],'.',','),string.replace('%5.2f' % line[2],'.',',')])
    data.append([' ',string.replace('%5.2f' % thisYear,'.',','),string.replace('%5.2f' % nextYear,'.',',')])
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
      ('ALIGN',(-2,1),(-1,-1),'RIGHT'),
      ]))
    story.append(t)
    return story

