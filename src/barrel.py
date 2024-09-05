
import os

import crated # adrift
import freight.Parser as Parser

from ship.Cargo import Cargo

from ship.Crate import Crate
from ship.containers.Box import Box
from ship.containers.Rect import Rect



## Freight format ##

# crated.dock = PygameDock(
# 	[Parser.loadFreight(f"./freight/{file}")
# 	for file in os.listdir()]
# )


DOCK = crated.PygameDock([
	Cargo("ID", children=[
		Box(
		dim=[1.0,1.0],
		padding=6,
		children=[
			Rect(id=["hellothere"],
			dim=[512,256],
			bg="FF00FF",
			)
		])
	])
])


DOCK.embark()

while DOCK.ungated:
	
	try:
		
		DOCK.sail()
		
		
	except KeyboardInterrupt:
		DOCK.ungated = False
		
	
# del DOCK


# while True : if DOCK.gated: return; ??