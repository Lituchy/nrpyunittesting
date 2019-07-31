import sys
import cmdline_helper as cmd
import logging
import os


def create_test(module, module_name, function_and_global_dict, logging_level='INFO', initialization_string=''):

    logging.basicConfig(level=logging_level)

    for function, global_list in function_and_global_dict.items():
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
        setup_trusted_values_dict(cls.path)

    def test_globals(self):

        self.module = '{}'

        self.module_name = '{}'

        self.function = '{}'
        
        self.global_list = {}
        
        self.initialization_string = """{}"""
        
        self.trusted_values_dict_name = '{}_globals'
        
        try:
            run_test(self)
        except AssertionError:
            pass
        else:
            import os
            with open(os.path.join(self.path, 'success.txt'), 'w') as file:
                pass
                
                
if __name__ == '__main__':
    unittest.main()
'''

        trusted_values_dict_name = module_name
        if len(function_and_global_dict) > 1:
            trusted_values_dict_name += '_' + function[0:-2]

        file_string = file_string.format(logging_level.upper(), sys.path[0], module, module_name, function,
                                         global_list, initialization_string, trusted_values_dict_name)

        # with open('UnitTesting/run_test.py', 'r') as file:
        #     run_test_string = file.read()
        #
        # file_string = file_string.replace('run_test(self)', run_test_string)

        logging.debug('temp_test_file.py for:\n\tmodule:   ' + module_name +
                      '\n\tfunction: ' + function + '\n' + file_string)

        full_path = os.path.join(sys.path[0], 'temp_test_file.py')
        print('full path: ' + full_path)

        with open(full_path, 'w') as file:
            file.write(file_string)

        python_string = 'python'
        if sys.version_info[0] == 3:
            python_string += '3'

        cmd.Execute_input_string(python_string + ' ' + full_path)

        try:
            success_file = os.path.join(sys.path[0], 'success.txt')
            open(success_file)
            cmd.delete_existing_files(success_file)
        except IOError:
            logging.error(module_name + ' failed.')
            raise SystemExit
        else:
            logging.info(module_name + ' passed.')

        cmd.delete_existing_files(full_path)
