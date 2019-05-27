# Takes in a module [mod], a result list [result_list], and a trusted list [trusted_list]
# and computes the error for each result-trusted pair for each respective index.
# Logs debug statements for each pair of values if the logging level is <= DEBUG
# and logs a failure message if logging level is <= ERROR.
# Returns a boolean [good] that represents if any two value pairs didn't differ
# by more than (precision/2) decimal places.
def calcError(mod,result_list,trusted_list):
    print
    for res, val in zip(result_list, trusted_list):
        logging.debug('\nResult, value: \n\t' + str(res) + '\n\t'+ str(val)+'\n')
        if val == 0:
            log10_relative_error = log10(fabs(res))
        else:
            log10_relative_error = log10(fabs( (val - res ) / val ) )
        good = (log10_relative_error < (precision / -2))
        if not good:
            logging.error('\n\n Failed with ' + str(mod) + '\n\n')
            return False
    return True