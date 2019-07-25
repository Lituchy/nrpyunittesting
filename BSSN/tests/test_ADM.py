from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.ADM_in_terms_of_BSSN'

    module_name = 'ADM_in_terms_of_BSSN'

    global_list = ['gammaDD', 'gammaDDdD', 'gammaDDdDD', 'gammaUU', 'detgamma', 'GammaUDD', 'KDD', 'KDDdD']

    function_list = ['ADM_in_terms_of_BSSN()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
