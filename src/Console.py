
# colors = {
#     'BLACK' : '30m',
#     'RED' : '31m',
#     'GREEN' : '32m',
#     'YELLOW' : '33m',
#     'BLUE' : '34m',
#     'MAGENTA' : '35m',
#     'CYAN' : '36m',
#     'WHITE' : '37m'
# }
# logTypes = {
#     'ERROR' : colors["RED"],
#     'WARN' : colors["YELLOW"]
#     #'INFO' : colors["ORANGE"]
# }
logTypes = {
    'ERROR' : [255,0,0],
    'WARN' : [255,165,0]
}


def log(*args, type:str=None, clr:list=None, bg:list=None):
    """


    :param type: ERROR,WARN
    :param clr: decimal rgb ANSI text color
    :param bg: decimal rgb ANSI background color
    :param args: Any amount of strings
    :return: Dual color console line
    """
    strings:str = ""
    for i in range(len(args)):
        strings += args[i]
    #print(, sep='')


    # 48;2 = bg clr
    # 38;2 = txt clr
    #print("\033[38:2:255:00:00m", strings)
    output = ""
    if bg is not None: output += f"\033[48:2:{bg[0]}:{bg[1]}:{bg[2]}m"
    if type is not None: output += f"\033[38:2:{logTypes[type][0]}:{logTypes[type][1]}:{logTypes[type][2]}m" + f"[{type}] "
    # if clr is not None:
    #     if bg is not None:
    #         output += f"\033[38:2:{max(0,min(255,bg[0] - clr[0]))}:{max(0,min(255,bg[1] - clr[1]))}:{max(0,min(255,bg[2] - clr[2]))}m"
    #         print(bg[2] - clr[2])
    #     else:
    #         output += f"\033[38:2:{clr[0]}:{clr[1]}:{clr[2]}m"
    # else:
    #     output += f"\033[0m" + f"\033[48:2:{bg[0]}:{bg[1]}:{bg[2]}m"
    output += f"\033[38:2:{clr[0]}:{clr[1]}:{clr[2]}m" if clr is not None else "\033[0m" + f"\033[48:2:{bg[0]}:{bg[1]}:{bg[2]}m"

    output += strings
    print(output, sep='')

    #print(f"\033[38:2:{bg[0]}:{bg[1]}:{bg[2]}m", f"\033[48:2:{logTypes[type][0]}:{logTypes[type][1],{logTypes[type][2]}}", f"[{type}] ", "\033[0m", f"\033[38:2:{clr[0]}:{clr[1],{clr[2]}}", strings, sep='')
    #print(logTypes[type], f"[{type}] ",strings,'\033[0m', sep='')
    #print(type, clr, bg, args)

#log(logTypes['ERROR'], "a")
#log("hey that should be red", type='ERROR')
#print("\033[48;5;31 m", "hey")
#print("\033[31m", "hey")
#print("\033[48:2:255:165:0m", "hey")

log("hey", type='ERROR', bg=[0,0,255], clr=[255,255,0])