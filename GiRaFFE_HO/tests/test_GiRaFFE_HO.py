from UnitTesting.kevin_test import kevin_test


def test_GiRaFFE_HO():

    module = 'GiRaFFE_HO.GiRaFFE_Higher_Order'

    module_name = 'GiRaFFE_HO'

    global_list = ['uD', 'uU', 'gammaUU', 'gammadet', 'u0alpha', 'alpsqrtgam', 'Stilde_rhsD', 'AevolParen',
                   'PevolParenU', 'A_rhsD', 'psi6Phi_rhs']

    function_list = ['GiRaFFE_Higher_Order()']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test_GiRaFFE_HO()