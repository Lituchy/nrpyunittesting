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
        cls.path = sys.path[0]
        setup_trusted_values_dict(cls.path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def setUp(self):
        import grid as gri
        gri.glb_gridfcs_list = []

    def test_globals(self):

        self.module = 'GiRaFFE_HO.GiRaFFE_Higher_Order'

        self.module_name = 'GiRaFFE_HO'

        self.global_list = ['uD', 'uU', 'gammaUU', 'gammadet', 'u0alpha', 'alpsqrtgam', 'Stilde_rhsD', 'AevolParen',
                            'PevolParenU', 'A_rhsD', 'psi6Phi_rhs']

        self.function_list = ['GiRaFFE_Higher_Order()']

        run_test(self)

    def test_globals_v2(self):

        self.module = 'GiRaFFE_HO.GiRaFFE_Higher_Order_v2'

        self.module_name = 'GiRaFFE_HO_v2'

        self.global_list = ['gammaUU', 'gammadet', 'SevolParenUD', 'Stilde_rhsD', 'AevolParen', 'PevolParenU', 'A_rhsD',
                            'psi6Phi_rhs']

        self.function_list = ['GiRaFFE_Higher_Order_v2()']

        run_test(self)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
