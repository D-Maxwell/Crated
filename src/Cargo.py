from Console import log
from Node import Node
from Crate import Crate

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
            for line in file.read().splitlines():
                crate = Crate()
                crate.pack(line)
                self.freight.append(crate)
        finally:
            file.close()
