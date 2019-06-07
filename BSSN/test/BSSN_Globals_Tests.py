
# Necessary imports for unit testing framework
import unittest
import logging
from BSSN.test.runTest import runTest
from BSSN.test.functionsAndGlobals import functionsAndGlobals
from RepeatedTimer import RepeatedTimer
import cProfile

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds/13151299
# Creates a threaded timer object that prints to the console every 5 minutes
def printFn(msg):
    logging.info(msg)


Timer = RepeatedTimer(300, printFn, "\nPrinting every 5 minutes to prevent timeouts.\n")


# Python unittest class
class TestBSSNGlobals(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    # Testing globals for ADM in terms of BSSN module
    def testADMGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.ADM_in_terms_of_BSSN as ADM_in_terms_of_BSSN

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        # None

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

    # Testing globals for BSSN Constraints
    def testConstraintsGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.BSSN_constraints as BSSN_constraints

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        # None

        # TODO: Create lists of globals to calculate
        ConstraintsGlobalList = ['H', 'MU']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'BSSN_constraints': functionsAndGlobals(['BSSN_constraints()'], ConstraintsGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())
        
    # Testing globals for BSSN exact modules
    def testExactGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.BrillLindquist as BrillLindquist
        import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
        import BSSN.StaticTrumpet as StaticTrumpet
        import BSSN.UIUCBlackHole as UIUCBlackHole

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        # None

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

    # Testing globals for BSSN Psi4 Globals
    def testPsi4Globals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.Psi4 as Psi4
        import BSSN.Psi4_tetrads as Psi4Tetrads

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        # None

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

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())

    # Testing globals for BSSN quantities
    def testQuantitiesGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.BSSN_quantities as BSSN_quantities

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        import reference_metric as rfm
        rfm.reference_metric()

        # TODO: Create lists of globals to calculate
        QuantitiesGlobalList = ['hDD','aDD','lambdaU','vetU','betU','trK','cf','alpha','gammabarDD','AbarDD','LambdabarU','betaU','BU','gammabarUU', 'gammabarDD_dD', 'gammabarDD_dupD', 'gammabarDD_dDD', 'GammabarUDD','detgammabar','detgammabar_dD','detgammabar_dDD','AbarUU','AbarUD','trAbar','AbarDD_dD','AbarDD_dupD','RbarDD','DGammaUDD','gammabarDD_dHatD','DGammaU','betaU_dD','betaU_dupD','betaU_dDD','phi_dD','phi_dupD','phi_dDD','exp_m4phi','phi_dBarD','phi_dBarDD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'BSSN_quantities': functionsAndGlobals(['declare_BSSN_gridfunctions_if_not_declared_already()','BSSN_basic_tensors()','gammabar__inverse_and_derivs()','detgammabar_and_derivs()','AbarUU_AbarUD_trAbar_AbarDD_dD()','RicciBar__gammabarDD_dHatD__DGammaUDD__DGammaU()','betaU_derivs()','phi_and_derivs()'],
                                                   QuantitiesGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())

    # Testing globals for BSSN RHS
    def testRHSGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.BSSN_RHSs_new as RHS
        import BSSN.BSSN_gauge_RHSs as gaugeRHS

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        # None

        # TODO: Create lists of globals to calculate
        RHSGlobalList = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']
        gaugeRHSGlobalList = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'RHS': functionsAndGlobals(['BSSN_RHSs()'], RHSGlobalList),

            'gaugeRHS': functionsAndGlobals(['BSSN_gauge_RHSs()'], gaugeRHSGlobalList),
        }

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())

    # Testing globals for BSSN T4UUmunu_vars
    def testT4UUGlobals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
        # Their information gets passed into runTest through locals()
        import BSSN.BSSN_T4UUmunu_vars as BSSN_T4UUmunu_vars

        # TODO: Modules that need to be imported to pre-initialize module and their function calls
        # None

        # TODO: Create lists of globals to calculate
        T4UUGlobalList = ['rho','S','sD','sDD']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in ModDicT MUST have the same name as the imported module.
        # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1' as a string.
        ModDict = {
            'BSSN_T4UUmunu_vars': functionsAndGlobals(['define_BSSN_T4UUmunu_rescaled_source_terms()'], T4UUGlobalList)
        }

        # TODO: Call runTest with arguments (self, ModDict, locals())
        runTest(self, ModDict, locals())


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
