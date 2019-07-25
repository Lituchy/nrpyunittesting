from UnitTesting.kevin_test import kevin_test


def test_GiRaFFE_HO():

    logging_level = 'INFO'

    module = 'GiRaFFE_HO.GiRaFFE_Higher_Order'

    module_name = 'GiRaFFE_HO'

    global_list = ['uD', 'uU', 'gammaUU', 'gammadet', 'u0alpha', 'alpsqrtgam', 'Stilde_rhsD', 'AevolParen',
                        'PevolParenU', 'A_rhsD', 'psi6Phi_rhs']

    function_list = ['GiRaFFE_Higher_Order()']

    kevin_test(logging_level, module, module_name, global_list, function_list)


def test_GiRaFFE_HO_v2():

    logging_level = 'INFO'

    module = 'GiRaFFE_HO.GiRaFFE_Higher_Order_v2'

    module_name = 'GiRaFFE_HO_v2'

    global_list = ['gammaUU', 'gammadet', 'SevolParenUD', 'Stilde_rhsD', 'AevolParen', 'PevolParenU', 'A_rhsD',
                   'psi6Phi_rhs']

    function_list = ['GiRaFFE_Higher_Order_v2()']

    kevin_test(logging_level, module, module_name, global_list, function_list)


if __name__ == '__main__':
    test_GiRaFFE_HO()
    test_GiRaFFE_HO_v2()
