from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.BSSN_constraints'

    module_name = 'BSSN_constraints'

    global_list = ['H', 'MU']

    function_list = ['BSSN_constraints()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
