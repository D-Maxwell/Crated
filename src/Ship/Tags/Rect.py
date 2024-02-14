
from ext.BetterBuiltins import Unpackable, IAttributable, Array
from Ship.Crate import Crate


class Rect(Crate, IAttributable):
	
	attributes:dict = Unpackable({
		('pos','dim'): Array([0]*2),
		
		('origin','anchor'): Array([-1]*2),
		
		'bg': [0]*3,
	})
	
	
	def __init__(self):
		super().__init__()
		IAttributable.__init__(self, Rect.attributes)
		
	
	def pack(self, line):
		super().pack(line)
		
		self.dimension()
		
		self.position()
		
		# self.resize()
	
	
	def position(self):
		
		origin = round( (self.origin + 1) / 2 * self.parent.dim )
		
		anchor = round( (self.anchor + 1) / 2 * self.dim )
		
		# can't make use of array operations as each value depends on a condition
		# and i feel like trying would end up degrading the legibility of the code even further
		offset = [round( pos * parent_dim ) if type(pos) is float else pos
			for pos,parent_dim in zip(self.pos,self.parent.dim)]
		
		self.pos = origin - anchor + offset
		
		if hasattr(self.parent, 'pos'):
			self.pos += self.parent.pos
			
		# print(self, f"(origin=} (offset=} (self.parent=} (self.parent.dim=} (self.pos=} (self.dim=}")
	
	
	def dimension(self):
		self.dim = [round(dim * parent_dim) if type(dim) is float else dim
			for dim,parent_dim in zip(self.dim,self.parent.dim)]
	
	
	# def position(self):
		# mode = None
		# for idx in range(len(self.pos)):
		# 	#self.pos[idx] = self.attributes.get("pos")[1]
		# 	#print(self.pos[idx])
		# 	if type(self.pos[idx]) is str:
		# 		#print(self.pos[idx].__contains__("R"))
		# 		if self.pos[idx].__contains__("R"):
		# 			mode = "R"

		# 		# exclude "", temp
		# 		self.pos[idx] = int(self.pos[idx][0:-1])

		# 		if self.parent is not None:
		# 			if mode == "R":
		# 				#self.pos[idx] += self.hook("#main")[0]
		# 				self.pos[idx] += self.parent.pos[idx]
		# 				#pass
	
	# def resize(self):
		# print(self, self.parent)

		# for s,dim in enumerate(self.dim):
		# 	if type(dim) is float:
		# 		if self.parent is None:
		# 			# last hack before going to bed
		# 			print(f"(self.cargo.dock.surface.get_size()=}")
		# 			self.dim[s] = int(self.dim[s] * self.cargo.dock.surface.get_size()[s])
		# 			print(f"(self.dim[s]=}")
		# 		else:
		# 			self.dim[s] = int(self.dim[s] * self.parent.dim[s])
