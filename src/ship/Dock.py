from ship.Node import Node
from ship.Crate import Crate



class Dock(Node):
	def __init__(self, children:[Crate]=None):
		super().__init__("root", children)
		
		self.ungated = True
		
		# self.focus:str = self.children[0].id
		self.steer(self.children[0].id)
	
	def embark(self):
		for cargo in self.children:
			cargo.dock = self
			cargo.embark()
			
	
	def steer(self, cargo_id):
		self.focus:str = cargo_id
	
	
	def sail(self): pass
