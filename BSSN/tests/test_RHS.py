from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.BSSN_RHSs'

    module_name = 'BSSN_RHSs'

    global_list = ['cf_rhs', 'trK_rhs', 'lambda_rhsU', 'a_rhsDD', 'h_rhsDD']

    function_list = ['BSSN_RHSs()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
