
def inscribe(arg, cont):
	out = list(cont)
	for idx in range(len(arg)):
		out[idx] = arg[idx]
	return out


def rgba(arg):
	out = [0,0,0,0]
	if type(arg) == str:
		arg = inscribe(arg, "000000FF")
		# opaque black by default
		for i in range(len(out)):
			out[i] = int(arg[i*2] + arg[i*2+1],16)
			# get pairs of chrs and turn them into base 10 ints
	return out



