
from ext.BetterBuiltins import Unpackable, IAttributable, Array, A
from ship.Crate import Crate


class Rect(Crate, IAttributable):
	"""
	The lowest tag of all, the simplest there is.
	Rect, conversely to Crate, possesses graphical oriented properties,
	and so will any children thereof.
	"""
	
	attributes:dict = Unpackable({
		('pos','dim'): A[0,0],
		
		('origin','anchor'): A[-1,-1],
		
		'bg': [0]*3,
	})
	
	
	def __init__(self, **kwargs):
		
		# self.attributes:dict = {}
		
		## TODO : automagically reference topmost class
		IAttributable.__init__(self, Rect.attributes)
		super().__init__(**kwargs)
		
	
	def sail(self):
		# TODO : should anchor == origin unless explictly declared otherwise ?
		
		self.dimension()
		
		self.position()
	
		super().sail() 
		
	
	def position(self):
		
		# print(f"{self.attributes=}")
		
		origin = round( (self.origin + 1) / 2 * (self.parent.innerDim() if hasattr(self.parent,'innerDim') else self.parent.dim) )
		
		anchor = round( (self.anchor + 1) / 2 * self.outerDim() )
		
		
		offset = self.attributes.get('pos', Rect.attributes['pos'])
		if type(offset) is float:
			offset = A[ round(offset * self.parent.dim) ]
		
		# can't make use of array operations as each value depends on a condition
		# and i feel like trying would end up degrading the legibility of the code even further
		# offset = Array([round( pos * parent_dim ) if type(pos) is float else pos
		# 	for pos,parent_dim in zip(self.attributes.get('pos', Rect.attributes['pos']),self.parent.dim)])
		
		self.pos = origin - anchor + offset
		
		# if hasattr(self.parent, 'innerPos'):
		# 	self.pos += self.parent.innerPos()
			
	
	def dimension(self):
		# print(f"{self} ~ {self.attributes}")
		# print(f"{self.parent=}")
		# print(f"{self} {self.dim=} {self.parent.dim=} {self.parent=}")
		self.dim = Array([round(dim * parent_dim) if type(dim) is float else dim
			for dim,parent_dim in zip(self.dim,self.parent.innerDim() if hasattr(self.parent,'innerDim') else self.parent.dim)])
	
	
	
	# One could not declare both of these methods this way by default,
	# as one should not assume all classes implementing IContainer to have such fields
	
	def outerDim(self): return self.dim
	
	def innerDim(self): return self.dim
	
	
	def outerPos(self): return self.pos
	
	def innerPos(self): return self.pos
