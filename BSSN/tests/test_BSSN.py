from UnitTesting.create_test import create_test


def test_ADM_in_terms_of_BSSN():

    module = 'BSSN.ADM_in_terms_of_BSSN'

    module_name = 'ADM_in_terms_of_BSSN'

    function_and_global_dict = {'ADM_in_terms_of_BSSN()': ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma', 
                                                           'GammaUDD', 'KDD', 'KDDdD']}

    create_test(module, module_name, function_and_global_dict)

def test_BrillLindquist():

    module = 'BSSN.BrillLindquist'

    module_name = 'BrillLindquist'

    function_and_global_dict = {'BrillLindquist(ComputeADMGlobalsOnly = True)': ['alphaCart', 'betaCartU', 'BCartU', 
                                                                                 'gammaCartDD', 'KCartDD']}

    create_test(module, module_name, function_and_global_dict)

def test_constraints():

    module = 'BSSN.BSSN_constraints'

    module_name = 'BSSN_constraints'
    
    function_and_global_dict = {'BSSN_constraints()': ['H', 'MU']}

    create_test(module, module_name, function_and_global_dict)

def test_gauge_RHSs():

    module = 'BSSN.BSSN_gauge_RHSs'

    module_name = 'gauge_RHSs'
    
    function_and_global_dict = {'BSSN_gauge_RHSs()': ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']}

    create_test(module, module_name, function_and_global_dict)

def test_Psi4():

    module = 'BSSN.Psi4'

    module_name = 'Psi4'
    
    function_and_global_dict = {'Psi4(specify_tetrad=False)': ['psi4_re_pt', 'psi4_im_pt']}

    create_test(module, module_name, function_and_global_dict)

def test_Psi4_tetrads():

    module = 'BSSN.Psi4_tetrads'

    module_name = 'Psi4_tetrads'
    
    function_and_global_dict = {'Psi4_tetrads()': ['l4U', 'n4U', 'mre4U', 'mim4U']}

    create_test(module, module_name, function_and_global_dict)

def ftest_quantities():

    module = 'BSSN.BSSN_quantities'

    module_name = 'BSSN_quantities'
    
    function_and_global_dict = {'declare_BSSN_gridfunctions_if_not_declared_already()': ['hDD', 'aDD', 'lambdaU', 'vetU', 'betU', 'trK', 'cf', 'alpha'],

                                'BSSN_basic_tensors()': ['gammabarDD', 'AbarDD', 'LambdabarU', 'betaU', 'BU'],

                                'gammabar__inverse_and_derivs()': ['gammabarUU', 'gammabarDD_dD', 'gammabarDD_dupD', 'gammabarDD_dDD', 'GammabarUDD'],

                                'detgammabar_and_derivs()': ['detgammabar', 'detgammabar_dD', 'detgammabar_dDD'],

                                'AbarUU_AbarUD_trAbar_AbarDD_dD()': ['AbarUU', 'AbarUD', 'trAbar', 'AbarDD_dD', 'AbarDD_dupD'],

                                'RicciBar__gammabarDD_dHatD__DGammaUDD__DGammaU()': ['RbarDD', 'DGammaUDD', 'gammabarDD_dHatD', 'DGammaU'],

                                'betaU_derivs()': ['betaU_dD', 'betaU_dupD', 'betaU_dDD'],

                                'phi_and_derivs()': ['phi_dD', 'phi_dupD', 'phi_dDD', 'exp_m4phi', 'phi_dBarD', 'phi_dBarDD']
                                }

#     initialization_string = '''
# import reference_metric as rfm
# rfm.ref_metric__hatted_quantities()
#     '''

    create_test(module, module_name, function_and_global_dict, logging_level='DEBUG')

def test_RHSs():

    module = 'BSSN.BSSN_RHSs'

    module_name = 'BSSN_RHSs'
    
    function_and_global_dict = {'BSSN_RHSs()': ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']}

    create_test(module, module_name, function_and_global_dict)

def test_ShiftedKerrSchild():

    module = 'BSSN.ShiftedKerrSchild'

    module_name = 'ShiftedKerrSchild'
    
    function_and_global_dict = {'ShiftedKerrSchild(ComputeADMGlobalsOnly = True)': ['alphaSph', 'betaSphU', 'BSphU', 
                                                                                    'gammaSphDD', 'KSphDD']}

    create_test(module, module_name, function_and_global_dict)

def test_StaticTrumpet():

    module = 'BSSN.StaticTrumpet'

    module_name = 'StaticTrumpet'
    
    function_and_global_dict = {'StaticTrumpet(ComputeADMGlobalsOnly = True)': ['alphaSph', 'betaSphU', 'BSphU', 
                                                                                'gammaSphDD', 'KSphDD']}

    create_test(module, module_name, function_and_global_dict)

def test_T4UUmunu_vars():

    module = 'BSSN.BSSN_T4UUmunu_vars'

    module_name = 'T4UUmunu_vars'
    
    function_and_global_dict = {'define_BSSN_T4UUmunu_rescaled_source_terms()': ['rho', 'S', 'sD', 'sDD']}

    create_test(module, module_name, function_and_global_dict)

def test_UIUCBlackHole():

    module = 'BSSN.UIUCBlackHole'

    module_name = 'UIUCBlackHole'
    
    function_and_global_dict = {'UIUCBlackHole(ComputeADMGlobalsOnly = True)': ['alphaSph', 'betaSphU', 'BSphU', 
                                                                                'gammaSphDD', 'KSphDD']}

    create_test(module, module_name, function_and_global_dict)


if __name__ == '__main__':
    failed = set()
    for fun in dir():
        if fun[0:5] == 'test_':
            try:
                exec(fun + '()')
            except SystemExit:
                failed.add(True)
            else:
                failed.add(False)

    if failed == set() or True in failed:
        print('Calling exit(1)...')
        exit(1)
