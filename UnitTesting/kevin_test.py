import sys


def kevin_test(logging_level, module, module_name, global_list, function_list):
    string = '''
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict

logging.basicConfig(level=logging.{})  

Timer = RepeatedTimer(300, logging.info, '\\nPrinting every 5 minutes to prevent timeouts.\\n')


class TestGlobals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = '{}'
        setup_trusted_values_dict(cls.path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def test_globals(self):

        self.module = '{}'

        self.module_name = '{}'

        self.global_list = {}

        self.function_list = {}

        run_test(self)
        
        
if __name__ == '__main__':
    unittest.main()
'''.format(logging_level.upper(), sys.path[0], module, module_name, global_list, function_list)

    print(string)

    f = open(sys.path[0] + '/temp_test_file.py', 'w')
    f.write(string)
    f.close()

    # import temp_test_file


if __name__ == '__main__':
    kevin_test('INFO', 'UnitTesting.module', 'test_module', ['a', 'b', 'c'], ['set_up()'])
