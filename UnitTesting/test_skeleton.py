from UnitTesting.create_test import create_test


def test_your_module():

    module = 'your_module_location.your_module'

    module_name = 'name_of_your_module'

    function_and_global_dict = {'function_call': ['your global', 'your next global', 'your next next global', 'etc']}

    create_test(module, module_name, function_and_global_dict)


def test_your_next_module():
    # you get the picture
    pass


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