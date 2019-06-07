from trustedValuesDict import trustedValuesDict

# isFirstTime takes in a module dictionary [ModDict] and determines if it is the first time the code is being run
# based off the existence of trusted values for every module in [ModDict].
# Requires: The name of the trusted values dictionary is the same as the convention set by createTrustedGlobalsDict

# Called by runTest


def isFirstTime(ModDict):

    result = []

    for mod in ModDict:

        # Boolean stating whether or not the module has an entry with the proper name in trustedValuesDict
        result.append((mod + 'Globals') not in trustedValuesDict)

    return result
