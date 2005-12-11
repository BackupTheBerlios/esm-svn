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

class MemberCsvDownload(DownloadTemplate):

  contentType = 'text/saveit'
  tableStore = 'AccountsMI'
  headline = ''
  fields = []

  def writeContent(self):
    now = DateTime.now()
    if self.tableStore != '':
      if self.headline:
        self.write('%s\n' % self.headline)
      #
      # read objects from database
      #
      storeObjects = self.store.fetchObjectsOfClass(self.tableStore,'WHERE ID LIKE "%0"')
      for entry in storeObjects:
        attrs = entry.allAttrs(0)
        ein = DateTime.DateTimeFrom(attrs['Eintrittsdatum'])
        if attrs['Austrittsdatum']:
          aus = DateTime.DateTimeFrom(attrs['Austrittsdatum'])
        else:
          aus = None
        content = ''
        for x in self.fields:
          if content:
            content = content + ',' + attrs[x]
          else:
            content = attrs[x]
        if ((aus and ein <= now <= aus) or (not aus and (ein <= now))) and content:
          self.write('%s\n' % content)
