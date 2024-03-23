from ship.Node import Node
from ship.containers.Rect import Rect



class Dock(Node):
	def __init__(self, id:str=None, data=None, children:list=None):
		super().__init__(id,data,children)
		
		self.selected_cargo:"" = self.children[0].id

	def embark(self, *cargo):
		for cargo in self.children:
			cargo.dock = self
			cargo.embark()
	
	def goto(self, cargo_id):
		self.selected_cargo = cargo_id
	
	
	def sail(self): pass
