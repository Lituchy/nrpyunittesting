from UnitTesting.create_test import create_test


def test_GiRaFFEfood_HO():

    module = 'GiRaFFEfood_HO.GiRaFFEfood_HO'

    module_name = 'GiRaFFEfood_HO'

    function_and_global_dict = {'GiRaFFEfood_HO()': ['AD', 'ValenciavU']}

    create_test(module, module_name, function_and_global_dict)

def test_GiRaFFEfood_HO_Aligned_Rotator():

    module = 'GiRaFFEfood_HO.GiRaFFEfood_HO_Aligned_Rotator'

    module_name = 'GiRaFFEfood_HO_Aligned_Rotator'

    function_and_global_dict = {'GiRaFFEfood_HO_Aligned_Rotator()': ['AD', 'ValenciavU']}

    create_test(module, module_name, function_and_global_dict)

def test_GiRaFFEfood_HO_1D_tests():

    module = 'GiRaFFEfood_HO.GiRaFFEfood_HO_1D_tests'

    module_name = 'GiRaFFEfood_HO_1D_tests'

    function_and_global_dict = {'GiRaFFEfood_HO_1D_tests()': ['AleftD', 'AcenterD', 'ArightD', 'ValenciavleftU', 'ValenciavcenterU', 'ValenciavrightU']}

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