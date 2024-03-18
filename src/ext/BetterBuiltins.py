

class IAttributable:
	def __init__(self, dictionary:dict):
		for field,value in dictionary.items():
			exec(f"self.{field} = value")



class Unpackable(dict):
	"""
	Allows for multiple keys to be instanciated all at once,
	grouped together as a tuple, sharing a single value.
	"""
	
	def __init__(self, dictionary:dict) -> dict:
		
		super().__init__(dictionary)
		
		for key,value in dictionary.items():
			
			if type(key) is tuple:
				
				for k in key:
					print(k,value)
					# print(id(value),id(eval(f"{value}"))) # OH FFS FINALLY I GOT IT
					# avoid any pointer linkages, fresh instances only
					self[k] = type(value)(value)
				
				self.pop(key)
			

# from collections.abc import Iterable

class Array(list):
	def __init__(self, *values):
		if len(values)==1 and hasattr(values[0], '__iter__'):
			values = values[0]
		super().__init__(values)
		
	for dunder in {
		'add',
		'sub',
		'mul',
		'truediv',
		'floordiv',
		'round',
		'neg',
	}:
		exec("\n".join([
		f"def __{dunder}__(self, other=None):"
		f"	return Array(["
		f"		s.__{dunder}__(o) if o is not None else s.__{dunder}__()"
		f"		for s,o in zip(self, other if hasattr(other, '__iter__') else [other]*len(self) )"
		f"	])"
		]))
		
		if dunder in {'add','mul'}:
			exec(f"def __i{dunder}__(self, value): return self.__{dunder}__(value)")
		
		

