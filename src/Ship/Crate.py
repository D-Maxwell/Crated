from src.Ship.Node import Node


# Tags = {
#     ['','rect'] : 'Rect',
#     ['txt','text'] : 'Text'
# }

#tag = Rect


class Crate(Node):
    """
    Node of type Crate.
    Crates are made of an id, a class, arguments, and children.
    These may all be individually omitted.
    """

    def __init__(self):

        #super().__init__([tag,id,class_],attributes,children)
        super(Node, self).__init__()
        #super(Rect, self).__init__()
        #delattr(self,"data")

        self.rank = 0
        self.parent = None
        self.tag = []
        self.id = []
        self.class_ = []
        self.attributes = {}
        #self.children = []

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
                    # out = []
                    # key = line[keychars[idx][0]+1 : equal]
                    # for subIdx in range(len(self.attributes[key])):
                    #     if self.attributes[key][subIdx] == '[':
                    #         out.append([])
                        # elif self.attributes[key][subIdx] in ["'",'"']:
                        #     marker = subIdx
                        #     while self.attributes[key][subIdx] not in ["'",'"'] and marker != subIdx:



        #print(keychars)

    def inherit(self, tags:{Node:['']}):
        # """Thanks to Socradeez#1059. Learning everyday.
        # I feel stupid this is so short and simple"""
        #Rect.__init__(self)

        # for tag in self.PrimitiveTags:
        #     if len(self.tag) == 0 or self.tag[0] in self.PrimitiveTags[tag]:
        #         #print(globals())
        #         return tag
        #print(self.__class__)

        print(f"{self.tag=}")

        if len(self.tag) == 0:
            self.tag += [''] # add empty tag for below loop to run once and assign default tag type
            # return self.__class__

        for tag,aliases in tags.items():
            if self.tag[0] in aliases: # I've allowed multiple tags for some reason
                return tag

        return self.__class__
                # print(i)
                # print(globals())
                # globals()[i].__init__(self)
                #self = globals()[i]
                # for attr in self.attributes:
                #     if attr in globals()[i].__dict__:
                #         vars(self)[attr] = self.attributes[attr]
                # #print(vars(globals()[i]))
                # print(self.pos)


    def hook(self, path:str):

        tag = id = class_ = None

        # deconstruct path
        for idx in range(len(path)):
            marker = idx
            if path[idx] in ['#','.','(']:
                if marker == 0:
                    tag = path[marker:idx]
                if path[marker] == '#':
                    id = path[marker:idx]
                if path[marker] == '.':
                    class_ = path[marker:idx]
            #while path[idx] not in ['#','.','(',')']:

        print(tag,id,class_)
        # find matching crate
        out = []
        for crate in self.cargo.freight:
            if (tag is None or crate.tag == tag) and (id is None or crate.id == id) and (class_ is None or crate.class_ == class_):
                out.append(crate)
        return out

# c = Crate()
# c.hook("#main")

