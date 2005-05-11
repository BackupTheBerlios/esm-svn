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

from SiteTemplate import SiteTemplate
from mx import DateTime
from MySQLdb import OperationalError,Warning
from Middle.Transfers import Transfers
from misc import fee
import string
from MiscUtils.Funcs import uniqueId

role = 'manager'

tableStore = 'AccountsMI'
priceStore = 'Prices'

Anzahl_Beitragsarten = 5

class FeesBooking(SiteTemplate):

  def __init__(self, *args, **KWs):
    SiteTemplate.__init__(self, *args, **KWs)

  def writeContent(self, trans=None):
    #
    # read in database
    #
    globalSetVars = self._globalSetVars
    store = globalSetVars['store']
    priceObjects = store.fetchObjectsOfClass(priceStore)
    prices = {}
    for x in priceObjects:
      a = x.allAttrs(0)
      prices[a['BKZ']] = a
    taid = self.getSite() + DateTime.now().strftime("%Y%m%d%H%M%S") + uniqueId(self)[:4]
    if tableStore != '':
      date = DateTime.DateTimeFrom(self.transaction.request().field('date',''))
      notice = self.transaction.request().field('notice','')
      bookdate = DateTime.DateTimeFrom(self.transaction.request().field('bookdate',''))
      #
      # read all objects from database
      #
      storeObjects = store.fetchObjectsOfClass(tableStore,'WHERE ID like "%%0"')
      for entry in storeObjects:
        attrs = entry.allAttrs(0)
        for y in range(Anzahl_Beitragsarten):
          #
          # Aufnahmegebuehr kalkulieren
          #
          if (attrs['Beitragsart'+str(y+1)] != '') \
              and (attrs['BeitragsartErhebungAb'+str(y+1)] == attrs['Eintrittsdatum']) \
              and not (attrs['BeitragsartFreiAb'+str(y+1)] and (attrs['BeitragsartFreiAb'+str(y+1)] <= attrs['Eintrittsdatum'])) \
              and (attrs['BeitragsartErhebungAb'+str(y+1)] < date):
            price = prices['11' + attrs['Beitragsart'+str(y+1)][2:]]
            if attrs['BeitragsartErhebungAb'+str(y+1)] >= price['Ab']:
              price_haben = price['AbHaben']
              price_soll = price['AbSoll']
            else:
              price_haben = price['Haben']
              price_soll = price['Soll']
            transfer = Transfers()
            transfer.setTAID(taid)
            transfer.setTransferID(attrs['ID'] + "_" + price['BKZ'])
            transfer.setWho(attrs['Nachname'] + ', ' + attrs['Vorname'])
            transfer.setImportWho(attrs['Nachname'] + ', ' + attrs['Vorname'])
            transfer.setBeschreibung(price['Beschreibung'])
            transfer.setImportBeschreibung(price['Beschreibung'])
            transfer.setHaben(price_haben)
            transfer.setSoll(price_soll)
            if attrs['ID'] < price['Konto']:
              transfer.setKonto1(price['Konto'])
              transfer.setKonto2(attrs['ID'])
            else:
              transfer.setKonto1(attrs['ID'])
              transfer.setKonto2(price['Konto'])
            transfer.setChangedBy(self.transaction.session().value('authenticated_user',''))
            transfer.setChangedAt(DateTime.now())
            if bookdate:
              transfer.setJahr(bookdate.year)
              transfer.setDatum(bookdate)
            else:
              transfer.setJahr(DateTime.now().year)
              transfer.setDatum(DateTime.now())
            transfer.setBKZ(price['BKZ'])
            transfer.setChangedOn(self.getSite())
            #
            # store transfer in database
            #
            store.addObject(transfer)
            #
          #
          # Beitrag kalkulieren
          #
          if attrs['Beitragsart'+str(y+1)] \
              and not ((attrs['BeitragsartFreiAb'+str(y+1)] == attrs['BeitragsartErhebungAb'+str(y+1)]) \
                and attrs['BeitragsartFreiAb'+str(y+1)] \
                and attrs['BeitragsartErhebungAb'+str(y+1)]) \
              and (attrs['BeitragsartAb'+str(y+1)] < date) \
              and (attrs['BeitragsartErhebungAb'+str(y+1)] \
                and (attrs['BeitragsartErhebungAb'+str(y+1)] < date)) \
              and (not attrs['BeitragsartFreiAb'+str(y+1)] \
                or (attrs['BeitragsartFreiAb'+str(y+1)] >= attrs['BeitragsartErhebungAb'+str(y+1)])) \
              and (not attrs['Austrittsdatum'] \
                or (attrs['Austrittsdatum'] >= attrs['BeitragsartErhebungAb'+str(y+1)])):
            price = prices[attrs['Beitragsart'+str(y+1)]]
            price_soll,price_haben,bkz,beschreibung = fee(attrs['Beitragsart'+str(y+1)],attrs['Eintrittsdatum'],attrs['BeitragsartAb'+str(y+1)],attrs['BeitragsartFreiAb'+str(y+1)],attrs['BeitragsartErhebungAb'+str(y+1)],date,price,notice)
            transfer = Transfers()
            transfer.setTAID(taid)
            transfer.setTransferID(attrs['ID'] + "_" + price['BKZ'])
            transfer.setWho(attrs['Nachname'] + ', ' + attrs['Vorname'])
            transfer.setImportWho(attrs['Nachname'] + ', ' + attrs['Vorname'])
            transfer.setBeschreibung(beschreibung)
            transfer.setImportBeschreibung(beschreibung)
            transfer.setHaben(price_haben)
            transfer.setSoll(price_soll)
            if attrs['ID'] < price['Konto']:
              transfer.setKonto1(price['Konto'])
              transfer.setKonto2(attrs['ID'])
            else:
              transfer.setKonto1(attrs['ID'])
              transfer.setKonto2(price['Konto'])
            transfer.setChangedBy(self.transaction.session().value('authenticated_user',''))
            transfer.setChangedAt(DateTime.now())
            if bookdate:
              transfer.setJahr(bookdate.year)
              transfer.setDatum(bookdate)
            else:
              transfer.setJahr(DateTime.now().year)
              transfer.setDatum(DateTime.now())
            transfer.setBKZ(bkz)
            transfer.setChangedOn(self.getSite())
            #
            # store transfer in database
            #
            store.addObject(transfer)
            if attrs['BeitragsartFreiAb'+str(y+1)] and (date >= attrs['BeitragsartFreiAb'+str(y+1)]):
              entry.setValueForKey('BeitragsartErhebungAb'+str(y+1), attrs['BeitragsartFreiAb'+str(y+1)])
            else:
              entry.setValueForKey('BeitragsartErhebungAb'+str(y+1), date)
      #
      # save changes
      #
      try:
        store.saveChanges()
      except OperationalError,x:
        store.discardEverything()
        errorCode,errorText = x
        #
        # back to error page
        #
        self.transaction.response().sendRedirect('Error?problem=Daten+konnten+nicht+gespeichert+werden!&reason=' + urlEncode(str(errorText)))
      except Warning,x:
        pass
      #
      # back to old page
      #
      self.transaction.response().sendRedirect('Administration')
