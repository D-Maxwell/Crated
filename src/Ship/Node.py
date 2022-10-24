class Node(object):

    """
    Nodes are made of an id, data, and children. These may all be invidivually omitted.
    """

    # Nodes with no data are folders
    def __init__(self,id=None,data=None,children:list=None):
        self.id = id
        self.data = data
        self.children = children

    # def __iter__(self):
    #     self.iter = 0
    #     return self
    #
    # def __next__(self):
    #     if self.iter <= len(self.children):
    #         self.iter += 1
    #         return self.children[self.iter]

    def __getitem__(self, item):
        # print(self.children[item])
        if type(item) == str:
            for e in self.children:
                if item == e.id:
                    return e
        # if item is int:
        #     return self.children[item]
        if type(item) == int:
            return self.children[item]
