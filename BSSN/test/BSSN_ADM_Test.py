# Necessary imports for unit testing framework
import unittest
import logging
import coverage
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals
import subprocess


cov = coverage.Coverage()

# TODO: Import modules to be tested
import BSSN.ADM_in_terms_of_BSSN as ADM_in_terms_of_BSSN

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)


# Python unittest class
class TestADM(unittest.TestCase):

    def testADMGlobals(self):

        cov.start()

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

        cov.stop()
        cov.save()
        cov.html_report()
        subprocess.call("firefox htmlcov/index.html", shell=True)



if __name__ == '__main__':
    unittest.main()
