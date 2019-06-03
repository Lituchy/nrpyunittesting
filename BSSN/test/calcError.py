import logging
from trustedValuesDict import trustedValuesDict
from mpmath import log10,fabs
from datetime import datetime

# Takes in a module [mod], a result list [result_list], and a trusted list [trusted_list]
# and computes the error for each result-trusted pair for each respective index.
# Logs debug statements for each pair of values if the logging level is <= DEBUG
# and logs a failure message if logging level is <= ERROR.
# Returns a boolean [good] that represents if any two value pairs didn't differ
# by more than (precision/2) decimal places.

# Called by runTest

def calcError(mod,resultDict,trustedDict,symbolicDict):

    resultSet = set(resultDict)
    trustedSet = set(trustedDict)

    # If resultDict and trustedDict have different variables, print the differing variables
    if resultSet != trustedSet:
        logging.error('\n\t' + mod + ': Calculated dictionary and trusted dictionary have different variables.')
        resultMinusTrusted = resultSet - trustedSet
        trustedMinusResult = trustedSet - resultSet
        if resultMinusTrusted != set([]):
            logging.error('Calculated Dictionary variables not in Trusted Dictionary: \n\t' + str(resultMinusTrusted))
        if trustedMinusResult != set([]):
            logging.error('Trusted Dictionary variables not in Calculated Dictionary: \n\t' + str(trustedMinusResult))
        return False


    # For each variable, print calculated and trusted values
    for var in resultDict:
        resultNum = resultDict[var]
        trustedNum = trustedDict[var]
        outputStr = '\n' + mod + ': ' + var + ': Calculated: ' + str(resultNum) + '\n' + mod + ': ' + var \
                    + ': Trusted:    '+ str(trustedNum)
        if logging.getLogger().getEffectiveLevel() == 0:
            logging.debug(outputStr + '\n' + mod + ': ' + var + ': Symbolic: ' + str(symbolicDict[var]) + '\n')
        else:
            logging.debug(outputStr + '\n')
        if trustedNum == 0:
            log10_relative_error = log10(fabs(resultNum))
        else:
            log10_relative_error = log10(fabs( (trustedNum - resultNum ) / trustedNum ) )
        good = (log10_relative_error < (trustedValuesDict["precision"] / -2))
        if not good:
            logging.error('\n\nVariable ' + var + ' in module ' + str(mod) + ' failed. Please check values.\n\n' +
                          'If you are confident that the newly calculated values are correct, comment out the old '
                          'trusted values for ' + "'" + mod + "Globals'" + ' in trustedValuesDict and copy the '
                          'following code between the ##### into trustedValuesDict. Make sure to fill out the TODO '
                          'comment describing why the values had to be changed. Then re-run test script.\n' +
                          "#####\n\n# Generated on: " + str(datetime.now()) + "\n# Reason for changing values: TODO" 
                          "\ntrustedValuesDict['" + mod + "Globals'] = " + str(resultDict) + '\n\n#####')
            return False
    return True
