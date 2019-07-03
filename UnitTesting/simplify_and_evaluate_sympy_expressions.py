# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi, mpc, fabs
import random
from sympy import cse, N
import UnitTesting.standard_constants as standard_constants
import logging
import hashlib


# Takes in a variable dictionary [var_dict]  and returns
# a dictionary with each expression in [var_dict] evaluated according to parameters (seed, precision).

# Called by run_test

def simplify_and_evaluate_sympy_expressions(var_dict, first_time):

    if var_dict == dict():
        return dict()

    precision = standard_constants.precision

    # Setting precision
    mp.dps = precision

    free_symbols_set = set()
    for val in var_dict.values():
        free_symbols_set = free_symbols_set | val.free_symbols

    # List all the free symbols in the expressions in [var_dict].
    free_symbols_list = list(free_symbols_set)

    # Creating dictionary entry for each variable and its pseudorandom value in [0,1) as determined by seed
    variable_dictionary = dict()

    for var in free_symbols_list:
        # Make sure M_PI is set to its correct value, pi, to the desired number of significant digits"
        if str(var) == "M_PI":
            variable_dictionary[var] = mpf(pi)
        # Then make sure M_SQRT1_2 is set to its correct value, 1/sqrt(2), to the desired number of significant digits:
        elif str(var) == "M_SQRT1_2":
            variable_dictionary[var] = mpf(1/sqrt(2))
        # All other free variables are set to random numbers
        else:
            random.seed(int(hashlib.md5(str(var).encode()).hexdigest(), 16))
            variable_dictionary[var] = mpf(random.random())

    value_dict = dict()
    simplified_expression_dict = dict()
    # Evaluating each expression using the values in variable_dictionary
    for var, expression in var_dict.items():

        if var[0:10] == 'Cart_to_xx':
            print('\nvar: ' + var)
            print('exp: ' + str(expression))

        # Using sympy's cse algorithm to optimize our value substitution
        replaced, reduced = cse(expression, order='none')
        reduced = reduced[0]
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
        # If value is a complex number, store it as a mpc
        except TypeError:
            value_dict[var] = mpc(N(reduced))

        if var[0:10] == 'Cart_to_xx':
            print('val: ' + str(value_dict[var]))

    if first_time:
        for var, val in value_dict.items():
            if val != mpf('0.0') and fabs(val) < 100 * 10 ** (-precision):
                logging.info("Found |result| (" + str(fabs(val)) +
                             ") close to zero. Checking if indeed it should be zero.")
                result = recalculate_value(variable_dictionary, simplified_expression_dict[var][0],
                                           simplified_expression_dict[var][1], 2 * precision)
                if fabs(result) < 100 * 10 ** (-2 * precision):
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