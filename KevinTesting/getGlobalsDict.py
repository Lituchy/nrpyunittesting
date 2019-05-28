
def getGlobalsDict(oldGlobals,newGlobals):
    
    value = dict()

    for key in newGlobals:
        if not (key in oldGlobals):
            value[key] = newGlobals[key]
    return value



