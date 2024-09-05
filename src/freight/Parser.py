
from ext.LoftyLogger import log
from ship.Crate import Crate


def parseFreight(filepath:str) -> [Crate]:
	try:
		file = open(filepath)
	except FileNotFoundError:
		log(f"File at path '{filepath}' could not be found. Make sure to include the '.frg' suffix, and check the scope.",
			type='ERROR')
		raise FileNotFoundError
	
	is_comment:bool = False
	
	root:Crate = Crate()
	
	parent_indentation:int = 0
	parent = root
	
	lines:[str] = file.read().splitlines()
	
	for l,line in enumerate(lines):
		# if line == r"\\\ ".strip(): # raw string literals can't end in a backslash for some reason
		if line == "```":
			is_comment ^= True
			continue
		if is_comment or line == '': continue
		
		
		line:str = line.lstrip('\t')
		indentation:int = len(lines[l]) - len(line)
		# print(f"{indentation=} {parent_indentation=}")
		
		
		
		crate = Crate()
		
		# crate = inherit(, PrimitiveTags)() # temp Crate instance, TODO : make inherit a function not a method
		
		
		# crate.pack(line)
		
		
		# crate.__class__ = globals()[crate.inherit()] if crate.inherit() != crate.__class__ else crate.__class__
		# crate.__class__ = crate.inherit(PrimitiveTags)
		# crate.__init__()
		
		
		if indentation < parent_indentation:
			# parent.pop() # getting parent of current parent would remove the need for a stack
			parent = parent.parent # make what you will of this
		
		
		crate.parent = parent
		
		
		crate.pack(line) # TODO : pull from Crate#pack to Parser::parseFreight
		
		parent.children += [crate]
		
		print(f"{crate.parent=} {parent.children=}")
		print()
		
		
		if indentation >= parent_indentation:
			parent = crate
		
		parent_indentation = indentation
		
		
	file.close()
	
	return root



