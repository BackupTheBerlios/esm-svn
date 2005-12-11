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
from MySQLdb import OperationalError,Warning
from Middle.Transfers import Transfers
from GlobalState import ID
import string

class TransferChange(SiteContent):

  def __init__(self, *args, **KWs):
    SiteContent.__init__(self, *args, **KWs)

  def writeContent(self, trans=None):
    #
    # this servlet creates and stores a new Transfer
    #

    account = self.transaction.request().field('account','')
    taid = self.transaction.request().field('taid','')
    page = self.transaction.request().field('page','Main')
    index = self.transaction.request().field('index',0)

    globalSetVars = self._globalSetVars
    store = globalSetVars['store']

    #
    # change transfer object
    #
    transferObjects = store.fetchObjectsOfClass('Transfers','WHERE TAID="%s"' % taid)
    transfer = transferObjects[0]
    transfer.setBeschreibung(string.strip(self.transaction.request().field('description','') + ' ' + self.transaction.request().field('notice','')))
    transfer.setWho(self.transaction.request().field('name',''))
    transfer.setHaben(float(string.replace(self.transaction.request().field('Haben','0,0'),',','.')))
    transfer.setSoll(float(string.replace(self.transaction.request().field('Soll','0,0'),',','.')))
    transfer.setDatum(DateTime.DateTimeFrom(self.transaction.request().field('date',DateTime.now())))
    transfer.setBKZ(self.transaction.request().field('bkz',''))
    transfer.setJahr(DateTime.DateTimeFrom(self.transaction.request().field('date',DateTime.now())).year)
    transfer.setChangedBy(self.transaction.session().value('authenticated_user',''))
    transfer.setChangedAt(DateTime.now())
    transfer.setChangedOn(self.getSite())
    #
    # store transfer in database
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
    # test for errors and consistency
    #
    if not self.transaction.request().field('name',''):
      self.transaction.response().sendRedirect(string.split(self.transaction.request().environ()['HTTP_REFERER'],'?')[0] + '?id=%s&taid=%s&index=%s&error=Bitte einen Zahlungsempfänger angeben' % (account,taid,index))
    elif (DateTime.DateTimeFrom(self.transaction.request().field('date',DateTime.now())).year > (DateTime.now().year + 2)) or \
      (DateTime.DateTimeFrom(self.transaction.request().field('date',DateTime.now())).year < (DateTime.now().year - 5)):
        self.transaction.response().sendRedirect(string.split(self.transaction.request().environ()['HTTP_REFERER'],'?')[0] + '?id=%s&taid=%s&index=%s&error=das Buchungsdatum scheint nicht korrekt zu sein' % (account,taid,index))
    elif float(string.replace(self.transaction.request().field('Haben','0,0'),',','.')) < 0.0:
      self.transaction.response().sendRedirect(string.split(self.transaction.request().environ()['HTTP_REFERER'],'?')[0] + '?id=%s&taid=%s&index=%s&error=das Haben darf nicht negativ sein' % (account,taid,index))
    elif float(string.replace(self.transaction.request().field('Soll','0,0'),',','.')) < 0.0:
      self.transaction.response().sendRedirect(string.split(self.transaction.request().environ()['HTTP_REFERER'],'?')[0] + '?id=%s&taid=%s&index=%s&error=das Soll darf nicht negativ sein' % (account,taid,index))
    elif (float(string.replace(self.transaction.request().field('Soll','0,0'),',','.')) == 0.0) and (float(string.replace(self.transaction.request().field('Haben','0,0'),',','.')) == 0.0):
      self.transaction.response().sendRedirect(string.split(self.transaction.request().environ()['HTTP_REFERER'],'?')[0] + '?id=%s&taid=%s&index=%s&error=Haben oder Soll müssen einen Wert haben' % (account,taid,index))
    elif (float(string.replace(self.transaction.request().field('Soll','0,0'),',','.')) != 0.0) and (float(string.replace(self.transaction.request().field('Haben','0,0'),',','.')) != 0.0):
      self.transaction.response().sendRedirect(string.split(self.transaction.request().environ()['HTTP_REFERER'],'?')[0] + '?id=%s&taid=%s&index=%s&error=entweder Haben oder Soll darf einen Wert haben' % (account,taid,index))

    #
    # back to old page
    #
    elif index:
      self.transaction.response().sendRedirect(page + '?account=%s&index=%s' % (account,index))
    else:
      self.transaction.response().sendRedirect(page + '?account=%s' % account)
