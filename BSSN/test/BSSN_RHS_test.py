
# Necessary imports for unit testing framework
import unittest
import logging
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals

# TODO: Import modules to be tested
import BSSN.BSSN_RHSs_new as RHS
import BSSN.BSSN_gauge_RHSs as gaugeRHS

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)

class Test_BSSN_RHS(unittest.TestCase):

    # Testing scalars
    def testRHSGlobals(self):

        # TODO: Create lists of globals to calculate
        RHSGlobalList = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']
        gaugeRHSGlobalList = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'RHS': functionsAndGlobals(['BSSN_RHSs()'], RHSGlobalList),

            'gaugeRHS': functionsAndGlobals(['BSSN_gauge_RHSs()'], gaugeRHSGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, globals())
        runTest(self, ModDict, globals())


# Necessary for unittest class to work properly
if __name__ == '__main__':
        unittest.main()
