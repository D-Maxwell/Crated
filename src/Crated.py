from interface.Pygame import PygameDock
from ship.Cargo import Cargo
from ext.Console import log

# def hook(self, path:str):
#     for idx in range(len(path)):
#         pass



# Contains all pages
dock = PygameDock("root","",[
	# Cargo("index", "Freight/freight01.frg"),
	# Cargo("something", "Freight/freight02.frg"),
	Cargo("MODERN", "freight/modern_freight.frg"),
	Cargo("TODO", "freight/todo.frg"),
])



# def embark(node:Cargo):
#
#     #cargo = []
#     keychars = ['#','.','']
#
#     try:
#         file = open(node.data)
#         text = file.read().splitlines()
#
#         for line in range(len(text)):
#
#             tag = ""
#             id = ""
#             classes = ""
#             data = {}
#             children = []
#
#             marker:int = 0
#             marker_arg:int = 0
#             # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#             #  tag#thisisquitealongid.andthisisaclass(pos=[0,24]) #
#             # ----|------------------|--------------------------- #
#             #     ^                  ^            _________       #
#             #   marker              idx           | -> id |       #
#             # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#             indent:int = text[line].count(" " * 4) # amount of spaces required, will be dynamic soon enough
#
#             for idx in range(len(text[line])):
#
#                 #v# "rollback" search # to be done dynamically (dicts, strings as var pointers, ...)
#
#                 if marker == indent*4 and text[line][marker] not in ['#','.','('] and text[line][idx] in ['#','.','(']:
#                     tag = text[line][marker : idx]
#
#                 if text[line][marker] == '#' and text[line][idx] in ['#','.','(']:
#                     id = text[line][marker + 1 : idx]
#
#                 if text[line][marker] == '.' and text[line][idx] in ['#','.','(']:
#                     classes = text[line][marker + 1 : idx]
#
#                 if text[line][marker] in ['(',','] and text[line][idx] in [',',')']:
#                     if marker_arg == 0: marker_arg = marker
#                     data[text[line][marker + 1 : marker_arg]] = text[line][marker_arg + 1 : idx]
#
#
#                 #v# set marker onto any special character
#
#                 if idx == indent*4 or text[line][idx] in ['#','.','('] or (text[line][idx] == ',' and text[line][0 : idx].count('[') == text[line][0 : idx].count(']')):
#                     marker = idx
#                     #print("m '",marker, "' idx '",idx, "' line '", line, "'", sep='')
#
#                 if text[line][idx] == '=':
#                     marker_arg = idx
#
#
#                 #v# reached End of Line
#
#                 if idx == len(text[line])-1:
#                     node.freight.append(Crate(tag,id,classes,pos=data.get("pos"),dim=data.get("dim"),children=children))
#                     print("tag",tag,"id",id,"class",classes,"data",data)
#
#     except FileNotFoundError:
#         log(f"File at path '{node.data}' could not be found. Make sure to include the '.frg' suffix, and check the scope.",
#             type='ERROR')
#     else:
#         file.close()
#     finally:
#         return cargo


#ship(dock["index"])
dock.embark()
dock.goto('TODO')
for crate in dock[dock.selected_cargo].freight:
	tab = '\t' # can't have shit in fstrings
	log(f"{crate.rank*tab}{crate} {crate.attributes}",
		type='INFO')



# TODO: move mainloop to pygame interface probably or have a single call that maps to whichever interface is used
# might wanna rename interface directory to renderer ?
import pygame as pg

pg.init()

# import win32gui
# import win32.lib.win32con as win32con
# import win32.win32api as win32api
# win32gui.SetWindowLong(pg.display.get_wm_info()['window'], win32con.GWL_EXSTYLE, win32gui.GetWindowLong(pg.display.get_wm_info()['window'], win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# win32gui.SetLayeredWindowAttributes(pg.display.get_wm_info()['window'], win32api.RGB(*[0,0,0]), 0, win32con.LWA_COLORKEY)


RUNNING:bool = True
while RUNNING:
	
	try:
		
		# if pg.event.get(pg.VIDEORESIZE):
		# 	dock.embark()
		
		dock.sail()
		
		pg.display.update()
		
		
		
		if pg.event.get(pg.QUIT):
			RUNNING = False
		
	except KeyboardInterrupt:
		RUNNING = False
		
	
pg.quit()





