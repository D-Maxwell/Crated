logTypes = {
    'ERROR' : '\033[91m',
    'WARN' : '\033[93m'
}

def log(type, *args):
    """
    :param type: ERROR,WARN -> Text color
    :param args: Any amount of strings
    :return: Single color console line
    """
    string:str = ""
    type = logTypes[type]
    for i in range(len(args)):
        string += args[i]
    print(type,string,'\033[0m', sep='')

#log(logTypes['ERROR'], "a")