import logging
from trustedValuesDict import trustedValuesDict
from mpmath import log10,fabs

# Takes in a module [mod], a result list [result_list], and a trusted list [trusted_list]
# and computes the error for each result-trusted pair for each respective index.
# Logs debug statements for each pair of values if the logging level is <= DEBUG
# and logs a failure message if logging level is <= ERROR.
# Returns a boolean [good] that represents if any two value pairs didn't differ
# by more than (precision/2) decimal places.

def calcError(mod,resultDict,trustedDict):

    if set(resultDict) != set(trustedDict):
        logging.error(mod + ': Calculated dictionary and trusted dictionary have different variables.')
        logging.error('Calculated Dictionary variables: ' + str(resultDict.keys()))
        logging.error('Trusted Dictionary variables: ' + str(trustedDict.keys()))
        return False
    
    for var in resultDict:
        resultNum = resultDict[var]
        trustedNum = trustedDict[var]
        logging.debug('\n' + var + ': \n\tCalculated: ' + str(resultNum) + '\n\tTrusted:    '+ str(trustedNum)+'\n')
        if trustedNum == 0:
            log10_relative_error = log10(fabs(resultNum))
        else:
            log10_relative_error = log10(fabs( (trustedNum - resultNum ) / trustedNum ) )
        good = (log10_relative_error < (trustedValuesDict["precision"] / -2))
        if not good:
            logging.error('\n\n Variable ' + var + ' in module ' + str(mod) + 'failed. Please check values.\n\n')
            return False
    return True
