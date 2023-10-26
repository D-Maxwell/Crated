from src.Ship.Node import Node



from src.Ship.Tags.Rect import Rect

PrimitiveTags = {
    Rect : ["rect","Rect",""] # tag will never contain an empty string, thus last element serves no purpose
}



class Dock(Node):
    def __init__(self, id:str=None, data=None, children:list=None):
        super().__init__(id,data,children)

    def ship(self, *cargo):
        for cargo in self.children:
            cargo.load()
