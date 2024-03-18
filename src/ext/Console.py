import os     # hacky workaround,
os.system('') # may fix escape sequences being ignored in some older NT versions


## TODO : rewrite this as a class where each Log call (!=log) is stored within the class (upon calling the constructor several times, acts as dedicated method as well)
## 		  would store logTypes as well, perhaps as constants (class could also be an Enum perhaps ?)
## 		  this would allow for bulk printing --potentially more efficient--, data logging to disk (easier at the very least), and dynamic tty refresh ('\r' shenanigans)



logTypes = {
	'ERROR' : [255,0,0],
	'WARN' : [255,165,0],
	'INFO' : [255,255,0]
}


def log(*args, type:str=None, clr:list=None, bg:list=None):
	"""
	A function to write logs to the console, concisely and in colors !
	:param type: ERROR,WARN
	:param clr: decimal rgb ANSI text color
	:param bg: decimal rgb ANSI background color
	:param args: Any amount of strings
	:return: Dual color console line
	"""
	
	output = ""
	
	if bg is not None: output += f"\033[48;2;{';'.join(map(str,bg))}m"
	if type is not None: output += f"\033[38;2;{';'.join(map(str,logTypes[type]))}m" + f"[{type}] "
	
	output += f"\033[0m"
	
	if bg is not None: output += f"\033[48;2;{';'.join(map(str,bg))}m"
	if clr is not None: output += f"\033[38;2;{';'.join(map(str,clr))}m"
	
	output += "".join(map(str,args))
	print(output, sep='')


#log("File not found", type="ERROR")