from UnitTesting.create_test import create_test


def test_u0_smallb_Poynting__Cartesian():

    module = 'u0_smallb_Poynting__Cartesian.u0_smallb_Poynting__Cartesian'

    module_name = 'u0sbPoyn'

    function_and_global_dict = {'compute_u0_smallb_Poynting__Cartesian()': ['g4DD', 'u0', 'uD', 'uBcontraction', 'uU',
                                                                            'smallb4U', 'g4UU', 'smallb4D',
                                                                            'smallb2etk', 'PoynSU']}

    create_test(module, module_name, function_and_global_dict, logging_level='DEBUG')


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