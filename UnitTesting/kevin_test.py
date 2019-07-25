import sys
import cmdline_helper


def kevin_test(module, module_name, global_list, function_list, logging_level='INFO'):

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
        cls.path = r'{}'
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
    print(sys.path[0])
    full_path = sys.path[0] + '/temp_test_file.py'
    f = open(full_path, 'w')
    f.write(string)
    f.close()

    # https://stackoverflow.com/questions/31559473/run-unittests-from-a-different-file
    import unittest
    import importlib
    try:
        temp_test_file = importlib.import_module('temp_test_file')
    except ModuleNotFoundError:
        print('Module not found...waiting 5 seconds')
        import time
        time.sleep(5)
        try:
            temp_test_file = importlib.import_module('temp_test_file')
        except ModuleNotFoundError:
            print('Module still not found. Now exiting without testing.')
            exit(1)
    #import temp_test_file
    import os
    suite = unittest.TestLoader().loadTestsFromModule(temp_test_file)
    unittest.TextTestRunner().run(suite)
    os.remove(full_path)

    # cmdline_helper.Execute_input_string("python temp_test_file.py", 'temp_file.txt')
