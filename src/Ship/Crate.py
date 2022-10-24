from src.Ship.Node import Node
from src.Ship.Tags.Rect import Rect

# Tags = {
#     ['','rect'] : 'Rect',
#     ['txt','text'] : 'Text'
# }

tag = Rect

class Crate(Node,Rect):
    """
    Node of type Crate.
    Crates are made of an id, a class, arguments, and children.
    These may all be individually omitted.
    """

    def __init__(self):

        #super().__init__([tag,id,class_],attributes,children)
        super(Node, self).__init__()
        super(Rect, self).__init__()
        #delattr(self,"data")

        self.rank = 0
        self.tag = []
        self.id = []
        self.class_ = []
        self.attributes = {}
        self.children = []

    def __repr__(self):
        output = ""
        for tag in self.tag: output += tag + (',' if len(self.tag) > 1 else '')
        for id in self.id: output += '#' + id
        for class_ in self.class_: output += '.' + class_
        return output
        #return f"{self.tag}{'#' if self.id != (None or '') else ''}{self.id}{'.' if self.class_ != (None or '') else ''}{self.class_}"


    def pack(self, line):
        # the rank of a crate is determined by the amount of trailing spaces.
        self.rank = rank = line.count(" ")

        keychars = []
        self.tag = []
        self.id = []
        self.class_ = []
        self.attributes = {}

        #if self.id is None: self.id = []
        #if self.class_ is None: self.class_ = []

        for idx in range(len(line)):
            # keychar found or BoL or arg
            if line[idx] in ['#','.','(',')'] or idx == rank or (line[idx] == ',' and line[:idx].count("[") == line[:idx].count("]")):
                keychars.append([idx, line[idx]])

        for idx in range(len(keychars)):
            #if idx != len(keychars)-1: print(line[keychars[idx][0] : keychars[idx+1][0]])
            if keychars[idx][0] == rank and keychars[idx][1] not in ['#','.','(']: self.tag.append(line[keychars[idx][0] : keychars[idx+1][0]])
            if keychars[idx][1] == '#': self.id.append(line[keychars[idx][0]+1 : keychars[idx+1][0]])
            if keychars[idx][1] == '.': self.class_.append(line[keychars[idx][0]+1 : keychars[idx+1][0]])

            if keychars[idx][1] in ['(',',']:
                hasArgs = False
                for i in keychars:
                    if i[1] == ',':
                        hasArgs = True
                if hasArgs:
                    #self.attributes[line[keychars[idx][0] : str(line[keychars[idx][0] : keychars[idx+1][0]]).find("=")]] = line[str(line[keychars[idx][0] : keychars[idx+1][0]]).find("=") : keychars[idx+1][0]]
                    equal = keychars[idx][0] + str(line[keychars[idx][0] : keychars[idx+1][0]]).find('=')
                    self.attributes[line[keychars[idx][0]+1 : equal]] = line[equal+1 : keychars[idx+1][0]]

        #print(keychars)
