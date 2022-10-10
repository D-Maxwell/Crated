from Console import log
from Node import Node
from Cargo import Cargo
from Crate import Crate


# Contains all pages
dock = Node("root","",[
    Cargo("index", "freight01.frg")
])



def ship(node:Cargo):

    cargo = []
    break_chrs = ['#','.','']

    try:
        file = open(node.data)
        text = file.read().splitlines()

        for line in range(len(text)):

            tag = ""
            id = ""
            class_ = ""
            data = {}
            children = []

            marker:int = 0
            marker_arg:int = 0
            # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            #  tag#thisisquitealongid.andthisisaclass(pos=[0,24]) #
            # ----|------------------|--------------------------- #
            #     ^                  ^            _________       #
            #   marker              idx           | -> id |       #
            # # # # # # # # # # # # # # # # # # # # # # # # # # # #

            indent:int = text[line].count(" " * 4) # amount of spaces required, will be dynamic soon enough

            for idx in range(len(text[line])):

                #v# "rollback" search # to be done dynamically (dicts, strings as var pointers, ...)

                if marker == indent*4 and text[line][marker] not in ['#','.','('] and text[line][idx] in ['#','.','(']:
                    tag = text[line][marker : idx]

                if text[line][marker] == '#' and text[line][idx] in ['#','.','(']:
                    id = text[line][marker + 1 : idx]

                if text[line][marker] == '.' and text[line][idx] in ['#','.','(']:
                    class_ = text[line][marker + 1 : idx]

                if text[line][marker] in ['(',','] and text[line][idx] in [',',')']:
                    if marker_arg == 0: marker_arg = marker
                    data[text[line][marker + 1 : marker_arg]] = text[line][marker_arg + 1 : idx]
                    #print(marker, marker_arg)




                # if text[line][marker] == '(' and text[line][idx] == ',':



                #v# set marker onto any special character

                if idx == indent*4 or text[line][idx] in ['#','.','('] or (text[line][idx] == ',' and text[line][0 : idx].count('[') == text[line][0 : idx].count(']')):
                    marker = idx
                    #print("m '",marker, "' idx '",idx, "' line '", line, "'", sep='')

                if text[line][idx] == '=':
                    marker_arg = idx

                # arg, val = "", ""
                # if text[line][idx] == '=':
                #     arg = text[line][marker : idx]
                #     #data_idx = idx + 1
                #
                # # equal amount of brackets not to catch unwanted commas
                # if text[line][idx] in [',',')'] and text[line][0 : idx].count('[') == text[line][0 : idx].count(']'):
                #     val = text[line][marker_arg : idx]
                #     #data_idx = idx + 1
                #     data[arg] = val
                #     arg, val = "", ""

                # if text[line][idx] in ['#','.','(']:
                #     if (tag == "" or tag is None) and text[line][idx] == '#':
                #         tag = text[line][indent*4+marker : idx]
                #     if (id == "" or id is None) and text[line][idx] == '.':
                #         id = text[line][indent*4+marker : idx]
                #         print(tag, idx, text[line][idx])
                #     if (class_ == "" or class_ is None) and text[line][idx] == '(':
                #         class_ = text[line][indent*4+marker : idx]
                #
                # marker = 0 if (tag == "" or tag is None) else idx if text[line][idx] in ['#','.'] else None
                # marker = idx if text[line][idx] in ['#','.'] else marker
                #
                #
                # if id == "" or id is None:
                #     if text[line][idx] == '#':
                #         marker = idx
                #     if text[line][idx] == '(':
                #         id = text[line][indent*4+marker : idx]
                #         data_idx = idx + 1
                #         print('/','>'*indent, id, sep='')
                #         marker = None
                # else:


                # reached End of Line

                if idx == len(text[line])-1:
                    cargo.append(Crate(tag,id,class_,pos=data.get("pos"),size=data.get("size"),children=children))
                    print("tag",tag,"id",id,"class",class_,"data",data)

    except FileNotFoundError:
        log('ERROR', "[ERROR] ", "File at path '", node.data, "' could not be found. Make sure to include the '.frg' suffix, and check the scope.")
    else:
        file.close()
    finally:
        return cargo


# ~~iters !!!~~
# getitems!!!
print(ship(dock["index"]))