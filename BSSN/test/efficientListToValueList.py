# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi
from random import seed, random
from trustedValuesDict import trustedValuesDict


# Takes in a list [lst] and returns the list with each index evaluated
# according to parameters (seed, precision) in trustedValues

# Called by runTest

def efficientListToValueList(varList, first_time):

    # Setting precision
    mp.dps = trustedValuesDict["precision"]

    # List all the free symbols in the expressions in [lst].
    free_symbols_list = list(sum(varList).free_symbols)

    # Sort free symbols list based off the alphanumeric strings for each variable
    free_symbols_list.sort(key=lambda v: str(v))

    # Set the random seed according to seed in trustedValuesDict:
    seed(trustedValuesDict["seed"])

    # Creating dictionary entry for each variable and its pseudorandom value in [0,1) as determined by seed
    variable_dictionary = dict()
    for var in free_symbols_list:
        if str(var) == "M_PI":
            variable_dictionary[var] = mpf(pi)
        # Then make sure M_SQRT1_2 is set to its correct value, 1/sqrt(2), to the desired number of significant digits:
        elif str(var) == "M_SQRT1_2":
            variable_dictionary[var] = mpf(1/sqrt(2))
        # All other free variables are set to random numbers
        else:
            variable_dictionary[var] = sqrt(mpf(random()))

    # Evaluating each expression using the values in variable_dictionary
    value_list = []
    for expression in varList:
        # Getting free symbols for expression
        keys = expression.free_symbols
        for key in keys:
            # Replacing each free symbol with its value in variable_dictionary
            expression = expression.subs(key, variable_dictionary[key])
        # Create list of values found by evaluating expression
        value_list.append(mpf(expression))

    return value_list
