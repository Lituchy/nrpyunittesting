# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi, mpc, fabs
from random import seed, random
from sympy import cse, simplify
import UnitTesting.standard_constants as standard_constants


# Takes in a variable dictionary [var_dict] a precision value [precision] and a seed value [seed_value], and returns
# a dictionary with each expression in [var_dict] evaluated according to parameters (seed, precision).
# Throws an [AttributeError] if the variable list being passed in has no sympy symbols

# Called by run_test

def var_dict_to_value_dict(var_dict, first_time):

    if var_dict == dict():
        return dict()

    precision = standard_constants.precision

    # Setting precision
    mp.dps = precision

    # List all the free symbols in the expressions in [var_dict].
    free_symbols_list = list(sum(var_dict.values()).free_symbols)

    # Sort free symbols list based off the alphanumeric strings for each variable
    free_symbols_list.sort(key=lambda v: str(v))

    # Set the random seed according to seed in trustedValuesDict:
    seed(standard_constants.seed)

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
            variable_dictionary[var] = sqrt(mpf(random()))

    value_dict = dict()
    # Evaluating each expression using the values in variable_dictionary
    for var, expression in var_dict.items():
        # Copying variable_dictionary into a new variable dictionary
        new_var_dict = dict(variable_dictionary)

        # Using sympy's cse algorithm to optimize our value substitution
        replaced, reduced = cse(expression, order='none')
        reduced = reduced[0]

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
            value_dict[var] = mpc(simplify(reduced))

    if first_time:
        for var, val in value_dict.items():
            if fabs(val) < 100 * 10 ** (-precision):
                print('\nvar: ' + var)
                print('val: ' + str(val))
                expression = var_dict[var]
                print('exp: ' + str(expression))
                # print("Found |result| (" + str(fabs(val)) + ") close to zero. Checking if indeed it should be zero.")
                mp.dps = 2 * precision

    return value_dict

