from UnitTesting.create_test import create_test


def test_FishboneMoncriefID():

    module = 'FishboneMoncriefID.FishboneMoncriefID'

    module_name = 'FishBoneMoncriefID'

    function_and_global_dict = {'FishboneMoncriefID()': ['hm1', 'rho_initial', 'IDalpha', 'IDgammaDD', 'IDKDD', 'IDbetaU', 'IDValencia3velocityU']}

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
