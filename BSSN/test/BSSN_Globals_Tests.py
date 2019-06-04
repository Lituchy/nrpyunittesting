
# Necessary imports for unit testing framework
import unittest
import logging
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals



# Exact Modules


# ADM Modules


# TODO Kevin:
# Look into git commit
# Look into pulling last correct travis build and print difference

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


# Python unittest class
class TestBSSNGlobals(unittest.TestCase):
        
    # Testing globals for BSSN exact modules
    def testExactGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.BrillLindquist as BrillLindquist
        import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
        import BSSN.StaticTrumpet as StaticTrumpet
        import BSSN.UIUCBlackHole as UIUCBlackHole

        # TODO: Create lists of globals to calculate
        CartGlobalList = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']
        SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # IMPORTANT: The name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1',not 'Module1'.
        ModDict = {
            'BrillLindquist': functionsAndGlobals(['BrillLindquist(ComputeADMGlobalsOnly = True)'], CartGlobalList),

            'ShiftedKerrSchild': functionsAndGlobals(['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'],
                                                     SphGlobalList),

            'StaticTrumpet': functionsAndGlobals(['StaticTrumpet(ComputeADMGlobalsOnly = True)'], SphGlobalList),

            'UIUCBlackHole': functionsAndGlobals(['UIUCBlackHole(ComputeADMGlobalsOnly = True)'], SphGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())

    # Testing globlas for ADM in terms of BSSN module
    def testADMGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.ADM_in_terms_of_BSSN as ADM_in_terms_of_BSSN

        # TODO: Create lists of globals to calculate
        ADMInTermsOfBSSNGlobalList = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma',
                                      'GammaUDD', 'KDD', 'KDDdD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'ADM_in_terms_of_BSSN': functionsAndGlobals(['ADM_in_terms_of_BSSN()'], ADMInTermsOfBSSNGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
