import sys
import cmdline_helper as cmd
import logging


def create_test(module, module_name, function_and_global_dict, logging_level='INFO', initialization_string=''):

    exec('logging.basicConfig(level=logging.{})'.format(logging_level))

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

        run_test(self)
        
        
if __name__ == '__main__':
    unittest.main()
'''
        trusted_values_dict_name = module_name
        if len(function_and_global_dict) > 1:
            trusted_values_dict_name += '_' + function[0:-2]

        file_string = file_string.format(logging_level.upper(), sys.path[0], module, module_name, function,
                                         global_list, initialization_string, trusted_values_dict_name)

        logging.debug('temp_test_file.py for:\n\tmodule:   ' + module_name +
                      '\n\tfunction: ' + function + '\n' + file_string)
        full_path = sys.path[0] + '/temp_test_file.py'
        f = open(full_path, 'w')
        f.write(file_string)
        f.close()

        cmd.Execute_input_string('python ' + full_path)
        cmd.delete_existing_files(full_path)
