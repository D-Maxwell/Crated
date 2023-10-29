from Pygame.Interface import PygameDock
from Ship.Cargo import Cargo
from ext.Console import log

# def hook(self, path:str):
#     for idx in range(len(path)):
#         pass



# Contains all pages
dock = PygameDock("root","",[
	# Cargo("index", "Freight/freight01.frg"),
	# Cargo("something", "Freight/freight02.frg")
	Cargo("modern", "Freight/modern_freight.frg"),
])



# def ship(node:Cargo):
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
#                     node.freight.append(Crate(tag,id,classes,pos=data.get("pos"),size=data.get("size"),children=children))
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
dock.ship()
dock.goto("modern")
for crate in dock[dock.selected_cargo].freight:
	log(f"{crate.rank*'> '}{crate} {crate.attributes}",
		type='INFO')



import pygame as pg

pg.init()

RUNNING:bool = True
while RUNNING:

	pg.display.update()

	if pg.event.get(pg.QUIT):
		RUNNING = False
		pg.quit()





