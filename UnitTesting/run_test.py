from UnitTesting.calc_error import calc_error
from UnitTesting.evaluate_globals import evaluate_globals
from UnitTesting.expand_variable_dict import expand_variable_dict
from UnitTesting.first_time_print import first_time_print
from UnitTesting.simplify_and_evaluate_sympy_expressions import simplify_and_evaluate_sympy_expressions
from UnitTesting.standard_constants import precision
from mpmath import mp
from importlib import import_module
import logging


def run_test(self):
    # TODO: Add steps (i.e. 1a, 2, 4c)

    logging.info(' Currently working on function ' + self.function + ' in module ' + self.module_name + '...\n')

    # Set precision to the value defined in standard_constants
    mp.dps = precision

    # Import trusted_values_dict from trusted_values_dict.py in self.path
    logging.info(' Importing trusted_values_dict...')
    self.trusted_values_dict = import_module('trusted_values_dict').trusted_values_dict
    logging.info(' ...Success: Imported trusted_values_dict.\n')

    # Set boolean self.first_time based on existence of desired trusted_values_dict entry
    self.first_time = self.trusted_values_dict_name not in self.trusted_values_dict

    # Set trusted_values_dict_entry its corresponding trusted_values_dict entry; if none exist, set to empty dict
    self.trusted_values_dict_entry = {} if self.first_time else self.trusted_values_dict[self.trusted_values_dict_name]

    logging.info(' Importing ' + self.module + '...')
    # Import self.module
    try:
        self.module = import_module(self.module)
    # If user supplied an incorrect module, log an error and break
    except ImportError:
        logging.error(" Attribute 'module' for " + self.module_name + " does not exist as a module. This attribute "
                      "should be what you would type if you were importing 'module' in your own file.\n")
        self.assertTrue(False)

    logging.info(' ...Success: Imported module.\n')

    # Call self.function and then get expressions for all globals in self.global_list
    logging.info(' Calling evaluate_globals...')
    self.variable_dict = evaluate_globals(self)
    logging.info(' ...Success: evaluate_globals ran without errors.\n')

    # Expand self.variable_dict by breaking up all tensors into scalars.
    logging.info(' Calling expand_variable_dict...')
    self.expanded_variable_dict = expand_variable_dict(self)
    logging.info(' ...Success: expand_variable_dict ran without errors.\n')

    # Assign each variable in each expression a random value and get a value for each expression.
    logging.info(' Calling simplify_and_evaluate_sympy_expressions...')
    self.calculated_dict = simplify_and_evaluate_sympy_expressions(self)
    logging.info(' ...Success: simplify_and_evaluate_sympy_expressions ran without errors.\n')

    # TODO: Not failing when it should
    if self.first_time:
        # Print self.calculated_dict in a nice format and append it to trusted_values_dict
        logging.info(' Calling first_time_print since it is being run for the first time...')
        first_time_print(self)
        logging.info(' ...Success: first_time_print ran without errors.\n')

    else:
        # Calculate the error between the trusted values and the calculated values
        logging.info(' Calling calc_error...')
        values_identical = calc_error(self)
        logging.info(' ...Success: calc_error ran without errors.\n')

        # If there is an error large enough, fail
        if not values_identical:
            self.assertTrue(values_identical,
                            'Variable(s) above have different calculated and trusted values. Follow '
                            'instructions above.')
        # Otherwise, test passes
        else:
            self.assertTrue(values_identical)

