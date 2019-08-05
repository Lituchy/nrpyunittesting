# Step 1: Initialize core Python/UnitTesting modules
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

    logging.info(' Currently working on function ' + self.function + ' in module ' + self.module_name + '...\n')

    # Step 2: Pre-processing

    # Step 2.a: Set precision to the value defined in standard_constants
    mp.dps = precision

    # Step 2.b: Import trusted_values_dict from trusted_values_dict.py in self.path
    logging.info(' Importing trusted_values_dict...')
    self.trusted_values_dict = import_module('trusted_values_dict').trusted_values_dict
    logging.info(' ...Success: Imported trusted_values_dict.\n')

    # Step 2.c: Set boolean self.first_time based on existence of desired trusted_values_dict entry
    self.first_time = self.trusted_values_dict_name not in self.trusted_values_dict

    # Step 2.d: Set trusted_values_dict_entry to its corresponding trusted_values_dict entry
    self.trusted_values_dict_entry = {} if self.first_time else self.trusted_values_dict[self.trusted_values_dict_name]

    # Step 2.e: Import self.module
    logging.info(' Importing ' + self.module + '...')
    try:
        self.module = import_module(self.module)
    # If user supplied an incorrect module, log an error and break
    except ImportError:
        logging.error(" Attribute 'module' for " + self.module_name + " does not exist as a module. This attribute "
                      "should be what you would type if you were importing 'module' in your own file.\n")
        self.assertTrue(False)
    logging.info(' ...Success: Imported module.\n')

    # Step 3: Calculation

    # Step 3.a: Call evaluate_globals to call self.function and get expressions for all globals in self.global_list
    logging.info(' Calling evaluate_globals...')
    self.variable_dict = evaluate_globals(self)
    logging.info(' ...Success: evaluate_globals ran without errors.\n')

    # Step 3.b: Call expand_variable_dict to break up all tensors into scalars with associated names.
    logging.info(' Calling expand_variable_dict...')
    self.expanded_variable_dict = expand_variable_dict(self)
    logging.info(' ...Success: expand_variable_dict ran without errors.\n')

    # Step 3.c: Call simplify_and_evaluate_sympy_expressions to assign each variable in each expression a random value
    #           and calculate the numerical result
    logging.info(' Calling simplify_and_evaluate_sympy_expressions...')
    self.calculated_dict = simplify_and_evaluate_sympy_expressions(self)
    logging.info(' ...Success: simplify_and_evaluate_sympy_expressions ran without errors.\n')

    # Step 4: Comparison

    # TODO: Not failing when it should
    if self.first_time:
        # Step 4.a: Print self.calculated_dict in a nice format and append it to trusted_values_dict
        logging.info(' Calling first_time_print since it is being run for the first time...')
        first_time_print(self)
        logging.info(' ...Success: first_time_print ran without errors. Automatically failing due to first_time.\n')

    else:
        # Step 4.b: Call calc_error to calculate the error between the trusted values and the calculated values
        logging.info(' Calling calc_error...')
        values_identical = calc_error(self)

        # If there is an error large enough, fail
        if not values_identical:
            self.assertTrue(values_identical,
                            'Variable(s) above have different calculated and trusted values. Follow '
                            'instructions above.')
        # Otherwise, pass
        else:
            logging.info(' ...Success: calc_error ran without errors.\n')
