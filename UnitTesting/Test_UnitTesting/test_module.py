from UnitTesting.create_test import create_test


def test_module_for_testing_no_gamma():

    module = 'module_for_testing'

    module_name = 'test_module'

    function_and_global_dict = {'function(create_gamma=False)': ['alpha', 'betaU'],
                                'function(create_gamma=True)': ['alpha', 'betaU', 'gamma'],
                                'function2(create_gamma=False)': ['alpha2', 'betaU2'],
                                'function2(create_gamma=True)': ['alpha2', 'betaU2', 'gamma2']}

    initialization_string = 'import module_for_testing as mft\nmft.init_function2()'

    initialization_string_dict = {'function2(create_gamma=False)': initialization_string,
                                  'function2(create_gamma=True)': initialization_string}

    create_test(module, module_name, function_and_global_dict, initialization_string_dict=initialization_string_dict)


if __name__ == '__main__':
    failed_functions = []
    for fun in dir():
        if fun[0:5] == 'test_':
            print('\nTesting function ' + str(fun) + '...\n')
            try:
                exec(fun + '()')
            except SystemExit:
                failed_functions.append(fun)

    if failed_functions != []:
        print(failed_functions)
        exit(1)
