from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.Psi4_tetrads'

    module_name = 'Psi4_tetrads'

    global_list = ['l4U', 'n4U', 'mre4U', 'mim4U']

    function_list = ['Psi4_tetrads()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
