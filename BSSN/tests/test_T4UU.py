from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.BSSN_T4UUmunu_vars'

    module_name = 'T4UUmunu_vars'

    global_list = ['rho', 'S', 'sD', 'sDD']

    function_list = ['define_BSSN_T4UUmunu_rescaled_source_terms()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
