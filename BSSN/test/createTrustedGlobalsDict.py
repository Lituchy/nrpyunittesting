from trustedValuesDict import trustedValuesDict
import logging

# createTrustedGlobalsDict takes in a module dictionary [ModDict] and a boolean [first_time].
# If [first_time] is True, then an empty dictionary is returned. This insures that when the dictionary is passed into
# [calcError], there will be an error so there will be output.
# If [first_time] is False, then a dictionary that contains every module in ModDict as keys, and each module's
# respective dictionary from trustedValuesDict as values. The naming convention for the dictionaries is as follows:
#   trustedValuesDict['(MODULE_NAME)Globals'] -- The module name with 'Globals' concatenated on the end. This is
#   consistent throughout all files.
def createTrustedGlobalsDict(ModDict,first_time):
    
    trustedDict = dict()
    
    if first_time == True:
        for mod in ModDict:
            trustedDict[mod] = []
    else:
        for mod in ModDict:

            globalString = mod + 'Globals'

            if globalString not in trustedValuesDict:
                logging.error('\n ' + mod + ': Reference to nonexistent values in trustedValuesDict. \n Make sure that '
                              + globalString + ' is set in trustedValuesDict.\n Set first_time to True if the trusted'
                              + 'values have not been calculated and pasted into trustedValuesDict yet.')
                assert(False)
            else:
                trustedDict[mod] = trustedValuesDict[globalString]
        
    return trustedDict
