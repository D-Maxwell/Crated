import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

from Ship.Dock import Dock
from Ship.Tags.Rect import Rect


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

#print(rgba("2897D6"))


class PygameDock(Dock):
	
	def __init__(self,id:str=None,data=None,children:list=None):
		super().__init__(id,data,children)
		
		pygame.display.set_caption(self[self.selected_cargo].id)
		
		self.surface = pygame.display.set_mode(self[self.selected_cargo].dim,flags=pygame.RESIZABLE)#|pygame.NOFRAME)
	
	
	def ship(self, *cargo):
		super().ship(*cargo)
		
		for cargo in self.children:
			cargo.surface = pygame.Surface(size=self.surface.get_size())
			for crate in cargo.freight:
				
				if isinstance(crate, Rect):
					
					crate_surface = pygame.Surface(crate.dim).convert_alpha()
					crate_surface.fill(rgba(crate.bg))
					
					cargo.surface.blit(crate_surface,crate.pos)
					


	def goto(self, cargo_id):
		super().goto(cargo_id)
		pygame.display.set_caption(self[self.selected_cargo].id)
		#print(cargo.id, cargo.surface)
		pygame.Surface.blit(self.surface, self[self.selected_cargo].surface, [0,0])

