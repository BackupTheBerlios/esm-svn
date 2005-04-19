'''
GenPrices.py
Sat Nov 30 12:00:18 2002
Generated by MiddleKit.
'''

# MK attribute caches for setFoo() methods
_BKZAttr = None
_SollAttr = None
_HabenAttr = None
_BeschreibungAttr = None
_AbAttr = None
_AbSollAttr = None
_AbHabenAttr = None
_KontoAttr = None
_changedOnAttr = None
_changedAtAttr = None
_changedByAttr = None

import types
from mx import DateTime


from MiddleKit.Run.MiddleObject import MiddleObject
from types import InstanceType, LongType



class GenPrices(MiddleObject):

	def __init__(self):
		MiddleObject.__init__(self)
		self._BKZ          = None
		self._Soll         = None
		self._Haben        = None
		self._Beschreibung = None
		self._Ab           = None
		self._AbSoll       = None
		self._AbHaben      = None
		self._Konto        = None
		self._changedOn    = None
		self._changedAt    = None
		self._changedBy    = None


	def BKZ(self):
		return self._BKZ

	def setBKZ(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._BKZ
		self._BKZ = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _BKZAttr
			if _BKZAttr is None:
				_BKZAttr = self.klass().lookupAttr('BKZ')
				if not _BKZAttr.shouldRegisterChanges():
					_BKZAttr = 0
			if _BKZAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['BKZ'] = _BKZAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Soll(self):
		return self._Soll

	def setSoll(self, value):
		assert value is not None
		if value is not None:
			if type(value) in (types.IntType, types.LongType):
				value = float(value)
			elif type(value) is not types.FloatType:
				raise TypeError, 'expecting float type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Soll
		self._Soll = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _SollAttr
			if _SollAttr is None:
				_SollAttr = self.klass().lookupAttr('Soll')
				if not _SollAttr.shouldRegisterChanges():
					_SollAttr = 0
			if _SollAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Soll'] = _SollAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Haben(self):
		return self._Haben

	def setHaben(self, value):
		assert value is not None
		if value is not None:
			if type(value) in (types.IntType, types.LongType):
				value = float(value)
			elif type(value) is not types.FloatType:
				raise TypeError, 'expecting float type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Haben
		self._Haben = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _HabenAttr
			if _HabenAttr is None:
				_HabenAttr = self.klass().lookupAttr('Haben')
				if not _HabenAttr.shouldRegisterChanges():
					_HabenAttr = 0
			if _HabenAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Haben'] = _HabenAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Beschreibung(self):
		return self._Beschreibung

	def setBeschreibung(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Beschreibung
		self._Beschreibung = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _BeschreibungAttr
			if _BeschreibungAttr is None:
				_BeschreibungAttr = self.klass().lookupAttr('Beschreibung')
				if not _BeschreibungAttr.shouldRegisterChanges():
					_BeschreibungAttr = 0
			if _BeschreibungAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Beschreibung'] = _BeschreibungAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Ab(self):
		return self._Ab

	def setAb(self, value):
		# have DateTime
		if value is not None:
			if type(value) is not DateTime.DateTimeType:
				raise TypeError, 'expecting date type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Ab
		self._Ab = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _AbAttr
			if _AbAttr is None:
				_AbAttr = self.klass().lookupAttr('Ab')
				if not _AbAttr.shouldRegisterChanges():
					_AbAttr = 0
			if _AbAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Ab'] = _AbAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def AbSoll(self):
		return self._AbSoll

	def setAbSoll(self, value):
		if value is not None:
			if type(value) in (types.IntType, types.LongType):
				value = float(value)
			elif type(value) is not types.FloatType:
				raise TypeError, 'expecting float type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._AbSoll
		self._AbSoll = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _AbSollAttr
			if _AbSollAttr is None:
				_AbSollAttr = self.klass().lookupAttr('AbSoll')
				if not _AbSollAttr.shouldRegisterChanges():
					_AbSollAttr = 0
			if _AbSollAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['AbSoll'] = _AbSollAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def AbHaben(self):
		return self._AbHaben

	def setAbHaben(self, value):
		if value is not None:
			if type(value) in (types.IntType, types.LongType):
				value = float(value)
			elif type(value) is not types.FloatType:
				raise TypeError, 'expecting float type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._AbHaben
		self._AbHaben = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _AbHabenAttr
			if _AbHabenAttr is None:
				_AbHabenAttr = self.klass().lookupAttr('AbHaben')
				if not _AbHabenAttr.shouldRegisterChanges():
					_AbHabenAttr = 0
			if _AbHabenAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['AbHaben'] = _AbHabenAttr  # changedAttrs is a set
				# Tell ObjectStore it happened
				self._mk_store.objectChanged(self)

	def Konto(self):
		return self._Konto

	def setKonto(self, value):
		assert value is not None
		if value is not None:
			if type(value) is not types.StringType:
				raise TypeError, 'expecting string type, but got value %r of type %r instead' % (value, type(value))

		# set the attribute
		origValue = self._Konto
		self._Konto = value

		# MiddleKit machinery
		self._mk_changed = 1  # @@ original semantics, but I think this should be under "if not self._mk_initing..."
		if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
			global _KontoAttr
			if _KontoAttr is None:
				_KontoAttr = self.klass().lookupAttr('Konto')
				if not _KontoAttr.shouldRegisterChanges():
					_KontoAttr = 0
			if _KontoAttr:
				# Record that it has been changed
				if self._mk_changedAttrs is None:
					self._mk_changedAttrs = {} # maps name to attribute
				self._mk_changedAttrs['Konto'] = _KontoAttr  # changedAttrs is a set
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
