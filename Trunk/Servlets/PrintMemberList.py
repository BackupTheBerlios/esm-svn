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


class PrintMemberList(PDFDownload):

  description = []
  subTitle = ''
  bank = 0

  def __init__(self, *args, **KWs):
    PDFDownload.__init__(self, *args, **KWs)
    self.title = 'Mitgliederliste'
    self.pageinfo = "%s (%s)" % (self.organisation,DateTime.DateTimeFrom('').strftime(self.dateFormat))


  def buildStory(self,story):
    accountObjects = self.store.fetchObjectsOfClass('AccountsMI','ORDER BY Nachname')
    reportingdate = self.transaction.request().field('reportingdate','')
    minAge = self.transaction.request().field('minAge')
    maxAge = self.transaction.request().field('maxAge')
    if minAge:
      minAge = string.atoi(minAge)
    else:
      minAge = 0
    if maxAge:
      maxAge = string.atoi(maxAge)
    else:
      maxAge = 200
    if reportingdate:
      reportingdate = DateTime.DateTimeFrom(reportingdate)
      story.append(Paragraph('Stichtag %s' % reportingdate.strftime(self.dateFormat), self.styleH3))
      story.append(Spacer(1,0.2*inch))
      refDate = reportingdate
    else:
      refDate = DateTime.DateTimeFrom('')
    data = [['MNr','Vorname','Nachname',' ','Alter','Geburtstag','Eintritt','Austritt']]
    for x in accountObjects:
      attrs = x.allAttrs(0)
      age = misc.age(attrs['Geburtsdatum'],refDate)
      if age >= minAge and age <= maxAge:
        if not reportingdate or (reportingdate and (not attrs['Austrittsdatum'] or (attrs['Austrittsdatum'] > reportingdate)) and (attrs['Eintrittsdatum'] <= reportingdate)):
          if attrs['Austrittsdatum']:
            data.append([attrs['MitgliedsNr'],attrs['Vorname'][:15],attrs['Nachname'][:20],attrs['Geschlecht'],age,attrs['Geburtsdatum'].strftime(self.dateFormat),attrs['Eintrittsdatum'].strftime(self.dateFormat),attrs['Austrittsdatum'].strftime(self.dateFormat)])
          else:
            data.append([attrs['MitgliedsNr'],attrs['Vorname'][:15],attrs['Nachname'][:20],attrs['Geschlecht'],age,attrs['Geburtsdatum'].strftime(self.dateFormat),attrs['Eintrittsdatum'].strftime(self.dateFormat),'-'])
    #
    # build table with stylesheet
    #
    t = Table(data,repeatRows=1)
    t.setStyle(TableStyle([
      ('FONTSIZE',(0,1),(-1,-2),9),
      ('TOPPADDING',(0,0),(-1,-1),1),
      ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
      ]))
    story.append(t)
    return story

