import logging
from mpmath import log10,fabs, mp
from datetime import date
from UnitTesting.standard_constants import precision
from UnitTesting.create_dict_string import create_dict_string

# Takes in a module [mod], a calculated dictionary [calculated_dict], and a trusted dictionary [trusted_dict],
# and computes the error for each result-trusted pair.
# Returns a boolean [good] that represents if any two value pairs didn't differ by more than
# [standard_constants.precision/2] decimal places.

# Called by run_test


def calc_error(mod, calculated_dict, trusted_dict, output=True):

    # Setting precision
    mp.dps = precision

    # Creating sets to easily compare the keys of calculated_dict and trusted_dict
    calculated_set = set(calculated_dict)
    trusted_set = set(trusted_dict)

    # If the sets differ
    if calculated_set != trusted_set:
        # Print differing values if [output] is True
        if output:
            logging.error('\n\t' + mod + ': Calculated dictionary and trusted dictionary have different variables.')
            calculated_minus_trusted = calculated_set - trusted_set
            trusted_minus_calculated = trusted_set - calculated_set
            if calculated_minus_trusted != set([]):
                logging.error('\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' +
                              str(sorted(calculated_minus_trusted)))
            if trusted_minus_calculated != set([]):
                logging.error('\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' +
                              str(sorted(trusted_minus_calculated)))
        # Automatically fail and don't proceed
        return False

    # Initialize list of variables whose values differ
    bad_var_list = []

    # For each variable, print calculated and trusted values
    for var in sorted(calculated_dict):

        # Values to compare
        calculated_val = calculated_dict[var]
        trusted_val = trusted_dict[var]

        if output:
            logging.debug('\n' + mod + ': ' + var + ': Calculated: ' + str(calculated_val) + '\n' + mod + ': ' + var
                          + ': Trusted:    ' + str(trusted_val) + '\n')

        # Calculate the error between both values
        if trusted_val == 0:
            log10_relative_error = log10(fabs(calculated_val))
        elif calculated_val == 0:
            log10_relative_error = log10(fabs(trusted_val))
        else:
            log10_relative_error = log10(fabs((trusted_val - calculated_val) / trusted_val))

        # Boolean determining if their difference is within the tolerance we accept
        good = (log10_relative_error < (precision / -2.0))

        # Store all variables who are not 'good'
        if not good:
            bad_var_list.append(var)

    # If we want to output and there exists at least one variable with error, print
    if output and bad_var_list != []:
        logging.error('\n\nVariable(s) ' + str(bad_var_list) + ' in module ' + str(mod) +
                      ' failed. Please check values.\n\n' + 'If you are confident that the newly calculated values' +
                      ' are correct, comment out the old trusted values for ' + "'" + mod + "Globals'" +
                      ' in trusted_values_dict and copy the following code between the ##### into ' +
                      'trusted_values_dict. Make sure to fill out the TODO comment describing why the values' +
                      ' had to be changed. Then re-run test script.\n' + '#####\n\n# Generated on: ' +
                      str(date.today()) + '\n# Reason for changing values: TODO' + "\ntrusted_values_dict['" +
                      mod + "Globals'] = " + create_dict_string(calculated_dict) + '\n\n#####')

    # Return True if all variables are good, False otherwise
    return bad_var_list == []
