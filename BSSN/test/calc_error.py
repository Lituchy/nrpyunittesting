import logging
from trusted_values_dict import trusted_values_dict
from mpmath import log10,fabs
from datetime import datetime

# Takes in a module [mod], a result dictionary [result_dict], a trusted dictionary [trusted_dict], and a symbolic
# dictionary [symbolic_dict] and computes the error for each result-trusted pair for each respective index.
# Logs debug statements for each pair of values if the logging level is <= DEBUG
# and logs a failure message if logging level is <= ERROR.
# Returns a boolean [good] that represents if any two value pairs didn't differ
# by more than (precision/2) decimal places.

# Called by run_test


def calc_error(mod, result_dict, trusted_dict, symbolic_dict):

    # Precision for the module based off the set precision in trusted_values_dict
    precision = trusted_values_dict['precision']

    # Creating sets to easily compare the keys of resultDict and trustedDict
    result_set = set(result_dict)
    trusted_set = set(trusted_dict)

    # If resultDict and trustedDict have different variables, print the differing variables
    if result_set != trusted_set:
        logging.error('\n\t' + mod + ': Calculated dictionary and trusted dictionary have different variables.')
        result_minus_trusted = result_set - trusted_set
        trusted_minus_result = trusted_set - result_set
        if result_minus_trusted != set([]):
            logging.error('Calculated Dictionary variables not in Trusted Dictionary: \n\t' + str(result_minus_trusted))
        if trusted_minus_result != set([]):
            logging.error('Trusted Dictionary variables not in Calculated Dictionary: \n\t' + str(trusted_minus_result))
        return False

    del result_set, trusted_set

    # For each variable, print calculated and trusted values
    for var in result_dict:
        result_num = result_dict[var]
        trusted_num = trusted_dict[var]
        output_str = '\n' + mod + ': ' + var + ': Calculated: ' + str(result_num) + '\n' + mod + ': ' + var \
                    + ': Trusted:    '+ str(trusted_num)
        if logging.getLogger().getEffectiveLevel() == 0:
            logging.debug(output_str + '\n' + mod + ': ' + var + ': Symbolic: ' + str(symbolic_dict[var]) + '\n')
        else:
            logging.debug(output_str + '\n')
        if trusted_num == 0:
            log10_relative_error = log10(fabs(result_num))
        else:
            log10_relative_error = log10(fabs((trusted_num - result_num) / trusted_num))
        good = (log10_relative_error < (precision / -2))
        if not good:
            logging.error('\n\nVariable ' + var + ' in module ' + str(mod) + ' failed. Please check values.\n\n' +
                          'If you are confident that the newly calculated values are correct, comment out the old '
                          'trusted values for ' + "'" + mod + "Globals'" + ' in trustedValuesDict and copy the '
                          'following code between the ##### into trustedValuesDict. Make sure to fill out the TODO '
                          'comment describing why the values had to be changed. Then re-run test script.\n' +
                          "#####\n\n# Generated on: " + str(datetime.now()) + "\n# Reason for changing values: TODO" 
                          "\ntrustedValuesDict['" + mod + "Globals'] = " + str(result_dict) + '\n\n#####')
            return False

    return True
