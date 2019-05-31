
# Necessary imports for unit testing framework
import unittest
import logging
from runTest import runTest
from functionsAndGlobals import functionsAndGlobals

# TODO: Import modules to be tested
import BSSN.BrillLindquist as BrillLindquist
import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
import BSSN.StaticTrumpet as StaticTrumpet
import BSSN.UIUCBlackHole as UIUCBlackHole

# TODO Kevin:
# Look into git commit
# Look into pulling last correct travis build and print difference

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)


# Python unittest class
class TestBSSNExact(unittest.TestCase):
        
    # Testing globals for BSSN exact modules
    def testExactGlobals(self):

        # TODO: Create lists of globals to calculate
        CartGlobalList = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']
        SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'BrillLindquist': functionsAndGlobals(['BrillLindquist(ComputeADMGlobalsOnly = True)'], CartGlobalList),

            'ShiftedKerrSchild': functionsAndGlobals(['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'],
                                                     SphGlobalList),

            'StaticTrumpet': functionsAndGlobals(['StaticTrumpet(ComputeADMGlobalsOnly = True)'], SphGlobalList),

            'UIUCBlackHole': functionsAndGlobals(['UIUCBlackHole(ComputeADMGlobalsOnly = True)'], SphGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, globals())
        runTest(self, ModDict, globals())


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
