# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi, mpc, fabs
import random
from sympy import cse, N
import UnitTesting.standard_constants as standard_constants
import logging
import hashlib

# Takes in a variable dictionary [var_dict] and a boolean [first_time], and returns
# a dictionary with each expression in [var_dict] evaluated to a numerical expression by assigning each sympy variable
# to a random number. If [first_time] is True, near-zero values are checked if they indeed should be zero.
# Called by run_test


def simplify_and_evaluate_sympy_expressions(expanded_var_dict, first_time=False):

    # If an empty variable dict is passed, return an empty dictionary
    if expanded_var_dict == dict():
        return dict()

    # Setting precision
    precision = standard_constants.precision
    mp.dps = precision

    # Creating free_symbols_set, which stores all free symbols from all expressions.
    free_symbols_set = set()
    for val in expanded_var_dict.values():
        free_symbols_set = free_symbols_set | val.free_symbols

    # Initializing variable_dictionary
    variable_dictionary = dict()

    # Setting each variable in free_symbols_set to a random number in [0, 1) according to the hashed string
    # representation of each variable.
    for var in free_symbols_set:
        # Make sure M_PI is set to its correct value, pi
        if str(var) == "M_PI":
            variable_dictionary[var] = mpf(pi)
        # Then make sure M_SQRT1_2 is set to its correct value, 1/sqrt(2)
        elif str(var) == "M_SQRT1_2":
            variable_dictionary[var] = mpf(1/sqrt(2))
        # All other free variables are set to random numbers
        else:
            # Take the variable [var], turn it into a string, encode the string, hash the string using the md5
            # algorithm, turn the hash into a hex number, turn the hex number into an int, set the random seed to
            # that int. This ensures each variable gets a unique but consistent value.
            random.seed(int(hashlib.md5(str(var).encode()).hexdigest(), 16))
            # Store the random value in variable_dictionary as a mpf
            variable_dictionary[var] = mpf(random.random())

    # Initialize value_dict and simplified_expression_dict
    value_dict = dict()
    simplified_expression_dict = dict()

    # Evaluating each expression using the values in var_dict
    for var, expression in expanded_var_dict.items():

        # Using sympy's cse algorithm to optimize our value substitution
        replaced, reduced = cse(expression, order='none')
        reduced = reduced[0]
        # Store the replaced, reduced result from cse into simplified_expression_dict
        simplified_expression_dict[var] = replaced, reduced

        # Copying variable_dictionary into a new variable dictionary
        new_var_dict = dict(variable_dictionary)

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
            value_dict[var] = mpf(reduced)
        # If value is a complex number, store it as a numerical mpc
        except TypeError:
            value_dict[var] = mpc(N(reduced))

    # If [first_time] is True, double check all near-zero values to see if they should be zero.
    if first_time:
        for var, val in value_dict.items():
            # If val is within [(2/3) * precision] decimal places of zero
            if val != mpf('0.0') and fabs(val) < 10 ** ((-2/3)*precision):
                # Output that near-zero result was found
                logging.info("Found |result| (" + str(fabs(val)) +
                             ") close to zero. Checking if indeed it should be zero.")
                # Recalculate result with double the precision
                result = recalculate_value(variable_dictionary, simplified_expression_dict[var][0],
                                           simplified_expression_dict[var][1], 2 * precision)
                # If the new result dropped in value, we know it should actually be zero. Otherwise, do nothing.
                if fabs(result) < 10 ** (-(4/3) * precision):
                    logging.info("After re-evaluating with twice the digits of precision, |result| dropped to " +
                                 str(result) + ". Setting value to zero")
                    value_dict[var] = mpf('0.0')

    return value_dict


# Subfunction that recalculates value for variable with given precision
def recalculate_value(variable_dictionary, replaced, reduced, precision):

    mp.dps = precision

    # Copying variable_dictionary into a new variable dictionary
    new_var_dict = dict(variable_dictionary)

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

    mp.dps = standard_constants.precision

    return res
