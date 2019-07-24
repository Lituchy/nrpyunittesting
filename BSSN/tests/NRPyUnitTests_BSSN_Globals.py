# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)

# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds/13151299
# Creates a threaded timer object that prints to the console every 5 minutes
Timer = RepeatedTimer(300, logging.info, "\nPrinting every 5 minutes to prevent timeouts.\n")


# Python unittest class
class TestBSSNGlobals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Creating trusted_values_dict.py if it doesn't exist
        import sys
        cls.path = sys.path[0]
        setup_trusted_values_dict(cls.path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    # Testing globals for ADM in terms of BSSN module
    def test_ADM_Globals(self):

        self.module = 'BSSN.ADM_in_terms_of_BSSN'

        self.module_name = 'ADM_in_terms_of_BSSN'

        self.global_list = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma', 'GammaUDD', 'KDD', 'KDDdD']

        self.function_list = ['ADM_in_terms_of_BSSN()']

        run_test(self)

    # Testing globals for BSSN constraints
    def test_Constraints_Globals(self):

        self.module = 'BSSN.BSSN_constraints'

        self.module_name = 'BSSN_constraints'

        self.global_list = ['H', 'MU']

        self.function_list = ['BSSN_constraints()']

        run_test(self)

    # Testing globals for BSSN exact modules
    def test_BrillLindquist_Globals(self):

        self.module = 'BSSN.BrillLindquist'

        self.module_name = 'BrillLindquist'

        self.global_list = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']

        self.function_list = ['BrillLindquist(ComputeADMGlobalsOnly = True)']

        run_test(self)

    def test_UIUCBlackHole_Globals(self):

        self.module = 'BSSN.UIUCBlackHole'

        self.module_name = 'UIUCBlackHole'

        self.global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        self.function_list = ['UIUCBlackHole(ComputeADMGlobalsOnly = True)']

        run_test(self)

    def test_StaticTrumpet_Globals(self):
        self.module = 'BSSN.StaticTrumpet'

        self.module_name = 'StaticTrumpet'

        self.global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        self.function_list = ['StaticTrumpet(ComputeADMGlobalsOnly = True)']

        run_test(self)

    def test_ShiftedKerrSchild_Globals(self):
        self.module = 'BSSN.ShiftedKerrSchild'

        self.module_name = 'ShiftedKerrSchild'

        self.global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        self.function_list = ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)']

        run_test(self)

    # Testing globals for BSSN Psi4 Globals
    def test_Psi4_Globals(self):

        self.module = 'BSSN.Psi4'

        self.module_name = 'Psi4'

        self.global_list = ['psi4_re_pt', 'psi4_im_pt']

        self.function_list = ['Psi4(specify_tetrad=False)']

        run_test(self)

    def test_Psi4Tetrads_globals(self):

        self.module = 'BSSN.Psi4_tetrads'

        self.module_name = 'Psi4_tetrads'

        self.global_list = ['l4U', 'n4U', 'mre4U', 'mim4U']

        self.function_list = ['Psi4_tetrads()']

        run_test(self)

    # Testing globals for BSSN quantities
    def test_Quantities_Globals(self):

        self.module = 'BSSN.BSSN_quantities'

        self.module_name = 'BSSN_quantities'

        self.global_list = ['hDD', 'aDD', 'lambdaU', 'vetU', 'betU', 'trK', 'cf', 'alpha', 'gammabarDD', 'AbarDD',
                       'LambdabarU', 'betaU', 'BU', 'gammabarUU', 'gammabarDD_dD', 'gammabarDD_dupD',
                       'gammabarDD_dDD', 'GammabarUDD', 'detgammabar', 'detgammabar_dD', 'detgammabar_dDD',
                       'AbarUU', 'AbarUD', 'trAbar', 'AbarDD_dD', 'AbarDD_dupD', 'RbarDD', 'DGammaUDD',
                       'gammabarDD_dHatD', 'DGammaU', 'betaU_dD', 'betaU_dupD', 'betaU_dDD', 'phi_dD',
                       'phi_dupD', 'phi_dDD', 'exp_m4phi', 'phi_dBarD', 'phi_dBarDD']

        self.function_list = ['declare_BSSN_gridfunctions_if_not_declared_already()', 'BSSN_basic_tensors()',
                 'gammabar__inverse_and_derivs()', 'detgammabar_and_derivs()', 'AbarUU_AbarUD_trAbar_AbarDD_dD()',
                 'RicciBar__gammabarDD_dHatD__DGammaUDD__DGammaU()', 'betaU_derivs()', 'phi_and_derivs()']

        run_test(self)

    def test_RHS_Globals(self):

        self.module = 'BSSN.BSSN_RHSs'

        self.module_name = 'BSSN_RHSs'

        self.global_list = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']

        self.function_list = ['BSSN_RHSs()']

        run_test(self)

    def test_gauge_RHSs_Globals(self):

        self.module = 'BSSN.BSSN_gauge_RHSs'

        self.module_name = 'gauge_RHSs'

        self.global_list = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

        self.function_list = ['BSSN_gauge_RHSs()']

        run_test(self)

    def test_T4UU_Globals(self):

        self.module = 'BSSN.BSSN_T4UUmunu_vars'

        self.module_name = 'T4UUmunu_vars'

        self.global_list = ['rho', 'S', 'sD', 'sDD']

        self.function_list = ['define_BSSN_T4UUmunu_rescaled_source_terms()']

        run_test(self)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
