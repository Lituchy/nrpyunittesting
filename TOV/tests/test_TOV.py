from UnitTesting.create_test import create_test


def test_TOV_ADM_T4UUmunu():

    module = 'TOV.TOV_ADM_T4UUmunu'

    module_name = 'TOV_ADM_T4UUmunu'

    function_and_global_dict = {'TOV_ADM_T4UUmunu(True)': ['r', 'th', 'ph', 'gammaSphDD', 'KSphDD', 'alphaSph', 'betaSphU', 'BSphU', 'T4UU']}

    create_test(module, module_name, function_and_global_dict)


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
        import sys
        with open(sys.argv[2], 'a') as file:
            file.write(sys.argv[0] + ': ' + str(failed_functions) + '\n')
        exit(1)
