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
                logging.error('\n\t' + mod + ': Reference to nonexistant values in trustedValuesDict. Make sure that ' + globalString + ' is set in trustedValuesDict.\n')
                assert(False)
            else:
                trustedDict[mod] = trustedValuesDict[globalString]
        
    return trustedDict