from UnitTesting.create_test import create_test


def ftest_GiRaFFE_HO():

    module = 'GiRaFFE_HO.GiRaFFE_Higher_Order'

    module_name = 'GiRaFFE_HO'

    function_and_global_dict = {'GiRaFFE_Higher_Order()': ['uD', 'uU', 'gammaUU', 'gammadet', 'u0alpha', 'alpsqrtgam',
                                                             'Stilde_rhsD', 'AevolParen', 'PevolParenU', 'A_rhsD',
                                                             'psi6Phi_rhs']}

    create_test(module, module_name, function_and_global_dict)

def test_GiRaFFE_HO_v2():

    module = 'GiRaFFE_HO.GiRaFFE_Higher_Order_v2'

    module_name = 'GiRaFFE_HO_v2'

    function_and_global_dict = {'GiRaFFE_Higher_Order_v2()': ['gammaUU', 'gammadet', 'SevolParenUD', 'Stilde_rhsD',
                                                              'AevolParen', 'PevolParenU', 'A_rhsD', 'psi6Phi_rhs']}

    create_test(module, module_name, function_and_global_dict)


if __name__ == '__main__':
    failed = set()
    for fun in dir():
        if fun[0:5] == 'test_':
            print('\nTesting function ' + str(fun) + '...\n')
            try:
                exec(fun + '()')
            except SystemExit:
                failed.add(True)
            else:
                failed.add(False)

    if failed == set() or True in failed:
        exit(1)
