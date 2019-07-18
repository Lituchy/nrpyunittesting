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
        global path
        path = sys.path[0]
        setup_trusted_values_dict(path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    # Testing globals for ADM in terms of BSSN module
    def test_ADM_Globals(self):

        module = 'BSSN.ADM_in_terms_of_BSSN'

        module_name = 'ADM_in_terms_of_BSSN'

        global_list = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma', 'GammaUDD', 'KDD', 'KDDdD']

        function_list = ['ADM_in_terms_of_BSSN()']

        run_test(self, path, module, module_name, global_list, function_list)

    # Testing globals for BSSN constraints
    def test_Constraints_Globals(self):

        module = 'BSSN.BSSN_constraints'

        module_name = 'BSSN_constraints'

        global_list = ['H', 'MU']

        function_list = ['BSSN_constraints()']

        run_test(self, path, module, module_name, global_list, function_list)

    # Testing globals for BSSN exact modules
    def test_BrillLindquist_Globals(self):

        module = 'BSSN.BrillLindquist'

        module_name = 'BrillLindquist'

        global_list = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']

        function_list = ['BrillLindquist(ComputeADMGlobalsOnly = True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_UIUCBlackHole_Globals(self):

        module = 'BSSN.UIUCBlackHole'

        module_name = 'UIUCBlackHole'

        global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        function_list = ['UIUCBlackHole(ComputeADMGlobalsOnly = True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_StaticTrumpet_Globals(self):
        module = 'BSSN.StaticTrumpet'

        module_name = 'StaticTrumpet'

        global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        function_list = ['StaticTrumpet(ComputeADMGlobalsOnly = True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_ShiftedKerrSchild_Globals(self):
        module = 'BSSN.ShiftedKerrSchild'

        module_name = 'ShiftedKerrSchild'

        global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

        function_list = ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)']

        run_test(self, path, module, module_name, global_list, function_list)

    # Testing globals for BSSN Psi4 Globals
    def test_Psi4_Globals(self):

        module = 'BSSN.Psi4'

        module_name = 'Psi4'

        global_list = ['psi4_re_pt', 'psi4_im_pt']

        function_list = ['Psi4(specify_tetrad=False)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_Psi4Tetrads_globals(self):

        module = 'BSSN.Psi4_tetrads'

        module_name = 'Psi4_tetrads'

        global_list = ['l4U', 'n4U', 'mre4U', 'mim4U']

        function_list = ['Psi4_tetrads()']

        run_test(self, path, module, module_name, global_list, function_list)

    # Testing globals for BSSN quantities
    def test_Quantities_Globals(self):

        module = 'BSSN.BSSN_quantities'

        module_name = 'BSSN_quantities'

        global_list = ['hDD', 'aDD', 'lambdaU', 'vetU', 'betU', 'trK', 'cf', 'alpha', 'gammabarDD', 'AbarDD',
                       'LambdabarU', 'betaU', 'BU', 'gammabarUU', 'gammabarDD_dD', 'gammabarDD_dupD',
                       'gammabarDD_dDD', 'GammabarUDD', 'detgammabar', 'detgammabar_dD', 'detgammabar_dDD',
                       'AbarUU', 'AbarUD', 'trAbar', 'AbarDD_dD', 'AbarDD_dupD', 'RbarDD', 'DGammaUDD',
                       'gammabarDD_dHatD', 'DGammaU', 'betaU_dD', 'betaU_dupD', 'betaU_dDD', 'phi_dD',
                       'phi_dupD', 'phi_dDD', 'exp_m4phi', 'phi_dBarD', 'phi_dBarDD']

        function_list = ['declare_BSSN_gridfunctions_if_not_declared_already()', 'BSSN_basic_tensors()',
                 'gammabar__inverse_and_derivs()', 'detgammabar_and_derivs()', 'AbarUU_AbarUD_trAbar_AbarDD_dD()',
                 'RicciBar__gammabarDD_dHatD__DGammaUDD__DGammaU()', 'betaU_derivs()', 'phi_and_derivs()']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_RHS_Globals(self):

        module = 'BSSN.BSSN_RHSs'

        module_name = 'BSSN_RHSs'

        global_list = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']

        function_list = ['BSSN_RHSs()']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_gauge_RHSs_Globals(self):

        module = 'BSSN.BSSN_gauge_RHSs'

        module_name = 'gauge_RHSs'

        global_list = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

        function_list = ['BSSN_gauge_RHSs()']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_T4UU_Globals(self):

        module = 'BSSN.BSSN_T4UUmunu_vars'

        module_name = 'T4UUmunu_vars'

        global_list = ['rho', 'S', 'sD', 'sDD']

        function_list = ['define_BSSN_T4UUmunu_rescaled_source_terms()']

        run_test(self, path, module, module_name, global_list, function_list)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
