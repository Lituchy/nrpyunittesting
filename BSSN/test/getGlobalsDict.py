
def getGlobalsDict(oldGlobals,newGlobals):
    
    value = dict()

    for key in newGlobals:
        if not (key in oldGlobals or key == 'oldGlobals'):
            value[key] = newGlobals[key]
    return value

oldGlobals = dict(globals())

x = 4
Y = 7

print(getGlobalsDict(oldGlobals,globals()))

