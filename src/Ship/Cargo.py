from src.Ship import Crate
from src.ext.Console import log
from src.Ship.Node import Node
from src.Ship.Crate import Crate
from src.Ship.Tags.Rect import Rect

class Cargo(Node):
    """
    Node of type Cargo.
    Point to a freight file through their path arg.
    """

    def __init__(self, id:str=None, path=None, children:list=None):
        super().__init__(id,path,children)
        self.freight = []

    def load(self):
        try:
            file = open(self.data)
        except FileNotFoundError:
            log(f"File at path '{self.data}' could not be found. Make sure to include the '.frg' suffix, and check the scope.",
                type='ERROR')
        else:
            lines = file.read().splitlines()
            for idx in range(len(lines)):
                line = lines[idx]

                crate = Crate()


                crate.cargo = self
                crate.pack(line)


                crate.__class__ = globals()[crate.inherit()] if crate.inherit() != crate.__class__ else crate.__class__

                prevLines = lines[0:idx].swap()
                for subIdx in range(len(lines[0:idx])):
                    print(lines[0:idx][subIdx])
                    if line.count("    ") == lines[0:idx][subIdx].count("    ") - 1:
                        crate.parent = self.freight[idx-subIdx]

                crate.__init__()
                crate.pack(line)

                #crate = type('Crate',(Rect,), dict(Crate.__dict__))
                #Crate.__bases__ = (Rect,)
                #print(crate.pos)
                # crate.inherit()
                self.freight.append(crate)
        finally:
            file.close()


    # def assignParent(self):
    #     for idx in range(len(self.freight)):
    #         if self.freight[max(idx-1,0)].rank == self.freight[idx].rank - 1:
    #             self.freight[idx].parent = self.freight[max(idx-1,0)]


    def hook(self, path:str):
        pass
