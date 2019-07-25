from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.BSSN_gauge_RHSs'

    module_name = 'gauge_RHSs'

    global_list = ['alpha_rhs', 'bet_rhsU', 'vet_rhsU']

    function_list = ['BSSN_gauge_RHSs()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
