from UnitTesting.create_test import create_test


def test_u0_smallb_Poynting__Cartesian():

    module = 'u0_smallb_Poynting__Cartesian.u0_smallb_Poynting__Cartesian'

    module_name = 'u0sbPoyn'

    function_and_global_dict = {'compute_u0_smallb_Poynting__Cartesian()': ['g4DD', 'u0', 'uD', 'uBcontraction', 'uU',
                                                                            'smallb4U', 'g4UU', 'smallb4D',
                                                                            'smallb2etk', 'PoynSU']}

    create_test(module, module_name, function_and_global_dict)

def test_abcd():
    print('\n\n\nabcd\n\n\n')


if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 3:
        failed_functions = []
        for fun in dir():
            if fun[0:5] == 'test_':
                print('\nTesting function ' + str(fun) + '...\n')
                try:
                    exec(fun + '()')
                except SystemExit:
                    failed_functions.append(fun)

        if failed_functions != []:
            import sys, os
            with open(os.path.join('UnitTesting', 'failed_tests.txt'), 'a') as file:
                file.write(sys.argv[0] + ': ' + str(failed_functions) + '\n')
            exit(1)

    else:
        import ast
        function_list = ast.literal_eval(sys.argv[4])
        for function in function_list:
            globals()[function]()

