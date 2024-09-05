
from ship.containers.Rect import Rect
from ext.BetterBuiltins import Unpackable, IAttributable, A


class Box(Rect):
	
	attributes = Unpackable({
		('padding','paddout') : A[0,0],
		'direction' : A[1,1],
		'primaryAxis' : 0, # Enum Axis.X
	})
	
	
	def __init__(self, **kwargs):
		IAttributable.__init__(self, Box.attributes)
		super().__init__(**kwargs)
	
	
	
	def outerDim(self):
		# print(f"{self} {self.dim=}")
		return self.dim + self.paddout * 2
	
	
	def innerDim(self):
		return self.dim - self.padding * 2
	
	
	def innerPos(self):
		return self.pos + self.padding
	
	
	def outerPos(self):
		# print(f"{self.pos=} {self.paddout=}")
		return self.pos - self.paddout

