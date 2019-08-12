from UnitTesting.create_test import create_test


def test_FishboneMoncriefID():

    module = 'FishboneMoncriefID.FishboneMoncriefID'

    module_name = 'FishBoneMoncriefID'

    function_and_global_dict = {'FishboneMoncriefID()': ['hm1', 'rho_initial', 'IDalpha', 'IDgammaDD', 'IDKDD', 'IDbetaU', 'IDValencia3velocityU']}

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
