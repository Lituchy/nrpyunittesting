from UnitTesting.calc_error import calc_error
from UnitTesting.evaluate_globals import evaluate_globals
from UnitTesting.expand_variable_dict import expand_variable_dict
from UnitTesting.first_time_print import first_time_print
from UnitTesting.simplify_and_evaluate_sympy_expressions import simplify_and_evaluate_sympy_expressions
from UnitTesting.standard_constants import precision

from mpmath import mp
from importlib import import_module
import sys
import logging


def run_test(self):

    logging.debug(' Beginning run_test...\n')

    logging.info(' Currently working on function ' + self.function + ' in module ' + self.module_name + '...\n')

    # Setting the precision
    mp.dps = precision

    # Append [path] to [sys.path] in order to ensure that [import_module] functions correctly
    sys.path.append(self.path)

    # Getting [trusted_values_dict] by importing it from [path/trusted_values_dict.py]
    self.trusted_values_dict = import_module('trusted_values_dict').trusted_values_dict

    # Setting boolean [first_time] based off existence of entry in trusted_values_dict
    self.first_time = self.trusted_values_dict_name not in self.trusted_values_dict

    # Creating trusted dictionary based off names of modules in ModDict
    self.trusted_values_dict_entry = {} if self.first_time else self.trusted_values_dict[self.trusted_values_dict_name]

    # Try to import [module], giving an error message if it's in the wrong format
    try:
        self.module = import_module(self.module)
    except ImportError:
        logging.error(" Attribute 'module' for " + self.module_name + " does not exist as a module. This attribute "
                      "should be what you would type if you were importing 'module' in your own file.\n")
        self.assertTrue(False)

    # Creating dictionary of expressions for all modules in ModDict
    self.variable_dict = evaluate_globals(self)

    # Generating variable list and name list for module
    self.expanded_variable_dict = expand_variable_dict(self)

    # Calculating numerical list for module
    self.calculated_dict = simplify_and_evaluate_sympy_expressions(self)

    # If being run for the first time, print the code that must be copied into trusted_values_dict
    if self.first_time:
        first_time_print(self)

    # Otherwise, compare calculated values to trusted values
    else:

        # Calculates the error between mod_dict and trusted_dict[mod] for the current module
        values_identical = calc_error(self)

        # If at least one value differs, print exit message and fail the unittest
        if not values_identical:
            self.assertTrue(values_identical,
                            'Variable(s) above have different calculated and trusted values. Follow '
                            'instructions above.')

        # If every value is the same, completed module.
        logging.info('Completed module ' + self.module_name + ' with no errors.\n')
        self.assertTrue(values_identical)

    # If it's the first time for at least one module
    if self.first_time:
        self.assertTrue(False, 'Automatically failing due to it being the first time for at least one module. '
                               'Please see above for the code to copy into your trusted_values_dict.')
