'''
GenAccountsVV.py
Wed May 11 17:17:20 2005
Generated by MiddleKit.
'''

# MK attribute caches for setFoo() methods
_IDAttr = None
_NrAttr = None
_NameAttr = None
_KommentareAttr = None
_ErsteingabeAmAttr = None
_FehlercodeAttr = None
_changedOnAttr = None
_changedByAttr = None
_changedAtAttr = None

import types
from mx import DateTime


from MiddleKit.Run.MiddleObject import MiddleObject
from types import InstanceType, LongType



class GenAccountsVV(MiddleObject):

	def __init__(self):
		MiddleObject.__init__(self)
		self._ID            = None
		self._Nr            = None
		self._Name          = None
		self._Kommentare    = None
		self._ErsteingabeAm = None
		self._Fehlercode    = None
		self._changedOn     = None
		self._changedBy     = None
		self._changedAt     = None


	def ID(self):
		return self._ID

	def setID(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._ID
		self._ID = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _IDAttr
			if _IDAttr is None:
				_IDAttr = self.klass().lookupAttr('ID')
				if not _IDAttr.shouldRegisterChanges():
					_IDAttr = 0
			if _IDAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['ID'] = _IDAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Nr(self):
		return self._Nr

	def setNr(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Nr
		self._Nr = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _NrAttr
			if _NrAttr is None:
				_NrAttr = self.klass().lookupAttr('Nr')
				if not _NrAttr.shouldRegisterChanges():
					_NrAttr = 0
			if _NrAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Nr'] = _NrAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Name(self):
		return self._Name

	def setName(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Name
		self._Name = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _NameAttr
			if _NameAttr is None:
				_NameAttr = self.klass().lookupAttr('Name')
				if not _NameAttr.shouldRegisterChanges():
					_NameAttr = 0
			if _NameAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Name'] = _NameAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Kommentare(self):
		return self._Kommentare

	def setKommentare(self, value):
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Kommentare
		self._Kommentare = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _KommentareAttr
			if _KommentareAttr is None:
				_KommentareAttr = self.klass().lookupAttr('Kommentare')
				if not _KommentareAttr.shouldRegisterChanges():
					_KommentareAttr = 0
			if _KommentareAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Kommentare'] = _KommentareAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def ErsteingabeAm(self):
		return self._ErsteingabeAm

	def setErsteingabeAm(self, value):
		assert value is not None
		# have DateTime
		if value is not None:
			if type(value) is not DateTime.DateTimeType:
				raise TypeError, 'expecting date type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._ErsteingabeAm
		self._ErsteingabeAm = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _ErsteingabeAmAttr
			if _ErsteingabeAmAttr is None:
				_ErsteingabeAmAttr = self.klass().lookupAttr('ErsteingabeAm')
				if not _ErsteingabeAmAttr.shouldRegisterChanges():
					_ErsteingabeAmAttr = 0
			if _ErsteingabeAmAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['ErsteingabeAm'] = _ErsteingabeAmAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Fehlercode(self):
		return self._Fehlercode

	def setFehlercode(self, value):
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Fehlercode
		self._Fehlercode = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _FehlercodeAttr
			if _FehlercodeAttr is None:
				_FehlercodeAttr = self.klass().lookupAttr('Fehlercode')
				if not _FehlercodeAttr.shouldRegisterChanges():
					_FehlercodeAttr = 0
			if _FehlercodeAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Fehlercode'] = _FehlercodeAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def changedOn(self):
		return self._changedOn

	def setChangedOn(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._changedOn
		self._changedOn = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _changedOnAttr
			if _changedOnAttr is None:
				_changedOnAttr = self.klass().lookupAttr('changedOn')
				if not _changedOnAttr.shouldRegisterChanges():
					_changedOnAttr = 0
			if _changedOnAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['changedOn'] = _changedOnAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def changedBy(self):
		return self._changedBy

	def setChangedBy(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._changedBy
		self._changedBy = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _changedByAttr
			if _changedByAttr is None:
				_changedByAttr = self.klass().lookupAttr('changedBy')
				if not _changedByAttr.shouldRegisterChanges():
					_changedByAttr = 0
			if _changedByAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['changedBy'] = _changedByAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def changedAt(self):
		return self._changedAt

	def setChangedAt(self, value):
		assert value is not None
		# have DateTime
		if value is not None:
			if type(value) is not DateTime.DateTimeType:
				raise TypeError, 'expecting datetime type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._changedAt
		self._changedAt = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _changedAtAttr
			if _changedAtAttr is None:
				_changedAtAttr = self.klass().lookupAttr('changedAt')
				if not _changedAtAttr.shouldRegisterChanges():
					_changedAtAttr = 0
			if _changedAtAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['changedAt'] = _changedAtAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

