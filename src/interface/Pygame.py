import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

from ext.BetterBuiltins import Array

from ship.Dock import Dock
from ship.containers.Rect import Rect


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


class PygameDock(Dock): # TODO : extend pygame.display ?
	
	def __init__(self, id:str=None ,data=None ,children:list=None):
		super().__init__(id,data,children)
		
		pygame.display.set_caption(self[self.selected_cargo].id)
		
		self.surface = pygame.display.set_mode(self[self.selected_cargo].dim,flags=pygame.RESIZABLE|pygame.SRCALPHA)#|pygame.NOFRAME)
	
	
	def embark(self, *cargo):
		super().embark(*cargo)
		
		for cargo in self.children:
			# cargo.sail()
			cargo.dim = Array(self.surface.get_size())
			cargo.surface = pygame.Surface(size=cargo.dim)
			
			for crate in cargo.freight:
				crate.sail()
				crate.surface = pygame.Surface(crate.dim).convert_alpha()
			
		
		self.sail()
		
	
	def sail(self):
		
		cargo = self[self.selected_cargo]
		cargo.dim = Array(self.surface.get_size())
		# cargo.sail()
		
		for crate in cargo.freight:
			
			if hasattr(crate, 'surface'):
				crate.surface = pygame.Surface(size=crate.outerDim())
			
			# if hasattr(crate, 'sail'):
			crate.sail()
				
			# if isinstance(crate, (source_container:=Rect)):
			if hasattr(crate, 'surface'):
				
				crate.surface.fill(rgba(crate.bg))
				
				cargo.surface.blit(crate.surface,crate.outerPos())
				
				
		self.surface.blit(self[self.selected_cargo].surface, [0,0])
	
	
	def goto(self, cargo_id):
		super().goto(cargo_id)
		pygame.display.set_caption(self[self.selected_cargo].id)
		#print(cargo.id, cargo.surface)

