# Necessary imports for unit testing framework
import unittest
import logging
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals

# TODO: Import modules to be tested
import BSSN.BSSN_T4UUmunu_vars as BSSN_T4UUmunu_vars

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)


# Python unittest class
class TestBSSNT4UUMuNuVars(unittest.TestCase):

    def testT4UUGlobals(self):

        # TODO: Create lists of globals to calculate
        T4UUGlobalList = ['rho','S','sD','sDD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'BSSN_T4UUmunu_vars': functionsAndGlobals(['define_BSSN_T4UUmunu_rescaled_source_terms()'], T4UUGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, globals())
        runTest(self, ModDict, globals())

if __name__ == '__main__':
    unittest.main()
