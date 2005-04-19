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

#
# esm.misc
#

import string

True = 1
False = 0
dateFormat = '%d.%m.%Y'

def buildAccountClause(search,alphaSearchFields,numericSearchFields,sortField=''):
  if len(search) > 0:
    searchPattern = string.replace(string.lower(search),'*','%')
    searchPattern = string.replace(string.lower(searchPattern),'?','_')
    if searchPattern[0] in "0123456789":
      searchFields = numericSearchFields
    else:
      searchFields = alphaSearchFields
    if len(searchFields) > 0:
      clause = 'WHERE'
      first = True
      for x in searchFields:
        if first:
          first = False
        else:
          clause = clause + ' OR '
        clause = clause + ' %s LIKE "%s"' % (x,searchPattern)
      return clause + ' ORDER BY ' + searchFields[0]
    else:
      return 'ORDER BY ' + string.join(searchFields,',')
  elif sortField:
    return 'ORDER BY ' + sortField
  else:
    return 'ORDER BY ' + string.join(alphaSearchFields,',')

def nbOfMonths(a,b):
  return abs(a.year * 12 + a.month - b.year * 12 - b.month)

def age(birthday,referencedate):
  if (referencedate.month * 100 + referencedate.day) < (birthday.month * 100 + birthday.day):
    return referencedate.year - birthday.year - 1
  else:
    return referencedate.year - birthday.year

def fee(bkz,eintritt,ab,freiab,erhebungab,newdate,price,notiz):
  if erhebungab >= price['Ab']:
    price_haben = price['AbHaben']
    price_soll = price['AbSoll']
  else:
    price_haben = price['Haben']
    price_soll = price['Soll']
  if ab and not freiab and not erhebungab:
    soll = price_soll*float(nbOfMonths(ab,newdate))
    haben = 0.0
    beschreibung = ab.strftime(dateFormat) + ' - ' + newdate.strftime(dateFormat) + ' ' + price['Beschreibung']
  elif ab and freiab and not erhebungab:
    if freiab > ab:
      soll = price_soll*float(nbOfMonths(ab,freiab))
      haben = 0.0
      beschreibung = ab.strftime(dateFormat) + ' - ' + freiab.strftime(dateFormat) + ' ' + price['Beschreibung']
  elif ab and not freiab and erhebungab:
    if ab > erhebungab:
      soll = price_soll*float(nbOfMonths(ab,newdate))
      haben = 0.0
      beschreibung = ab.strftime(dateFormat) + ' - ' + newdate.strftime(dateFormat) + ' ' + price['Beschreibung']
    else:
      soll = price_soll*float(nbOfMonths(erhebungab,newdate))
      haben = 0.0
      beschreibung = erhebungab.strftime(dateFormat) + ' - ' + newdate.strftime(dateFormat) + ' ' + price['Beschreibung']
  elif freiab < erhebungab:
    soll = 0.0
    haben = price_soll*float(nbOfMonths(freiab,erhebungab))
    bkz = 'GutBei'
    beschreibung = freiab.strftime(dateFormat) + ' - ' + erhebungab.strftime(dateFormat) + ' ' + price['Beschreibung']
  elif freiab >= erhebungab:
    if newdate > freiab:
      soll = price_soll*float(nbOfMonths(erhebungab,freiab))
      haben = 0.0
      beschreibung = erhebungab.strftime(dateFormat) + ' - ' + freiab.strftime(dateFormat) + ' ' + price['Beschreibung']
    else:
      soll = price_soll*float(nbOfMonths(erhebungab,newdate))
      haben = 0.0
      beschreibung = erhebungab.strftime(dateFormat) + ' - ' + newdate.strftime(dateFormat) + ' ' + price['Beschreibung']
  else:
    soll = price_soll*float(nbOfMonths(erhebungab,freiab))
    haben = 0.0
    beschreibung = erhebungab.strftime(dateFormat) + ' - ' + freiab.strftime(dateFormat) + ' ' + price['Beschreibung']
  if notiz:
    beschreibung = beschreibung + ' (' + notiz + ')'
  return soll,haben,bkz,beschreibung

