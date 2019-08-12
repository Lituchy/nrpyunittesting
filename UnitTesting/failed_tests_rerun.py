

def failed_tests_rerun():
    import os

    with open(os.path.join('UnitTesting', 'failed_tests.txt'), 'r') as file:
        file_text_list = file.readlines()

    for line in file_text_list[2:]:
        path, function_list = line.split(': ', 1)
        print(path, function_list)
        import UnitTesting.Test_UnitTesting.test_module as mod
        mod.test_module_for_testing_no_gamma(logging_level='DEBUG')


if __name__ == '__main__':
    failed_tests_rerun()
