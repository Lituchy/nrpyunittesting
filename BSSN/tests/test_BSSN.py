from UnitTesting.kevin_test import create_and_run_test


def test_ADM_in_terms_of_BSSN():

    module = 'BSSN.ADM_in_terms_of_BSSN'

    module_name = 'ADM_in_terms_of_BSSN'

    global_list = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma', 'GammaUDD', 'KDD', 'KDDdD']

    function_list = ['ADM_in_terms_of_BSSN()']

    create_and_run_test(module, module_name, global_list, function_list)

def test_BrillLindquist():

    module = 'BSSN.BrillLindquist'

    module_name = 'BrillLindquist'

    global_list = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']

    function_list = ['BrillLindquist(ComputeADMGlobalsOnly = True)']

    create_and_run_test(module, module_name, global_list, function_list)

def test_constraints():

    module = 'BSSN.BSSN_constraints'

    module_name = 'BSSN_constraints'

    global_list = ['H', 'MU']

    function_list = ['BSSN_constraints()']

    create_and_run_test(module, module_name, global_list, function_list)

def test_gauge_RHSs():

    module = 'BSSN.BSSN_gauge_RHSs'

    module_name = 'gauge_RHSs'

    global_list = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

    function_list = ['BSSN_gauge_RHSs()']

    create_and_run_test(module, module_name, global_list, function_list)

def test_Psi4():

    module = 'BSSN.Psi4'

    module_name = 'Psi4'

    global_list = ['psi4_re_pt', 'psi4_im_pt']

    function_list = ['Psi4(specify_tetrad=False)']

    create_and_run_test(module, module_name, global_list, function_list)

def test_Psi4_tetrads():

    module = 'BSSN.Psi4_tetrads'

    module_name = 'Psi4_tetrads'

    global_list = ['l4U', 'n4U', 'mre4U', 'mim4U']

    function_list = ['Psi4_tetrads()']

    create_and_run_test(module, module_name, global_list, function_list)

def ftest_quantities():

    module = 'BSSN.BSSN_quantities'

    module_name = 'BSSN_quantities'

    global_list = ['hDD', 'aDD', 'lambdaU', 'vetU', 'betU', 'trK', 'cf', 'alpha', 'gammabarDD', 'AbarDD', 'LambdabarU',
                   'betaU', 'BU', 'gammabarUU', 'gammabarDD_dD', 'gammabarDD_dupD', 'gammabarDD_dDD', 'GammabarUDD',
                   'detgammabar', 'detgammabar_dD', 'detgammabar_dDD', 'AbarUU', 'AbarUD', 'trAbar', 'AbarDD_dD',
                   'AbarDD_dupD', 'RbarDD', 'DGammaUDD', 'gammabarDD_dHatD', 'DGammaU', 'betaU_dD', 'betaU_dupD',
                   'betaU_dDD', 'phi_dD', 'phi_dupD', 'phi_dDD', 'exp_m4phi', 'phi_dBarD', 'phi_dBarDD']

    function_list = ['declare_BSSN_gridfunctions_if_not_declared_already()', 'BSSN_basic_tensors()',
                     'gammabar__inverse_and_derivs()', 'detgammabar_and_derivs()', 'AbarUU_AbarUD_trAbar_AbarDD_dD()',
                     'RicciBar__gammabarDD_dHatD__DGammaUDD__DGammaU()', 'betaU_derivs()', 'phi_and_derivs()']

    create_and_run_test(module, module_name, global_list, function_list)

def test_RHSs():

    module = 'BSSN.BSSN_RHSs'

    module_name = 'BSSN_RHSs'

    global_list = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']

    function_list = ['BSSN_RHSs()']

    create_and_run_test(module, module_name, global_list, function_list)

def test_ShiftedKerrSchild():

    module = 'BSSN.ShiftedKerrSchild'

    module_name = 'ShiftedKerrSchild'

    global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

    function_list = ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)']

    create_and_run_test(module, module_name, global_list, function_list)

def test_StaticTrumpet():

    module = 'BSSN.StaticTrumpet'

    module_name = 'StaticTrumpet'

    global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

    function_list = ['StaticTrumpet(ComputeADMGlobalsOnly = True)']

    create_and_run_test(module, module_name, global_list, function_list)

def test_T4UUmunu_vars():

    module = 'BSSN.BSSN_T4UUmunu_vars'

    module_name = 'T4UUmunu_vars'

    global_list = ['rho', 'S', 'sD', 'sDD']

    function_list = ['define_BSSN_T4UUmunu_rescaled_source_terms()']

    create_and_run_test(module, module_name, global_list, function_list)

def test_UIUCBlackHole():

    module = 'BSSN.UIUCBlackHole'

    module_name = 'UIUCBlackHole'

    global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

    function_list = ['UIUCBlackHole(ComputeADMGlobalsOnly = True)']

    create_and_run_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    for func in dir():
        if func[0:5] == 'test_':
            exec(func + '()')
