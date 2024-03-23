
from ext.BetterBuiltins import Unpackable, IAttributable, Array
from ship.Crate import Crate


class Rect(Crate, IAttributable):
	"""
	The lowest tag of all, the simplest there is.
	Rect, conversely to Crate, possesses graphical oriented properties,
	and so will any children thereof.
	"""
	
	
	
	def __init__(self):
		
		self.attributes:dict = self.attributes | Unpackable({
			('pos','dim'): Array([0]*2),
			
			('origin','anchor'): Array([-1]*2),
			
			'bg': [0]*3,
		})
		
		# super().__init__()
		IAttributable.__init__(self, self.attributes)
		print(f"{self.attributes['pos']=}")
		
	
	# def pack(self, line):
	# 	super().pack(line)
	
	def sail(self):
		# TODO : should anchor == origin unless explictly declared otherwise ?
		
		self.dimension()
		
		self.position()
	
	
	def position(self):
		
		# print(f"{self.attributes=}")
		
		origin = round( (self.origin + 1) / 2 * (self.parent.innerDim() if hasattr(self.parent,'innerDim') else self.parent.dim) )
		
		anchor = round( (self.anchor + 1) / 2 * self.outerDim() )
		
		# can't make use of array operations as each value depends on a condition
		# and i feel like trying would end up degrading the legibility of the code even further
		offset = Array([round( pos * parent_dim ) if type(pos) is float else pos
			for pos,parent_dim in zip(self.attributes['pos'],self.parent.dim)])
		
		self.pos = origin - anchor + offset
		
		if hasattr(self.parent, 'innerPos'):
			self.pos += self.parent.innerPos()
			
		
		return;
		if 'title' in self.classes:
			print(self, f"{origin=} {offset=} {self.parent=} {self.parent.dim=} {self.pos=} {self.dim=}")
	
	
	def dimension(self):
		self.dim = Array([round(dim * parent_dim) if type(dim) is float else dim
			for dim,parent_dim in zip(self.dim,self.parent.innerDim() if hasattr(self.parent,'innerDim') else self.parent.dim)])
	
	
	
	# One could not declare both of these methods this way by default,
	# as one should not assume all classes implementing IContainer to have such fields
	
	def outerDim(self): return self.dim
	
	def innerDim(self): return self.dim
	
	
	def outerPos(self): return self.pos
	
	def innerPos(self): return self.pos
