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

from SiteBase import SiteBase
from mx import DateTime
from Middle.Transfers import Transfers
from GlobalState import ID,Store
import string
from MiscUtils.Funcs import uniqueId
import os

priceStore = 'Prices'

class DTAUS(SiteBase):

  def __init__(self, *args, **KWs):
    SiteBase.__init__(self, *args, **KWs)
    self.storeName = 'Transfers'
    self.accountStores = {
      'MI':'AccountsMI'
    }

  def respond(self, transaction):
    #
    # get the year for which the new saldos have to be calculated
    #
    try:
      year = int(self.transaction.request().field('date','')[-4:])
    except ValueError:
      self.transaction.response().sendRedirect('Administration')
    else:
      notice = self.transaction.request().field('notice','')
      if notice:
        bemerkung = self.transaction.request().field('date','') + '%s' % notice
      else:
        bemerkung = self.transaction.request().field('date','')
      store = Store.store
      sessionId = self.transaction.session().identifier()
      #
      # generate DTAUS.ctl
      #
      storeObjects = store.fetchObjectsOfClass('IDs','WHERE %s = "%s"' % ('Tablename',self.accountStores['MI']))
      if (len(storeObjects) == 1):
        id = storeObjects[0]
        taid = id.Lastschriften()
        dir = "/tmp/" + sessionId + "/" + DateTime.now().strftime("%Y%m%d")
        os.system("rm -rf " + dir)
        os.makedirs(dir)
        self.response().setHeader("Content-type","application/zip")
        ctl = open(dir + '/DTAUS.ctl','w')
        ctl.write('BEGIN {\n\
  Art   LK\n\
  Name  %s\n\
  Konto %s\n\
  BLZ   %s\n\
  Ausfuehrung %s\n\
  Euro\n\
}\n\n\
' % (self.getOrganisation(),self.getAccount(),self.getBLZ(),DateTime.now().strftime(self.dateFormat)))
        transfers = store.fetchObjectsOfClass(self.storeName,'WHERE TAID="%s" ORDER BY Konto1,Konto2' % taid)
        for x in transfers:
          if x.Konto1()[:2] in self.accountStores.keys():
            account = x.Konto1()
            betrag = x.Haben()
          else:
            account = x.Konto2()
            betrag = x.Soll()
          info = store.fetchObjectsOfClass(self.accountStores[account[:2]],'WHERE ID="%s"' % account)[0]
	  if info.Kontoinhaber1():
	    name = info.Kontoinhaber1()
	  elif info.Kontoinhaber2():
	    name = info.Kontoinhaber2()
	  else:
	    name = '%s, %s' % info.Nachname(),info.Vorname()
          ctl.write('\n\
\n\
{\n\
  Transaktion Einzug\n\
  Name   %s\n\
  Konto  %s\n\
  BLZ    %s\n\
  Betrag %5.2f\n\
  Zweck  %s %s\n\
  Text   %s\n\
}\n\
' % (name,info.KontoNr1(),info.BLZ1(),betrag,account,bemerkung,self.getSupport()))
        ctl.close()
        os.system('cd %s; dtaus -c DTAUS.ctl -d dtaus -b dtaus-begleitzettel.txt -o dtaus-liste.txt -dtaus' % dir)
        os.system('cd %s/..; zip dtaus.zip %s/*' % (dir,DateTime.now().strftime("%Y%m%d")))
        fd = open('%s/../dtaus.zip' % dir, 'r')
        self.write(fd.read())
        fd.close
        os.system("rm -rf %s/.." % dir)

