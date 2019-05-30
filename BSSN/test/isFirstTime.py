from trustedValuesDict import trustedValuesDict

# isFirstTime takes in a module dictionary [ModDict] and determines if it is the first time the code is being run
# based off the existence of trusted values for every module in [ModDict]
# Requires: The name of the trusted values dictionary is the same as the convention set by createTrustedGlobalsDict
def isFirstTime(ModDict):

    # Checks every module in ModDict
    for mod in ModDict:
        if not (mod + 'Globals') in trustedValuesDict:
            return True

    return False
