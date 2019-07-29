import sys
import cmdline_helper as cmd


def create_and_run_test(module, module_name, global_list, function_list, logging_level='INFO', initialization_string = ''):
    string = '''
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict

logging.basicConfig(level=logging.{})  

# Timer = RepeatedTimer(300, logging.info, '\\nPrinting every 5 minutes to prevent timeouts.\\n')


class TestGlobals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = r'{}'
        setup_trusted_values_dict(cls.path)

#   @classmethod
#   def tearDownClass(cls):
#       Timer.stop()

    def test_globals(self):

        self.module = '{}'

        self.module_name = '{}'

        self.global_list = {}

        self.function_list = {}
        
        self.initialization_string = '{}'

        run_test(self)
        
        
if __name__ == '__main__':
    unittest.main()
'''.format(logging_level.upper(), sys.path[0], module, module_name, global_list, function_list, initialization_string)

    import os
    full_path = sys.path[0] + '/temp_test_file.py'
    f = open(full_path, 'w')
    f.write(string)
    f.close()

    cmd.Execute_input_string('python ' + full_path, os.devnull)
    os.remove(full_path)
