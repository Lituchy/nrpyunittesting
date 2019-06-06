# from sympy import srepr, Pow, Add, Mul, Float, Symbol, Integer, cos, sin, Abs, evalf
# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below. This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi
from random import seed, random
# from re import sub
from trustedValuesDict import trustedValuesDict


# Takes in a list [lst] and returns the list with each index evaluated
# according to parameters (seed, precision) in trustedValues

# Called by runTest

def efficientListToValueList(varList, first_time):

    # Setting precision
    precision = trustedValuesDict["precision"]
    mp.dps = precision

    # Replace all integer fractions with the correct floating point representation:
    # index = 0
    # for expr in varList:
    #     string = srepr(expr)
    #     string2 = sub('Rational\(([0-9]+), ([0-9]+)\)',
    #                   "((Float('\\1'," + str(2 * precision) + "))/(Float('\\2'," + str(2 * precision) + ")))", string)
    #     string3 = sub('Rational\((-[0-9]+), ([0-9]+)\)',
    #                   "((Float('\\1'," + str(2 * precision) + "))/(Float('\\2'," + str(2 * precision) + ")))", string2)
    #     newexpr = eval(string3)
    #     varList[index] = newexpr
    #     index += 1

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
            variable_dictionary[var] =  pi
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

    # # TODO: Update this using new evaluation method
    # if first_time:
    #     index = 0
    #     for result in value_list:
    #         print(result)
    #         if result != 0 and fabs(result) < 100 * 10 ** (-precision):
    #             print("Found |result| (" + str(fabs(result)) + ") close to zero. Checking if indeed it should be zero.")
    #             # Now double the precision and redo. If number drops in magnitude
    #             loc2xprec = {}
    #             stringexec = stringexec.replace("mpm.mp.dps = " + str(precision), "mpm.mp.dps = " + str(2 * precision))
    #             exec(stringexec, {}, loc2xprec)
    #             evaled_lst2xprec = loc2xprec['lst']
    #             if fabs(evaled_lst2xprec[index]) < 100 * 10 ** (-2 * precision):
    #                 print("After re-evaluating with twice the digits of precision, |result| dropped to " + str(
    #                     evaled_lst2xprec[index]) + ". Setting value to zero")
    #                 value_list[index] = 0
    #         index += 1

    # # Make sure that all results in valueList *except* zeros are mpm.mpf type!
    # for i in range(len(value_list)):
    #     if value_list[i] != 0:
    #         value_list[i] = mpf(str(value_list[i]))

    return value_list

