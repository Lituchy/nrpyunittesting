# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
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

    # Testing globals
    def test_globals(self):

        module = 'FishboneMoncriefID.FishboneMoncriefID'

        module_name = 'FishBoneMoncriefID'

        global_list = ['hm1', 'rho_initial', 'IDalpha', 'IDgammaDD', 'IDKDD', 'IDbetaU', 'IDValencia3velocityU']

        function_list = ['FishboneMoncriefID()']

        run_test(self, path, module, module_name, global_list, function_list)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
