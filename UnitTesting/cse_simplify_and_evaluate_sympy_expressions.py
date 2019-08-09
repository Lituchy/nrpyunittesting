# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi, mpc, fabs
import random
from sympy import cse, N
import UnitTesting.standard_constants as standard_constants
import logging
import hashlib

# Takes in a variable dictionary [expanded_variable_dict] and a boolean [first_time], and returns
# a dictionary with each expression in [expanded_variable_dict] evaluated to a numerical expression by assigning each
# sympy variable to a deterministic pseudorandom number.
# If [first_time] is True, near-zero values are checked if they indeed should be zero.

# Called by run_test

precision = standard_constants.precision


def cse_simplify_and_evaluate_sympy_expressions(self):

    # If an empty variable dict is passed, return an empty dictionary
    if self.expanded_variable_dict == {}:
        return {}

    # Setting precision
    mp.dps = precision

    # Creating free_symbols_set, which stores all free symbols from all expressions.

    logging.debug(' Getting all free symbols...')
    free_symbols_set = set()
    for val in self.expanded_variable_dict.values():
        try:
            free_symbols_set = free_symbols_set | val.free_symbols
        except AttributeError:
            pass

    # Initializing free_symbols_dict
    free_symbols_dict = dict()

    logging.debug(' ...Setting each free symbol to a random value...')

    # Setting each variable in free_symbols_set to a random number in [0, 1) according to the hashed string
    # representation of each variable.
    for var in free_symbols_set:
        # Make sure M_PI is set to its correct value, pi
        if str(var) == "M_PI":
            free_symbols_dict[var] = mpf(pi)
        # Then make sure M_SQRT1_2 is set to its correct value, 1/sqrt(2)
        elif str(var) == "M_SQRT1_2":
            free_symbols_dict[var] = mpf(1/sqrt(2))
        # All other free variables are set to random numbers
        else:
            # Take the variable [var], turn it into a string, encode the string, hash the string using the md5
            # algorithm, turn the hash into a hex number, turn the hex number into an int, set the random seed to
            # that int. This ensures each variable gets a unique but consistent value.
            random.seed(int(hashlib.md5(str(var).encode()).hexdigest(), 16))
            # Store the random value in free_symbols_dict as a mpf
            free_symbols_dict[var] = mpf(random.random())

    # Initialize value_dict and simplified_expression_dict
    value_dict = dict()
    simplified_expression_dict = dict()

    logging.debug(' ...Calculating values for each variable based on free symbols...')

    # Evaluating each expression using the values in var_dict
    for var, expression in self.expanded_variable_dict.items():
        # Using SymPy's cse algorithm to optimize our value substitution
        replaced, reduced = cse(expression, order='none')
        reduced = reduced[0]

        result_value = calculate_value(free_symbols_dict, replaced, reduced)

        if fabs(result_value) != mpf('0.0') and fabs(result_value) < 10 ** ((-2.0/3)*precision):
            logging.info("Found |result| (" + str(fabs(result_value)) + ") close to zero. "
                         "Checking if indeed it should be zero.")
            new_result_value = calculate_value(free_symbols_dict, replaced, reduced, precision_factor=2)
            if fabs(new_result_value) < 10 ** (-(4.0/3) * precision):
                logging.info("After re-evaluating with twice the digits of precision, |result| dropped to " +
                             str(new_result_value) + ". Setting value to zero")
                result_value = mpf('0.0')

        value_dict[var] = result_value

    return value_dict


# Sub-function that calculates value for variable with precision multiplied by precision_factor
def calculate_value(free_symbols_dict, replaced, reduced, precision_factor=1):

    mp.dps = precision_factor * precision

    # Copying free_symbols_dict into a new variable dictionary
    new_var_dict = dict(free_symbols_dict)

    # Replacing old expressions with new expressions and putting result in new variable dictionary
    for new, old in replaced:
        keys = old.free_symbols
        for key in keys:
            old = old.subs(key, new_var_dict[key])
        new_var_dict[new] = old

    # Evaluating expression after cse optimization
    keys = reduced.free_symbols
    for key in keys:
        reduced = reduced.subs(key, new_var_dict[key])

    # Adding our variable, value pair to our value_dict
    try:
        res = mpf(reduced)
    # If value is a complex number, store it as a mpc
    except TypeError:
        res = mpc(N(reduced))

    mp.dps = precision

    return res
