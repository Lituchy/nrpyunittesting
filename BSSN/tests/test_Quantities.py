from UnitTesting.kevin_test import kevin_test


def test():

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

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
