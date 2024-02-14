
from Ship.Tags.Rect import Rect
from ext.BetterBuiltins import Unpackable, IAttributable


class Box(Rect):
	
	attributes = Unpackable({
		('padding','paddout') : [0]*2,
		'direction' : [1]*2,
		'primaryAxis' : 0,
	})
	
	
	def __init__(self):
		super().__init__()
		IAttributable.__init__(self, Box.attributes)
	
	
	

