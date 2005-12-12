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

from SiteContent import SiteContent
from mx import DateTime
from Middle.Transfers import Transfers
import string
from MiscUtils.Funcs import uniqueId

priceStore = 'Prices'

class Lastschriften(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'Transfers'
    self.accountStores = {
      'MI':'AccountsMI'
    }

  def writeContent(self, trans=None):
    #
    # get the year for which the new saldos have to be calculated
    #
    try:
      year = int(self.transaction.request().field('date','')[-4:])
    except ValueError:
      self.transaction.response().sendRedirect('Administration')
    else:
      bemerkung = self.transaction.request().field('bemerkung','')
      notice = self.transaction.request().field('notice','')
      globalSetVars = self._globalSetVars
      store = globalSetVars['store']
      #
      # BKZs einlesen
      #
      priceObjects = store.fetchObjectsOfClass(priceStore)
      prices = {}
      for x in priceObjects:
        a = x.allAttrs(0)
        prices[a['BKZ']] = a
      konto = prices['EL']['Konto']
      #
      # calculate new saldos from given year
      #
      transfers = store.fetchObjectsOfClass(self.storeName,'WHERE Jahr="%s" ORDER BY Datum' % str(year))
      saldos = {}
      for transfer in transfers:
        x = transfer.allAttrs(0)
        if saldos.has_key(x['Konto1']):
          saldo = saldos[x['Konto1']]
        else:
          saldo = 0.0
        if x['Haben'] != 0.0:
          saldo = saldo + x['Haben']
        if x['Soll'] != 0.0:
          saldo = saldo - x['Soll']
        if saldo != 0.0:
          saldos[x['Konto1']] = saldo
        elif saldos.has_key(x['Konto1']):
          del saldos[x['Konto1']]
        if (x['Konto1'] != x['Konto2']):
          if saldos.has_key(x['Konto2']):
            saldo = saldos[x['Konto2']]
          else:
            saldo = 0.0
          if x['Haben'] != 0.0:
            saldo = saldo - x['Haben']
          if x['Soll'] != 0.0:
            saldo = saldo + x['Soll']
          if saldo != 0.0:
            saldos[x['Konto2']] = saldo
          elif saldos.has_key(x['Konto2']):
            del saldos[x['Konto2']]
      #
      # book Lastschriften
      #
      taid = self.getSite() + DateTime.now().strftime("%Y%m%d%H%M%S") + uniqueId(self)[:4]
      for x in saldos.keys():
        if (x[:2] in self.accountStores.keys()) and (x[-1:] == '0') and (saldos[x] < 0.1):
          #
          # create transfer objectonly for Zahlungsart == "Lastschrift"
          #
          member = store.fetchObjectsOfClass(self.accountStores[x[:2]],'WHERE ID="%s"' % x)[0].allAttrs(0)
          if member['Zahlungsart'] == 'Lastschrift':
            transfer = Transfers()
            transfer.setTAID(taid)
            transfer.setImportWho(member['Nachname'] + ', ' + member['Vorname'])
            if notice:
              transfer.setImportBeschreibung(bemerkung + "(%s)" % notice)
              transfer.setBeschreibung(bemerkung + "(%s)" % notice)
            else:
              transfer.setImportBeschreibung(bemerkung)
              transfer.setBeschreibung(bemerkung)
            transfer.setWho(member['Nachname'] + ', ' + member['Vorname'])
            transfer.setBKZ('EL')
            transfer.setTransferID(x + "_EL")
            transfer.setHaben(saldos[x] * -1.0)
            transfer.setSoll(0.0)
            if x < konto:
              transfer.setKonto1(x)
              transfer.setKonto2(konto)
            else:
              transfer.setKonto1(konto)
              transfer.setKonto2(x)
            transfer.setChangedBy(self.transaction.session().value('authenticated_user',''))
            transfer.setChangedAt(DateTime.now())
            transfer.setJahr(year)
            transfer.setDatum(DateTime.now())
            transfer.setChangedOn(self.getSite())
            store.addObject(transfer)
      for x in self.accountStores.keys():
        storeObjects = store.fetchObjectsOfClass('IDs','WHERE %s = "%s"' % ('Tablename',self.accountStores[x]))
        if (len(storeObjects) == 1):
          id = storeObjects[0]
          id.setLastschriften(taid)
      store.saveChanges()
      self.transaction.response().sendRedirect('Administration')
