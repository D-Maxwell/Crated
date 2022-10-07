from Node import Node

class Crate(Node):
    """
    Node of type Crate.
    Crates are made of an id, a class, arguments, and children.
    These may all be individually omitted.
    """

    def __init__(self,tag:str=None,id:str=None,class_:str=None,pos:list=None,size:list=None,children:list=None):

        # data = [pos, size]
        # #for i in range(None in data):
        # while None in data:
        #     data.remove(None)

        #delattr(super(), super().data)
        super().__init__(id,children=children)
        delattr(self,"data")

        self.tag = tag
        self.id = id
        self.class_ = class_

        self.pos = pos
        self.size = size
        #print(vars(self))

    def __repr__(self):
        return f"{self.tag}{'#' if self.id != (None or '') else ''}{self.id}{'.' if self.class_ != (None or '') else ''}{self.class_}"


    def toRect(self):
        return [self.pos,self.size]
