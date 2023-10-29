import json

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

        #super().__init__([tag,id,classes],attributes,children)
        super(Node, self).__init__()
        #super(Rect, self).__init__()
        #delattr(self,"data")

        self.rank = 0
        self.parent = None
        self.tag = []
        self.id = []
        self.classes = []
        self.attributes = {}
        #self.children = []

    def __repr__(self):
        return "".join([
            ",".join(self.tag),
            '#'*(len(self.id)>0) + '#'.join(self.id),
            '.'*(len(self.classes)>0) + '.'.join(self.classes),
        ])
        # output = ""
        # for tag in self.tag: output += tag + (',' if len(self.tag) > 1 else '')
        # for id in self.id: output += '#' + id
        # for class_ in self.classes: output += '.' + class_
        # return output
        #return f"{self.tag}{'#' if self.id != (None or '') else ''}{self.id}{'.' if self.classes != (None or '') else ''}{self.classes}"


    def pack(self, line:str):
        # line is already expanded

        #self.rank = line.count(" ") # the rank of a crate is determined by the amount of trailing spaces that precede it.
        self.rank = len(line) - len(line.lstrip())
        #print(f"{self.rank=} {line=} {len(line)=} {line.lstrip()} {len(line.lstrip())}")

        self.tag = [] # multiple tags are allowed for some reason
        self.id = [] # multiple ids too ... ?
        self.classes = [] # class_ ew
        self.attributes = {}

        #if self.id is None: self.id = []
        #if self.classes is None: self.classes = []

        sections:[""] = line.strip()[:-1].split('{', 1)
        sections = {["selector","attributes"][s] : section.strip() for s,section in enumerate(sections)}

        # this will defo get rewritten given how awful it is
        def multisplit(string:"", chars:[''], include_char:bool=False):
            # string.split(chars[0])
            # string.split(chars[1])

            out:dict = {char:[] for char in chars}

            c:int = 0
            for char in string:

                if c == len(string) - 1:
                    c += 1

                if char in chars or c == len(string):
                    if c == 0:
                        # out[chars[0]] += ['']
                        c += 1
                        continue

                    out[string[0]] += [string[1-include_char : c]]
                    string = string[c:]
                    c = 0

                c += 1

            return out

        # print(multisplit(
        #     "ab#main.hello#id#moreid.abc",
        #     ['#','.'],
        #     True,
        # ))


        sections["selector"] = multisplit(sections["selector"], [',','#','.'])
        self.tag, self.id, self.classes = sections["selector"].values()
        #print(f"{self.tag=}, {self.id=}, {self.classes=}")

        sections["attributes"] = list(map(
            lambda attribute: attribute.strip().rsplit(':', -1),
            sections["attributes"].split(';')
        ))
        sections["attributes"] = {field : json.loads(value) for value,field in sections["attributes"]}
        self.attributes = sections["attributes"]

        # sections["attributes"] = [section.strip() for section in sections["attributes"].split(';')]

        # print(sections)
        # print(self.rank)


        def old():
            keychars = []
            rank = self.rank

            for idx in range(len(line)):
                # keychar found or BoL or arg
                if line[idx] in ['#','.','(',')'] or idx == rank or (line[idx] == ',' and line[:idx].count("[") == line[:idx].count("]")):
                    keychars.append([idx, line[idx]])

            for idx in range(len(keychars)):
                #if idx != len(keychars)-1: print(line[keychars[idx][0] : keychars[idx+1][0]])
                if keychars[idx][0] == rank and keychars[idx][1] not in ['#','.','(']: self.tag.append(line[keychars[idx][0] : keychars[idx+1][0]])
                if keychars[idx][1] == '#': self.id.append(line[keychars[idx][0]+1 : keychars[idx+1][0]])
                if keychars[idx][1] == '.': self.classes.append(line[keychars[idx][0] + 1: keychars[idx + 1][0]])

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
        # old()



    def inherit(self, tags:{Node:['']}):
        # """Thanks to Socradeez#1059. Learning everyday.
        # I feel stupid this is so short and simple"""
        #Rect.__init__(self)

        # for tag in self.PrimitiveTags:
        #     if len(self.tag) == 0 or self.tag[0] in self.PrimitiveTags[tag]:
        #         #print(globals())
        #         return tag
        #print(self.__class__)

        if len(self.tag) == 0:
            self.tag += [''] # add empty tag for below loop to run once and assign default tag type

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
            if (tag is None or crate.tag == tag) and (id is None or crate.id == id) and (class_ is None or crate.classes == class_):
                out.append(crate)
        return out

# c = Crate()
# c.hook("#main")

