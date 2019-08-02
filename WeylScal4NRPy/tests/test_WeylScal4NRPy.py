from UnitTesting.create_test import create_test


def test_WeylScalars_Cartesian():

    module = 'WeylScal4NRPy.WeylScalars_Cartesian'

    module_name = 'WeylScalars_Cartesian'

    function_and_global_dict = {'WeylScalars_Cartesian()': ['psi4r', 'psi4i', 'psi3r', 'psi3i', 'psi2r', 'psi2i', 'psi1r', 'psi1i', 'psi0r', 'psi0i']}

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