# from ext.BetterBuiltins import Array, A # no global imports, what is this
from interface.Pygame import PygameDock
from ship.Cargo import Cargo
from ext.LoftyLogger import log


# def hook(self, path:str):
#     for idx in range(len(path)):
#         pass



# Contains all pages
# dock = PygameDock([
# 	# Cargo("index", "Freight/freight01.frg"),
# 	# Cargo("something", "Freight/freight02.frg"),
# 	# Cargo("MODERN", "freight/modern_freight.frg"),
# 	Cargo("TODO", "freight/todo.frg"),
# ])




# dock.embark()



# TODO: move mainloop to pygame interface probably or have a single call that maps to whichever interface is used
# might wanna rename interface directory to render(er) ?
# import pygame as pg


# import win32gui
# import win32.lib.win32con as win32con
# import win32.win32api as win32api
# win32gui.SetWindowLong(pg.display.get_wm_info()['window'], win32con.GWL_EXSTYLE, win32gui.GetWindowLong(pg.display.get_wm_info()['window'], win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# win32gui.SetLayeredWindowAttributes(pg.display.get_wm_info()['window'], win32api.RGB(*[0,0,0]), 0, win32con.LWA_COLORKEY)




#RUNNING:bool = False
#while RUNNING:
#	
#	try:
#		
#		# if pg.event.get(pg.VIDEORESIZE):
#			# dock.embark()
#		
#		dock.sail()
#		
#		pg.display.update()
#		
#		
#		
#		if pg.event.get(pg.QUIT):
#			RUNNING = False
#		
#	except KeyboardInterrupt:
#		RUNNING = False
		
	
# pg.quit()





