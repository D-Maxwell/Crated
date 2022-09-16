from Node import Node

class Crate(Node):
    """
    Crates are made of an id, (an optional class), arguments, and children.
    Here, data will host our arguments.
    """

    def __init__(self,id:str=None,class_:str=None,pos:list=None,size:list=None,children:list=None):

        # data = [pos, size]
        # #for i in range(None in data):
        # while None in data:
        #     data.remove(None)

        #delattr(super(), super().data)
        super().__init__(id,children=children)
        delattr(self,"data")

        self.class_ = class_
        self.pos = pos
        self.size = size
        print(vars(self))

    def toRect(self):
        return [self.pos,self.size]
