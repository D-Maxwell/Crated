from ext.LoftyLogger import log
from ext.BetterBuiltins import Array

from freight import Parser

from ship.Node import Node
from ship.Crate import Crate



class Cargo(Node):
	"""
	Node of type Cargo.
	Point to a freight file through their path arg.
	"""
	
	def __init__(self, id:str=None, path:str=None, children:list=None):
		if id != id.upper():
			log("Cargo#{id} should be capitalised.",
			type='WARN')
		
		# let freight parameter of §init implying path and children by its strongly checked type
			
		self.path = path
		super().__init__(id, children)
		self.dim = Array([1280,720]) # TODO : bad
	
	
	def __repr__(self):
		return f"#{self.id}"
	
	
	def embark(self):
		if self.path is not None:
			self.children = Parser.parseFreight(self.path)
		
		for surface_crate in self.children:
			surface_crate.parent = self # assignments in comprehension lists ?? requires setter or messing with internal dicts
	

	# def assignParent(self):
	#     for idx in range(len(self.freight)):
	#         if self.freight[max(idx-1,0)].rank == self.freight[idx].rank - 1:
	#             self.freight[idx].parent = self.freight[max(idx-1,0)]


	def hook(self, path:str):
		pass
