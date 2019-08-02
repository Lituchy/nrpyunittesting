from UnitTesting.create_test import create_test


def test_InitialData_PlaneWave():

    module = 'ScalarWave.InitialData_PlaneWave'

    module_name = 'InitialData_PlaneWave'

    function_and_global_dict = {'InitialData_PlaneWave()': ['uu_ID', 'vv_ID']}

    create_test(module, module_name, function_and_global_dict)


def test_ScalarWave_RHSs():

    module = 'ScalarWave.ScalarWave_RHSs'

    module_name = 'ScalarWave_RHSs'

    function_and_global_dict = {'ScalarWave_RHSs()': ['wavespeed', 'uu_rhs', 'vv_rhs']}

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