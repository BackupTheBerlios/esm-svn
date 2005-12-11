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

from DownloadTemplate import DownloadTemplate
from mx import DateTime
import tempfile
import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

class PDFDownload(DownloadTemplate):

  contentType = 'application/pdf'
  title = "title"
  pageinfo = "pageinfo"

  def __init__(self, *args, **KWs):
    DownloadTemplate.__init__(self, *args, **KWs)
    styles = getSampleStyleSheet()
    self.styleN = styles["Normal"]
    self.styleH1 = styles["Heading1"]
    self.styleH2 = styles["Heading2"]
    self.styleH3 = styles["Heading3"]

  def myFirstPage(self,canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',7)
    canvas.drawString(inch, 0.75 * inch, "Seite %d / %s" % (doc.page,self.pageinfo))
    canvas.restoreState()

  def myLaterPages(self,canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',7)
    canvas.drawString(inch, 0.75 * inch, "Seite %d / %s" % (doc.page,self.pageinfo))
    canvas.restoreState()

  def buildStory(self,story):
    return story

  def writeContent(self):
    fn = tempfile.mktemp('.pdf')
    doc = SimpleDocTemplate(fn)
    story = self.buildStory([
      Paragraph(self.title, self.styleH1),
      Spacer(1,0.4*inch),
      ])
    doc.build(story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
    f = open(fn,'r')
    self.write(f.read())
    f.close()
    os.remove(fn)

