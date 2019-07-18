# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.functions_and_globals import functions_and_globals
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds/13151299
# Creates a threaded timer object that prints to the console every 5 minutes
Timer = RepeatedTimer(300, logging.info, "\nPrinting every 5 minutes to prevent timeouts.\n")


# Python unittest class
class TestGlobals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Creating trusted_values_dict.py if it doesn't exist
        import sys
        global path
        path = sys.path[0]
        setup_trusted_values_dict(path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def tearDown(self):
        import grid as gri
        gri.glb_gridfcs_list = []

    # Testing globals
    def test_globals(self):

        module = 'GiRaFFEfood_HO.GiRaFFEfood_HO'

        module_name = 'GiRaFFEfood_HO'

        global_list = ['AD', 'ValenciavU']

        function_list = ['GiRaFFEfood_HO()']

        run_test(self, path, module, module_name, global_list, function_list)

    # Testing globals
    def test_rotator_globals(self):

        module = 'GiRaFFEfood_HO.GiRaFFEfood_HO_Aligned_Rotator'

        module_name = 'GiRaFFEfood_HO_Aligned_Rotator'

        global_list = ['AD', 'ValenciavU']

        function_list = ['GiRaFFEfood_HO_Aligned_Rotator()']

        run_test(self, path, module, module_name, global_list, function_list)

    # Testing globals
    def test_1D_globals(self):

        module = 'GiRaFFEfood_HO.GiRaFFEfood_HO_1D_tests'

        module_name = 'GiRaFFEfood_HO_1D_tests'

        global_list = ['AleftD', 'AcenterD', 'ArightD', 'ValenciavleftU', 'ValenciavcenterU', 'ValenciavrightU']

        function_list = ['GiRaFFEfood_HO_1D_tests()']

        run_test(self, path, module, module_name, global_list, function_list)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
