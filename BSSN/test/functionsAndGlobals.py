
# functionsAndGlobals takes a list of functions [functionList] and a list of globals [globalList] and returns a
# dictionary with keys 'functionList' and 'globalList', and respective values [functionList] and [globalList].
# Mainly used for creating value of module dictionary.
# Throws AssertionError if either functionList or globalList is not a list,
# or if any element in either list is not a string


def functionsAndGlobals(functionList,globalList):

    assert(isinstance(functionList, list))
    assert(isinstance(globalList,   list))

    for function in functionList:
        assert(isinstance(function, str))
    for glob in globalList:
        assert(isinstance(glob, str))

    return {'functionList': functionList, 'globalList': globalList}