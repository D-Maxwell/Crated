import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

from ext.BetterBuiltins import Array, A

from ship.Dock import Dock
from ship.Cargo import Cargo
from ship.Crate import Crate





class PygameDock(Dock): # TODO : extend pygame.display ?
	
	def __init__(self, children:list=None):
		super().__init__(children)
		
		pygame.display.set_caption(self[self.focus].id)
		
		self.surface = pygame.display.set_mode(A[1280,720], flags=pygame.RESIZABLE|pygame.SRCALPHA)#|pygame.NOFRAME) # TODO : query screen resolution ?
		
		pygame.init()
	
	
	def embark(self):
		super().embark()
		
		for cargo in self.children:
			# cargo.sail()
			cargo.dim = A[self.surface.get_size()]
			cargo.surface = pygame.Surface(size=cargo.dim)
			
			for crate in cargo:
				# crate.surface = pygame.Surface(crate.dim).convert_alpha()
				crate.embark()
			
		
		self.sail()
		
	
	def sail(self):
		
		cargo:Cargo = self[self.focus]
		cargo.dim = A[self.surface.get_size()]
		
		for crate in cargo.children:
			crate.sail()
			
		self.surface.blit(cargo.surface, [0,0])
		# self.surface = cargo.surface
		
		pygame.display.update()
		
		
		if pygame.event.get(pygame.QUIT):
			self.ungated = False
			pygame.quit()
			# self.__delete__(self)
		
	
	
	def goto(self, cargo_id):
		super().steer(cargo_id)
		pygame.display.set_caption(self[self.focus].id)
		#print(cargo.id, cargo.surface)
	
	
	
	# def __delete__(self, instance):
	# 	print("quit ???")
	# 	pygame.quit()
	# 	del instance

