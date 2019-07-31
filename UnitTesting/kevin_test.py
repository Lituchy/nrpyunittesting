import sys
import cmdline_helper as cmd
import logging


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
        
        # Self-destruct if failed
        try:
            run_test(self)
        except AssertionError:
            import cmdline_helper as cmd
            cmd.delete_existing_files(self.path + '/temp_test_file.py')

                
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

        full_path = sys.path[0] + '/temp_test_file.py'

        with open(full_path, 'w') as file:
            file.write(file_string)

        cmd.Execute_input_string('python ' + full_path)

        try:
            import temp_test_file
        except ImportError:
            logging.error('Module failed.')
            raise SystemExit
        else:
            logging.info('Module passed.')
            cmd.delete_existing_files(full_path)
