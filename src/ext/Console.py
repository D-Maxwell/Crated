
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
	strings:str = ""
	for i in range(len(args)):
		strings += args[i]
	output = ""
	if bg is not None: output += f"\033[48:2:{bg[0]}:{bg[1]}:{bg[2]}m"
	if type is not None: output += f"\033[38:2:{logTypes[type][0]}:{logTypes[type][1]}:{logTypes[type][2]}m" + f"[{type}] "
	output += f"\033[0m"
	if bg is not None: output += f"\033[48:2:{bg[0]}:{bg[1]}:{bg[2]}m"
	if clr is not None: output += f"\033[38:2:{clr[0]}:{clr[1]}:{clr[2]}m"

	output += strings
	print(output, sep='')


#log("File not found", type="ERROR")