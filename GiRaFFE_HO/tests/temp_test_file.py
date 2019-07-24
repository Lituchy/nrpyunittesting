
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict

logging.basicConfig(level=logging.INFO)  

Timer = RepeatedTimer(300, logging.info, '\nPrinting every 5 minutes to prevent timeouts.\n')


class TestGlobals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = '/home/kevin/virtpypy/nrpyunittesting/GiRaFFE_HO/tests'
        setup_trusted_values_dict(cls.path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def test_globals(self):

        self.module = 'GiRaFFE_HO.GiRaFFE_Higher_Order'

        self.module_name = 'GiRaFFE_HO'

        self.global_list = ['uD', 'uU', 'gammaUU', 'gammadet', 'u0alpha', 'alpsqrtgam', 'Stilde_rhsD', 'AevolParen', 'PevolParenU', 'A_rhsD', 'psi6Phi_rhs']

        self.function_list = ['GiRaFFE_Higher_Order()']

        run_test(self)
        
        
if __name__ == '__main__':
    unittest.main()
