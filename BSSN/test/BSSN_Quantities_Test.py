# Necessary imports for unit testing framework
import unittest
import logging
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals

# TODO: Import modules to be tested
import BSSN.BSSN_quantities as BSSN_quantities

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)


# Python unittest class
class TestQuantities(unittest.TestCase):

    def testQuantitiesGlobals(self):

        # TODO: Create lists of globals to calculate
        BSSNQuantitiesGlobalList = ['hDD','aDD','lambdaU','vetU','betU','trK','cf','alpha','gammabarDD','AbarDD','LambdabarU','betaU','BU','gammabarUU', 'gammabarDD_dD', 'gammabarDD_dupD', 'gammabarDD_dDD', 'GammabarUDD','detgammabar','detgammabar_dD','detgammabar_dDD','AbarUU','AbarUD','trAbar','AbarDD_dD','AbarDD_dupD','RbarDD','DGammaUDD','gammabarDD_dHatD','DGammaU','betaU_dD','betaU_dupD','betaU_dDD','phi_dD','phi_dupD','phi_dDD','exp_m4phi','phi_dBarD','phi_dBarDD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'BSSN_quantities': functionsAndGlobals(['declare_BSSN_gridfunctions_if_not_declared_already()', 'BSSN_basic_tensors()', 'gammabar__inverse_and_derivs()', 'detgammabar_and_derivs()','AbarUU_AbarUD_trAbar_AbarDD_dD()','RicciBar__gammabarDD_dHatD__DGammaUDD__DGammaU()','betaU_derivs()','phi_and_derivs()'], BSSNQuantitiesGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, globals())
        runTest(self, ModDict, globals())

if __name__ == '__main__':
    unittest.main()
