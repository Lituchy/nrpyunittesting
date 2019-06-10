from trustedValuesDict import trustedValuesDict

# createTrustedGlobalsDict takes in a module dictionary [ModDict] and a boolean list [first_times].
# For each module, if [first_time] is True, then an empty dictionary is returned.
# This ensures that when the dictionary is passed into [calcError], there will be an error.
# If [first_time] is False, then a dictionary that contains every module in ModDict as keys, and each module's
# respective dictionary from trustedValuesDict as values. The naming convention for the dictionaries is as follows:
#   trustedValuesDict['(MODULE_NAME)Globals'] -- The module name with 'Globals' concatenated on the end.
#   This is consistent throughout all files.

# Called by runTest


def createTrustedGlobalsDict(ModDict, first_times):

    assert len(ModDict) == len(first_times)

    TrustedDict = dict()
    
    for mod, first_time in zip(ModDict,first_times):

        if first_time:
            TrustedDict[mod] = []
        else:
            TrustedDict[mod] = trustedValuesDict[mod + 'Globals']

    return TrustedDict
