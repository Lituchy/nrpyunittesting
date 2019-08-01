import sys
import cmdline_helper as cmd
import logging
import os


def create_test(module, module_name, function_and_global_dict, logging_level='INFO', initialization_string=''):

    assert type(module_name) == str, "module_name is " + str(type(module_name)) + " -- it should be type str. Please check input for module_name."
    assert type(module) == str, "module is " + str(type(module)) + " -- it should be type str. Please check input for module in " + module_name
    assert type(function_and_global_dict) == dict, "function_and_global_dict is " + str(type(function_and_global_dict)) + " -- it should be type dict. Please check input for function_and_global_dict in " + module_name
    assert len(function_and_global_dict) != 0, "function_and_global_dict is empty -- it must contain at least one entry to be tested. Please check input for function_and_global_dict in " + module_name
    assert type(logging_level) == str, "logging_level is " + str(type(logging_level)) + " -- it should be type str. Please check input for logging_level in " + module_name
    assert type(initialization_string) == str, "initialization_string is " + str(type(initialization_string)) + " -- it should be type str. Please check input for initialization_string in " + module_name

    logging.basicConfig(level=logging_level)

    for function, global_list in function_and_global_dict.items():
        assert type(function) == str, "function in function_and_global_dict is" + str(type(function)) + " -- it should be type str. Please check input for function_and_global_dict in " + module_name
        assert type(global_list) == list, "global_list for function " + function + 'is ' + str(type(global_list)) + " -- it should be type list. Please check input for function_and_global_dict in " + module_name
        assert len(global_list) != 0, "global_list for function " + function + "is empty -- it must contain at least one entry to be tested. Please check input for function " +function + " in " + module_name
        assert all(isinstance(glob, str) for glob in global_list), "global_list in function_and_global_dict contains at least one entry that's not a str. Please check input for function " + function + " in " + module_name
        file_string = '''
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict

logging.basicConfig(level=logging.{})  


class TestGlobals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = r'{}'
        # Create trusted_values_dict.py if it doesn't exist
        setup_trusted_values_dict(cls.path)

    def test_globals(self):

        self.module = '{}'

        self.module_name = '{}'

        self.function = '{}'
        
        self.global_list = {}
        
        self.initialization_string = """{}"""
        
        self.trusted_values_dict_name = '{}_globals'
        
        try:
        
{}
{}
        # Something failed
        except AssertionError:
            pass
        # Nothing failed
        else:
            import os
            with open(os.path.join(self.path, 'success.txt'), 'w') as file:
                pass
                
                
if __name__ == '__main__':
    unittest.main()
'''

        trusted_values_dict_name = module_name

        if len(function_and_global_dict) > 1:
            trusted_values_dict_name += '_' + function.split('(')[0]

        # Copying the lines from run_test.py into our test file
        with open('UnitTesting/run_test.py', 'r') as file:
            run_test_string = file.read().split('def run_test(self):')

        # Properly formatting run_test's imports
        run_test_imports_list = run_test_string[0].split('\n')
        final_run_test_imports_string = ''
        for line in run_test_imports_list:
            if line != '':
                final_run_test_imports_string += '            ' + line + '\n'

        # Properly formatting run_test's function
        run_test_body_list = run_test_string[1].split('\n')
        final_run_test_body_string = ''
        for line in run_test_body_list:
            final_run_test_body_string += '        ' + line + '\n'

        # Formatting file_string with inputs
        file_string = file_string.format(logging_level.upper(), sys.path[0], module, module_name, function,
                                         global_list, initialization_string, trusted_values_dict_name,
                                         final_run_test_imports_string, final_run_test_body_string)

        logging.debug(' Test file for:\n\tmodule:   ' + module_name + '\n\tfunction: ' + function + '\n' + file_string)

        test_file = module_name + '__' + function.split('(')[0] + '__test.py'

        full_path = os.path.join(sys.path[0], test_file)

        with open(full_path, 'w') as file:
            logging.info(' Creating file ' + test_file + ' in ' + sys.path[0] + ' for running test...\n')
            file.write(file_string)

        python_string = 'python'
        if sys.version_info[0] == 3:
            python_string += '3'

        cmd.Execute_input_string(python_string + ' ' + full_path, output=False)

        try:
            success_file = os.path.join(sys.path[0], 'success.txt')
            open(success_file)
            cmd.delete_existing_files(success_file)
        except IOError:
            logging.error(' ...Test for function ' + function + ' in module ' + module_name +
                          ' failed! Please examine test file.')
            raise SystemExit
        else:
            logging.info(' ...Test for function ' + function + ' in module ' + module_name +
                         ' passed! Deleting test file...')
            cmd.delete_existing_files(full_path)
            logging.info(' ...Deletion successful. Test complete.\n')