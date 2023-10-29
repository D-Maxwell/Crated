from src.Ship import Crate
from src.ext.Console import log
from src.Ship.Node import Node
from src.Ship.Crate import Crate
from src.Ship.Dock import PrimitiveTags


def swap(arg:list):
	out = []
	for idx in range(len(arg)):
		e = arg[idx]
		out.append(arg[-1 - idx])
	return out


class Cargo(Node):
	"""
	Node of type Cargo.
	Point to a freight file through their path arg.
	"""

	def __init__(self, id:str=None, path=None, children:list=None):
		super().__init__(id,path,children)
		self.freight = []

	def load(self):
		try:
			file = open(self.data)
		except FileNotFoundError:
			log(f"File at path '{self.data}' could not be found. Make sure to include the '.frg' suffix, and check the scope.",
				type='ERROR')
		else:

			isComment:bool = False

			parent_indentation:int = 0
			parent:[Crate] = []

			lines = file.read().splitlines()

			for l,line in enumerate(lines):
				line = line.expandtabs(1)

				# if line == r"\\\ ".strip(): # raw string literals can't end in a backslash for some reason
				if line == "```":
					isComment ^= True
					continue
				if isComment or line == '': continue


				crate = Crate()


				crate.cargo = self
				crate.pack(line)


				# crate.__class__ = globals()[crate.inherit()] if crate.inherit() != crate.__class__ else crate.__class__
				crate.__class__ = crate.inherit(PrimitiveTags)
				crate.__init__()


				if line.count(' ') < parent_indentation:
					parent.pop()

				if len(parent) > 0:
					crate.parent = parent[-1]

				if line.count(' ') >= parent_indentation:
					parent += [crate]

				parent_indentation = line.count(' ')


				# prevLines = swap(lines[0:l])
				# # print("l",l, "line",lines[l], "prev",prevLines)
				# for p,previous_line in enumerate(prevLines):
				#     # print("prevLines:",prevLines)
				#     # print(self.freight)
				#     # print(prevLines[p])
				#     # print(l, p)
				#     # print()
				#     #print("sub",p)
				#     #if line.count("    ") == prevLines[p].count("    ")+1:
				#     if previous_line.count("    ") < line.count("    "):
				#         crate.parent = self.freight[l-p-1]
				#         #print("frg",self.freight)
				#         #print(crate.parent)
				#         break

				crate.pack(line)

				#crate = type('Crate',(Rect,), dict(Crate.__dict__))
				#Crate.__bases__ = (Rect,)
				#print(crate.pos)
				# crate.inherit()
				self.freight.append(crate)
		finally:
			file.close()


	# def assignParent(self):
	#     for idx in range(len(self.freight)):
	#         if self.freight[max(idx-1,0)].rank == self.freight[idx].rank - 1:
	#             self.freight[idx].parent = self.freight[max(idx-1,0)]


	def hook(self, path:str):
		pass
