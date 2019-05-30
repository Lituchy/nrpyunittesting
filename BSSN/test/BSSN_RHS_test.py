import unittest
import logging

from trustedValuesDict import trustedValuesDict
from calcError import calcError
from firstTimePrint import firstTimePrint
from functionsAndGlobals import functionsAndGlobals
from evaluateGlobals import evaluateGlobals
from moduleDictToList import moduleDictToList
from listToValueList import listToValueList
from createTrustedGlobalsDict import createTrustedGlobalsDict
from isFirstTime import isFirstTime

import BSSN.BSSN_RHSs_new as RHS
import BSSN.BSSN_gauge_RHSs as gaugeRHS

# Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)

# Globals we want to calculate
RHSGlobalList = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']
gaugeRHSGlobalList = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

ModDict = {
    'RHS': functionsAndGlobals(['BSSN_RHSs()'], RHSGlobalList),

    'gaugeRHS': functionsAndGlobals(['BSSN_gauge_RHSs()'], gaugeRHSGlobalList)
}

# Determining if this is the first time the code is run based of the existence of trusted values
first_time = isFirstTime(ModDict)

# Creating trusted dictionary based off names of modules in ModDict
TrustedDict = createTrustedGlobalsDict(ModDict,first_time)

class Test_BSSN_RHS(unittest.TestCase):

    # Testing scalars
    def testRHSGlobals(self):

        # Creating dictionary of expressions for all modules in ModDict
        resultDict = evaluateGlobals(ModDict, globals())

        # Looping through each module in resultDict
        for mod in resultDict:

            if not first_time:
                logging.info('Currently working on module ' + mod + '...')

            # Generating variable list and name list for module
            (varList, nameList) = moduleDictToList(resultDict[mod])

            # Calculating numerical list for module
            numList = listToValueList(mod, varList, first_time)

            # Initalizing dictionary for the current module
            modDict = dict()

            # Assigning each numerical value to a name in the module's dictionary
            for num, name in zip(numList, nameList):
                modDict[name] = num

            # If being run for the first time, print the code that must be copied into trustedValuesDict
            if first_time:
                firstTimePrint(mod, modDict)
            # Otherwise, compare calculated values to trusted values
            else:

                symbolicDict = dict()

                # Store symbolic expressions in dictionary
                for var, name in zip(varList, nameList):
                    symbolicDict[name] = var

                # Calculates the error between modDict and TrustedDict[mod] for the current module
                valuesIdentical = calcError(mod, modDict, TrustedDict[mod], symbolicDict)

                # If at least one value differs, print exit message and fail the unittest
                if not valuesIdentical:
                    self.assertTrue(valuesIdentical,
                                    'Variable above has different calculated and trusted values. Follow '
                                    'above instructions.')

                # If every value is the same, completed module.
                else:
                    logging.info('Completed module ' + mod + ' with no errors.\n')
                self.assertTrue(valuesIdentical)

        if first_time:
            self.assertTrue(False, 'Automatically fails after running for the first time. Follow above instructions'
                                   ' and run again')


# Necessary for unittest class to work properly
if __name__ == '__main__':
        unittest.main()
