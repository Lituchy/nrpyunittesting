# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi
from random import seed, random
from trustedValuesDict import trustedValuesDict
from sympy import cse


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
        # Copying variable_dictionary into a new variable dictionary
        new_var_dict = dict(variable_dictionary)

        # Using sympy's cse algorithm to optimize our value substitution
        repl, redu = cse(expression, order='none')
        redu = redu[0]

        # Replacing old expressions with new expressions and putting result in new variable dictionary
        for new, old in repl:
            keys = old.free_symbols
            for key in keys:
                old = old.subs(key, new_var_dict[key])
            new_var_dict[new] = old

        # Evaluating expression after cse optimization
        keys = redu.free_symbols
        for key in keys:
            redu = redu.subs(key, new_var_dict[key])

        # Appending our result to value_list
        value_list.append(mpf(redu))

    return value_list