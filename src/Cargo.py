from Node import Node

class Cargo(Node):
    """
    Node of type Cargo.
    Point to a freight file through their path arg.
    """

    def __init__(self, id:str=None, path=None, children:list=None):
        super().__init__(id,path,children)
        self.freight = []