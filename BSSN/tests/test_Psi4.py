from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.Psi4'

    module_name = 'Psi4'

    global_list = ['psi4_re_pt', 'psi4_im_pt']

    function_list = ['Psi4(specify_tetrad=False)']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
