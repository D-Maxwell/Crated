from Ship.Node import Node



from Ship.Tags.Rect import Rect

PrimitiveTags = {
	Rect : ["rect","Rect",""] # tag will never contain an empty string, thus last element serves no purpose
}



class Dock(Node):
	def __init__(self, id:str=None, data=None, children:list=None):
		super().__init__(id,data,children)

		self.selected_cargo:"" = self.children[0].id

	def ship(self, *cargo):
		for cargo in self.children:
			cargo.dock = self
			cargo.load()

	def goto(self, cargo_id):
		self.selected_cargo = cargo_id
