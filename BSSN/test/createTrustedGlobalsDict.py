from trustedValuesDict import trustedValuesDict
import logging

# TODO: comment me
def createTrustedGlobalsDict(ModDict,first_time):
    
    trustedDict = dict()
    
    if first_time == True:
        for mod in ModDict:
            trustedDict[mod] = []
    else:
        for mod in ModDict:
            globalString = mod + 'Globals'
            if not globalString in trustedValuesDict:
                logging.error('\n ' + mod + ': Reference to nonexistent values in trustedValuesDict. \n Make sure that '
                              + globalString + ' is set in trustedValuesDict.\n Set first_time to True if the trusted'
                              + 'values have not been calculated and pasted into trustedValuesDict yet.')
                assert(False)
            else:
                trustedDict[mod] = trustedValuesDict[globalString]
        
    return trustedDict