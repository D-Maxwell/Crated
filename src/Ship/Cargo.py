from src.Ship import Crate
from src.ext.Console import log
from src.Ship.Node import Node
from src.Ship.Crate import Crate


def swap(arg:list):
    out = []
    for idx in range(len(arg)):
        e = arg[idx]
        out.append(arg[-1 - idx])
    return out


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
                crate.__init__()

                prevLines = swap(lines[0:idx])
                print("idx",idx, "line",lines[idx], "prev",prevLines)
                for subIdx in range(len(prevLines)):
                    # print("prevLines:",prevLines)
                    # print(self.freight)
                    # print(prevLines[subIdx])
                    # print(idx, subIdx)
                    # print()
                    #print("sub",subIdx)
                    #if line.count("    ") == prevLines[subIdx].count("    ")+1:
                    if prevLines[subIdx].count("    ") < line.count("    "):
                        #print("frg",self.freight)
                        crate.parent = self.freight[idx-subIdx-1]
                        #print(crate.parent)
                        break

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
