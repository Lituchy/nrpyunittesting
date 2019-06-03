
# functionsAndGlobals takes a list of functions [functionList] and a list of globals [globalList] and returns a
# dictionary with keys 'functionList' and 'globalList', and respective values [functionList] and [globalList].
# Mainly used for creating value of module dictionary.

def functionsAndGlobals(functionList,globalList):

    return {'functionList': functionList, 'globalList': globalList}