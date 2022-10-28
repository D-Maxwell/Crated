import pygame
from src.Ship.Dock import Dock



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
            # i = 0
            # arg[0] u arg[1]
            #
            # i = 1
            # arg[2] u arg[3]
            #
            # i = 2
            # arg[4] u arg[5]
            #
            # i = 3
            # arg[6] u arg[7]
            out[i] = int(arg[i*2] + arg[i*2+1],16)
            # get pairs of chrs and turn them into base 10 ints
    return out

#print(rgba("2897D6"))

class PygameDock(Dock):
    def __init__(self,id:str=None,data=None,children:list=None):
        super().__init__(id,data,children)
        self.surface = pygame.display.set_mode((1280,720))
    def ship(self, *cargo):
        super().ship(*cargo)
        for cargo in self.children:
            cargo.surface = pygame.Surface(size=self.surface.get_size())
            for crate in cargo.freight:
                #print(crate.PrimitiveTags.values())
                #print(crate.tag)
                if crate.tag == [] or crate.tag[0] in crate.PrimitiveTags["Rect"]:
                    #print(crate.tag[0] in crate.PrimitiveTags.values())
                    #print(crate.pos[0],crate.size)
                    #print(int(0x00))
                    #print(int(0x0 + int(crate.bg[0:2])))
                    #print(crate.pos[0])
                    pygame.draw.rect(cargo.surface,rgba(crate.bg),(crate.pos[0],crate.pos[1],crate.size[0],crate.size[1]))

    def goto(self, cargo):
        #print(cargo.id, cargo.surface)
        pygame.Surface.blit(self.surface, cargo.surface, [0,0])

