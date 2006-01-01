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

import string, Libs.misc
from reportlab.platypus import Paragraph, Spacer, Frame, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from mx import DateTime

ages = {
  0 : [0,6,'0 - 6'],
  7 : [7,14,'7 - 14'],
  15: [15,18,'15 -18'],
  19: [19,20,'19 - 20'],
  21: [21,26,'21 - 26'],
  27: [27,40,'27 - 40'],
  41: [41,50,'41 - 50'],
  51: [51,60,'51 - 60'],
  61: [61,150,'61 -']
}

class PrintAgesStatistics(PDFDownload):

  description = []
  subTitle = ''
  bank = 0

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.title = 'Mitgliederstatistik nach Alter'
    self.pageinfo = "Statistik -- %s" % self.organisation


  def buildStory(self,story):
    accountObjects = self.store.fetchObjectsOfClass('AccountsMI')
    year = self.transaction.session().value('accountYear',DateTime.now().year)
    reportingdate = DateTime.DateTimeFrom(self.transaction.request().field('reportingdate',''))
    story.append(Paragraph('Stichtag %s' % reportingdate.strftime(self.dateFormat), self.styleH3))
    story.append(Spacer(1,0.2*inch))
    stats = {}
    mstats = {}
    wstats = {}
    for x in ages.keys():
      stats[x]=0
      mstats[x]=0
      wstats[x]=0
    for x in accountObjects:
      attrs = x.allAttrs(0)
      if (not attrs['Austrittsdatum'] or (attrs['Austrittsdatum'] > reportingdate)) and (attrs['Eintrittsdatum'] <= reportingdate) and attrs['Geburtsdatum']:
        age = misc.age(attrs['Geburtsdatum'],reportingdate)
        for y in ages.keys():
          if age in range(ages[y][0],ages[y][1]+1):
            stats[y] = stats[y] + 1
            if attrs['Geschlecht'] == 'w':
              wstats[y] = wstats[y] + 1
            else:
              mstats[y] = mstats[y] + 1
    data = [['Altersgruppe','M','W','Anzahl']]
    sum = 0
    msum = 0
    wsum = 0
    k = stats.keys()
    k.sort()
    for x in k:
      data.append([ages[x][2],mstats[x],wstats[x],stats[x]])
      sum = sum + stats[x]
      msum = msum + mstats[x]
      wsum = wsum + wstats[x]
    data.append(['Gesamt',msum,wsum,sum])
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
    return story

