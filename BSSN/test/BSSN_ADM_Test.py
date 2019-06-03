# Necessary imports for unit testing framework
import unittest
import logging
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals

# TODO: Set coverage to True if you want a coverage report, False if you don't
# Note that coverage reports don't work on travis-ci, so it's best to set to False before pushing.
coverage = False

# TODO: Import modules to be tested
import BSSN.ADM_in_terms_of_BSSN as ADM_in_terms_of_BSSN

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


# Python unittest class
class TestADM(unittest.TestCase):

    def testADMGlobals(self):

        # Start coverage
        if coverage:
            import BSSN.test.coverageReport as coverageReport
            coverageReport.coverageStart()

        # TODO: Create lists of globals to calculate
        ADMInTermsOfBSSNGlobalList = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma',
                                      'GammaUDD', 'KDD', 'KDDdD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'ADM_in_terms_of_BSSN': functionsAndGlobals(['ADM_in_terms_of_BSSN()'], ADMInTermsOfBSSNGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, globals())
        runTest(self, ModDict, globals())

        # End coverage
        if coverage:
            coverageReport.coverageEnd('+BSSN')


if __name__ == '__main__':
    unittest.main()
