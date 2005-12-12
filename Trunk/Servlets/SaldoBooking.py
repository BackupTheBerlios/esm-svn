#
# File:      $URL$
# Version:   $rev$
# Changed:   $date$
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
__revision__ = "$Rev$"[4,-2]

from SiteContent import SiteContent
from mx import DateTime
from Middle.Transfers import Transfers
from UniqueID import UniqueID
import string

class SaldoBooking(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)
    self.storeName = 'Transfers'
    self.accountStores = {
      'MI':'AccountsMI',
      'TR':'AccountsTR',
      'VE':'AccountsVE',
      'BK':'AccountsBK',
      'VV':'AccountsVV'
    }

  def writeContent(self, trans=None):
    #
    # get the year for which the new saldos have to be calculated
    #
    try:
      year = int(self.transaction.request().field('year',''))
    except ValueError:
      self.transaction.response().sendRedirect('Administration')
    else:
      globalSetVars = self._globalSetVars
      store = globalSetVars['store']
      #
      # remove old saldos from next year
      #
      storeObjects = store.fetchObjectsOfClass(self.storeName,'WHERE Jahr="%s" AND (BKZ="SVH" OR BKZ = "SVS")' % str(year+1))
      for x in storeObjects:
        store.deleteObject(x)
      store.saveChanges()
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
      # store new saldos
      #
      for x in saldos.keys():
        if x[:2] in self.accountStores.keys():
          #
          # create transfer object
          #
          member = store.fetchObjectsOfClass(self.accountStores[x[:2]],'WHERE ID="%s"' % x)
          if member:
            attrs = member[0].allAttrs(0)
            transfer = Transfers()
            transfer.setTAID(self.getSite() + DateTime.now().strftime("%Y%m%d%H%M%S") + "%04d" % UniqueID.next())
            if attrs.has_key('Firma') and attrs['Firma']:
              transfer.setImportWho(attrs['Firma'])
              transfer.setWho(attrs['Firma'])
            elif attrs.has_key('Bank'):
              transfer.setImportWho(attrs['Bank'])
              transfer.setWho(attrs['Bank'])
            elif attrs.has_key('Name'):
              transfer.setImportWho(attrs['Name'])
              transfer.setWho(attrs['Name'])
            else:
              transfer.setImportWho(attrs['Nachname'] + ', ' + attrs['Vorname'])
              transfer.setWho(attrs['Nachname'] + ', ' + attrs['Vorname'])
            transfer.setImportBeschreibung('Saldovortrag aus %i' % year)
            transfer.setBeschreibung('Saldovortrag aus %i' % year)
            if saldos[x] > 0.0:
              transfer.setBKZ('SVH')
              transfer.setTransferID(x + "_SVH")
              if year+1 == 2002:
                transfer.setHaben(round(saldos[x] / 1.95583,2))
              else:
                transfer.setHaben(saldos[x])
              transfer.setSoll(0.0)
            else:
              transfer.setBKZ('SVS')
              transfer.setTransferID(x + "_SVS")
              transfer.setHaben(0.0)
              if year+1 == 2002:
                transfer.setSoll(0.0 - round(saldos[x] / 1.95583,2))
              else:
                transfer.setSoll(0.0 - saldos[x])
            transfer.setKonto1(x)
            transfer.setKonto2(x)
            transfer.setChangedBy(self.transaction.session().value('authenticated_user',''))
            transfer.setChangedAt(DateTime.now())
            transfer.setJahr(year+1)
            transfer.setDatum(DateTime.DateTimeFrom('31.12.' + str(year)))
            transfer.setChangedOn(self.getSite())
            store.addObject(transfer)
      store.saveChanges()
      self.transaction.response().sendRedirect('Administration')
