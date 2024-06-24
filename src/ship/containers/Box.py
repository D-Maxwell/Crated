
from ship.containers.Rect import Rect
from ext.BetterBuiltins import Unpackable, IAttributable, A


class Box(Rect):
	
	attributes = Unpackable({
		('padding','paddout') : A[0,0],
		'direction' : A[1,1],
		'primaryAxis' : 0, # Enum Axis.X
	})
	
	
	def __init__(self):
		super().__init__()
		IAttributable.__init__(self, Box.attributes)
	
	
	
	def outerDim(self):
		return self.dim + self.paddout * 2
	
	
	def innerDim(self):
		# print(f"{self.dim=} {self.padding=} {self.dim - self.padding * 2=}")
		return self.dim - self.padding * 2
	
	
	def innerPos(self):
		# print(f"{self.pos=} {self.paddout=} {self.padding=} {self.pos + self.paddout + self.padding=}")
		return self.pos + self.paddout + self.padding

