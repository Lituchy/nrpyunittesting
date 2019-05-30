import unittest
import logging

from runTest import runTest
from functionsAndGlobals import functionsAndGlobals
from createTrustedGlobalsDict import createTrustedGlobalsDict
from isFirstTime import isFirstTime

# Note: User-imported
import BSSN.BSSN_RHSs_new as RHS
import BSSN.BSSN_gauge_RHSs as gaugeRHS

# Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)









class Test_BSSN_RHS(unittest.TestCase):

    # Testing scalars
    def testRHSGlobals(self):

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
        TrustedDict = createTrustedGlobalsDict(ModDict, first_time)

        runTest(self,ModDict,TrustedDict,first_time,globals())



# Necessary for unittest class to work properly
if __name__ == '__main__':
        unittest.main()
