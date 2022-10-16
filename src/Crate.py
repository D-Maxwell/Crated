from Node import Node

class Crate(Node):
    """
    Node of type Crate.
    Crates are made of an id, a class, arguments, and children.
    These may all be individually omitted.
    """

    def __init__(self,tag:str=None,id:str=None,class_:str=None, attributes:list=None, children:list=None):

        super().__init__([tag,id,class_],attributes,children)
        delattr(self,"data")

        self.tag = tag
        self.id = id
        self.class_ = class_
        self.attributes = attributes
        #self.pos = pos
        #self.size = size

    def __repr__(self):
        output = ""
        if self.tag is not None: output += self.tag
        if self.id is not None: output += "#" + self.id
        if self.class_ is not None: output += "." + self.class_
        return output
        #return f"{self.tag}{'#' if self.id != (None or '') else ''}{self.id}{'.' if self.class_ != (None or '') else ''}{self.class_}"


    def pack(self, line):
        # the rank of a crate is determined by the amount of trailing spaces.
        rank = line.count(" ")

        keychars = []

        for idx in range(len(line)):
            # keychar found or BoL or arg
            if line[idx] in ['#','.','(',')'] or idx == rank or (line[idx] == ',' and line[:idx].count("[") == line[:idx].count("]")):
                keychars.append([idx, line[idx]])

        for idx in range(len(keychars)):
            #print(line[rank : keychars[idx+1][0]])
            if keychars[idx][0] == rank and keychars[idx][1] not in ['#','.','(']: self.tag = line[keychars[idx][0] : keychars[idx+1][0]]
            if keychars[idx][1] == '#': self.id = line[keychars[idx][0]+1 : keychars[idx+1][0]]
            if keychars[idx][1] == '.': self.class_ = line[keychars[idx][0]+1 : keychars[idx+1][0]]

            #if keychars[idx][1] in ['(',',']: self.attributes

        print(keychars)
