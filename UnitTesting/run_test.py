from UnitTesting.calc_error import calc_error
from UnitTesting.first_time_print import first_time_print
from UnitTesting.evaluate_globals import evaluate_globals
from UnitTesting.expand_variable_dict import expand_variable_dict
from UnitTesting.simplify_and_evaluate_sympy_expressions import simplify_and_evaluate_sympy_expressions
from UnitTesting.create_trusted_globals_dict import create_trusted_globals_dict
from UnitTesting.standard_constants import precision
from mpmath import mp
from importlib import import_module
import sys
import logging


# run_test takes in :
# [self]- The unittest self object,
# [mod_dict]- The user-supplied dictionary of modules
# [trusted_values_dict]- The dictionary of trusted values
# [path]- The path to the directory where the test file is being run. Should usually be 'os.path.abspath(__file__)'
# [locs]- The current local variables in the workspace. Should ALWAYS be locals()
# It then runs a unittest, comparing calculated values with trusted values.
# Throws an [AssertionError] if [mod_dict] is empty
def run_test(self, path, module, module_name, global_list, function_list):

    # Assuring correct type for all arguments
    self.assertTrue(type(path) == str, "'path' argument of run_test has incorrect type -- should be str.")
    self.assertTrue(type(module) == str, "'module' argument of run_test has incorrect type -- should be str.")
    self.assertTrue(type(module_name) == str, "'module_name' argument of run_test has incorrect type -- should be str.")
    self.assertTrue(type(global_list) == list,
                    "'global_list' argument of run_test has incorrect type -- should be list.")
    self.assertTrue(type(function_list) == list,
                    "'function_list' argument of run_test has incorrect type -- should be list.")

    mp.dps = precision

    sys.path.append(path)

    trusted_values_dict = import_module('trusted_values_dict').trusted_values_dict

    first_time = (module_name + 'Globals') not in trusted_values_dict

    # Creating trusted dictionary based off names of modules in ModDict
    trusted_dict = create_trusted_globals_dict(module_name, trusted_values_dict, first_time)

    try:
        module = import_module(module)
    except ImportError:
        self.assertTrue(False, "Argument 'module' in run_test does not exist as a module. Check path input.")

    # Creating dictionary of expressions for all modules in ModDict
    var_dict = evaluate_globals(module_name, global_list, function_list, module)

    if not first_time:
        logging.info('Currently working on module ' + module_name + '...')

    # Generating variable list and name list for module
    expanded_var_dict = expand_variable_dict(var_dict)

    # Calculating numerical list for module
    value_dict = simplify_and_evaluate_sympy_expressions(expanded_var_dict, first_time)

    # If being run for the first time, print the code that must be copied into trusted_values_dict
    if first_time:
        first_time_print(module_name, value_dict, path)

    # Otherwise, compare calculated values to trusted values
    else:

        # Calculates the error between mod_dict and trusted_dict[mod] for the current module
        values_identical = calc_error(module_name, value_dict, trusted_dict)

        # If at least one value differs, print exit message and fail the unittest
        if not values_identical:
            self.assertTrue(values_identical,
                            'Variable above has different calculated and trusted values. Follow '
                            'above instructions.')

        # If every value is the same, completed module.
        else:
            logging.info('Completed module ' + module_name + ' with no errors.\n')
        self.assertTrue(values_identical)

    # If it's the first time for at least one module
    if first_time:
        self.assertTrue(False, 'Automatically failing due to first time for at least one module. Please see above '
                               'for the code to copy into your trusted_values_dict.')
