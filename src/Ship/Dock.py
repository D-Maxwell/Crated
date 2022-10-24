from src.Ship.Node import Node

class Dock(Node):
    def __init__(self,id:str=None,data=None,children:list=None):
        super().__init__(id,data,children)

    def ship(self):
        for cargo in self.children:
            cargo.load()