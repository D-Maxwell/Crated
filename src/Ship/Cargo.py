from ext.Console import log
from ext.BetterBuiltins import Array

from ship.Node import Node
from ship.Crate import Crate



class Cargo(Node):
	"""
	Node of type Cargo.
	Point to a freight file through their path arg.
	"""
	
	def __init__(self, id:str=None, path=None, children:list=None):
		super().__init__(id,path,children)
		self.freight = [] # TODO : why is this not implemented equivalently to §children
		self.dim = Array([1280,720]) # TODO : bad
	
	
	def __repr__(self):
		return f"#{self.id}"
	
	
	def embark(self):
		try:
			file = open(self.data)
		except FileNotFoundError:
			log(f"File at path '{self.data}' could not be found. Make sure to include the '.frg' suffix, and check the scope.",
				type='ERROR')
		else:
			
			isComment:bool = False
			
			parent_indentation:int = 0
			parent:[Crate] = [self]
			
			lines:[''] = file.read().splitlines()

			for l,line in enumerate(lines):
				# if line == r"\\\ ".strip(): # raw string literals can't end in a backslash for some reason
				if line == "```":
					isComment ^= True
					continue
				if isComment or line == '': continue
				
				
				line:str = line.lstrip('\t')
				indentation:int = len(lines[l]) - len(line)
				print(f"{indentation=} {parent_indentation=}")
				
				
				
				crate = Crate()
				
				# crate = inherit(, PrimitiveTags)() # temp Crate instance, TODO : make inherit a function not a method
				
				
				crate.cargo = self
				# crate.pack(line)
				
				
				# crate.__class__ = globals()[crate.inherit()] if crate.inherit() != crate.__class__ else crate.__class__
				# crate.__class__ = crate.inherit(PrimitiveTags)
				# crate.__init__()
				
				
				if indentation < parent_indentation:
					parent.pop()
				
				
				if len(parent) > 0:
					crate.attributes['parent'] = parent[-1]
					print(f"{crate.parent=} {parent=}")
				
				crate.pack(line)
				
				
				if indentation >= parent_indentation:
					parent += [crate]
				
				parent_indentation = indentation
				
				
				self.freight.append(crate)
				
		finally:
			file.close()
	

	# def assignParent(self):
	#     for idx in range(len(self.freight)):
	#         if self.freight[max(idx-1,0)].rank == self.freight[idx].rank - 1:
	#             self.freight[idx].parent = self.freight[max(idx-1,0)]


	def hook(self, path:str):
		pass
