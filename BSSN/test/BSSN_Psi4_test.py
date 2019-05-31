
# Necessary imports for unit testing framework
import unittest
import logging
from runTest import runTest
from functionsAndGlobals import functionsAndGlobals

# TODO: Import modules to be tested
import BSSN.Psi4 as Psi4
import BSSN.Psi4_tetrads as Psi4Tetrads

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)

# Python unittest class
class TestPsi4(unittest.TestCase):


    def testPsi4Globals(self):

        # TODO: Create lists of globals to calculate
        Psi4GlobalList = ['psi4_re_pt', 'psi4_im_pt']
        Psi4TetradsGlobalList = ['l4U', 'n4U', 'mre4U', 'mim4U']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'Psi4': functionsAndGlobals(['Psi4(specify_tetrad=False)'], Psi4GlobalList),

            'Psi4Tetrads': functionsAndGlobals(['Psi4_tetrads()'], Psi4TetradsGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, globals())
        runTest(self, ModDict, globals())
        
if __name__ == '__main__':
    unittest.main()
