# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below.
# This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, sqrt, pi
from random import seed, random
from trustedValuesDict import trustedValuesDict
import outputC


# Takes in a list [lst] and returns the list with each index evaluated
# according to parameters (seed, precision) in trustedValues

# Called by runTest

def testListToValueList(varList, nameList, first_time):

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
    prestring = ''
    for key, val in variable_dictionary.items():
        prestring += '   mpf_t ' + str(key) + '= ' + str(val) + ';\n'

    outputC.outputC(varList, nameList, 'CtestList.C',prestring=prestring)


def __main__():
    from functionsAndGlobals import functionsAndGlobals
    # TODO: Import modules to be tested
    # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
    # Their information gets passed into runTest through locals()
    import BSSN.ADM_in_terms_of_BSSN as ADM_in_terms_of_BSSN
    from createTrustedGlobalsDict import createTrustedGlobalsDict
    from evaluateGlobals import evaluateGlobals
    from moduleDictToList import moduleDictToList

    # TODO: Modules that need to be imported to pre-initialize module and their function calls
    # None

    # TODO: Create lists of globals to calculate
    ADMInTermsOfBSSNGlobalList = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma',
                                  'GammaUDD', 'KDD', 'KDDdD']
    # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
    # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
    # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
    ModDict = {
        'ADM_in_terms_of_BSSN': functionsAndGlobals(['ADM_in_terms_of_BSSN()'], ADMInTermsOfBSSNGlobalList)
    }

    TrustedDict = createTrustedGlobalsDict(ModDict, [False])

    resultDict = evaluateGlobals(ModDict, locals())

    for mod, res in resultDict.items():
        break

    (varList, nameList) = moduleDictToList(res)

    testListToValueList(varList, nameList, False)


if __name__ == '__main__':
    __main__()
