from Node import Node
from Crate import Crate


# Contains all pages
cargo = Node("root","",[
    # Nodes contain the path to a freight file (called a dock, contains freight) in their data
    Node("index","freight01.frg")
])

#a = Crate("hey","datsaclass",pos=[25,78],size=[16,16])

def ship(node:Node):

    dock = []

    try:
        file = open(node.data)
        text = file.read().splitlines()

        id = ""
        data = {}
        children = []


        for line in range(len(text)):

            id = ""
            data = {}
            children = []

            for idx in range(len(text[line])):

                indent:int = text[line].count("    ")
                #arg, val = "", ""
                #data_idx:int = 0

                if id == "" or id is None:
                    if text[line][idx] == '(':
                        id = text[line][indent*4 : idx]
                        data_idx = idx + 1
                        print('/','>'*indent, id, sep='')
                else:
                    #arg, val = "",""
                    if text[line][idx] == '=':
                        arg = text[line][data_idx : idx]
                        #print(arg)
                        data_idx = idx + 1
                    # equal amount of brackets not to catch unwanted commas
                    if text[line][idx] in [',',')'] and text[line][0 : idx].count('[') == text[line][0 : idx].count(']'):
                        val = text[line][data_idx : idx]
                        #print(val)
                        data_idx = idx + 1
                        data[arg] = val
                        #print(arg, data)
                        arg, val = "", ""
                    # if text[line][idx] == ')' and text[line][0 : idx].count('[') == text[line][0 : idx].count(']'):
                    #     data[arg] = val
                    #     print(data)

                # reached End of Line
                if idx == len(text[line])-1:
                    #print("new crate!")
                    Crate(id,class_=data.get("class"),pos=data.get("pos"),size=data.get("size"),children=children)

                # # from idx to end of line
                # for text[line][idx : len(text[line]) - idx]:
                #     pass


            # Crate(id,class_=data.get("class"),pos=data.get("pos"),size=data.get("size"),children=children)

    finally:
        file.close()

    return dock


# ~~iters !!!~~
# getitems!!!
print(ship(cargo["index"]))