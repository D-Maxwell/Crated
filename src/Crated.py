from Node import Node
from Cargo import Cargo
from Crate import Crate


# Contains all pages
dock = Node("root","",[
    Cargo("index", "freight01.frg")
])



def ship(node:Cargo):

    cargo = []

    try:
        file = open(node.data)
        text = file.read().splitlines()

        for line in range(len(text)):

            tag = None
            id = ""
            class_ = ""
            data = {}
            children = []

            marker:int = 0
            # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            #  tag#thisisquitealongid.andthisisaclass(pos=[0,24]) #
            # ----|------------------|--------------------------- #
            #     ^                  ^            _________       #
            #   marker              idx           | -> id |       #
            # # # # # # # # # # # # # # # # # # # # # # # # # # # #

            for idx in range(len(text[line])):


                indent:int = text[line].count(" " * 4) # amount of spaces required, will be dynamic soon enough


                #v# "rollback" search # to be done dynamically (dicts, strings as var pointers, ...)

                if marker == 0 and text[line][idx] in ['#','.','(']:
                    tag = text[line][indent*4 + marker : idx]
                    print("tag:",tag)
                if text[line][marker] == '#' and text[line][idx] in ['.','(']:
                    id = text[line][indent*4 + marker + 1 : idx]
                    print("id",id)
                if text[line][marker] == '.' and text[line][idx] == '(':
                    class_ = text[line][indent*4 + marker + 1 : idx]
                    print("class",class_)


                #v# set marker onto any special character

                if idx == 0 or text[line][idx] == '#' or text[line][idx] == '.' or text[line][idx] == '(':
                    marker = idx
                print(idx,marker)




                # if text[line][idx] in ['#','.','(']:
                #     if (tag == "" or tag is None) and text[line][idx] == '#':
                #         tag = text[line][indent*4+marker : idx]
                #     if (id == "" or id is None) and text[line][idx] == '.':
                #         id = text[line][indent*4+marker : idx]
                #         print(tag, idx, text[line][idx])
                #     if (class_ == "" or class_ is None) and text[line][idx] == '(':
                #         class_ = text[line][indent*4+marker : idx]

                #marker = 0 if (tag == "" or tag is None) else idx if text[line][idx] in ['#','.'] else None
                # marker = idx if text[line][idx] in ['#','.'] else marker


                # if id == "" or id is None:
                #     if text[line][idx] == '#':
                #         marker = idx
                #     if text[line][idx] == '(':
                #         id = text[line][indent*4+marker : idx]
                #         data_idx = idx + 1
                #         print('/','>'*indent, id, sep='')
                #         marker = None
                # else:
                #     if text[line][idx] == '=':
                #         arg = text[line][data_idx : idx]
                #         data_idx = idx + 1
                #
                #     # equal amount of brackets not to catch unwanted commas
                #     if text[line][idx] in [',',')'] and text[line][0 : idx].count('[') == text[line][0 : idx].count(']'):
                #         val = text[line][data_idx : idx]
                #         data_idx = idx + 1
                #         data[arg] = val
                #         arg, val = "", ""

                # reached End of Line
                if idx == len(text[line])-1:
                    cargo.append(Crate(tag,id,class_,pos=data.get("pos"),size=data.get("size"),children=children))

    finally:
        file.close()
        return cargo


# ~~iters !!!~~
# getitems!!!
print(ship(dock["index"]))