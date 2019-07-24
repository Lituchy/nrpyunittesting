# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict
import sys
import NRPy_param_funcs as par

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
        cls.path = sys.path[0]
        setup_trusted_values_dict(cls.path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def setUp(self):
        # Deleting all attributes of reference_metric before running test
        import reference_metric as rfm
        # from UnitTesting.reload_module import reload_module
        # reload_module(rfm)

    def test_Spherical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'Spherical')

        self.module = 'reference_metric'

        self.module_name = 'rfm_Spherical'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_SinhSpherical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSpherical')

        self.module = 'reference_metric'

        self.module_name = 'rfm_SinhSpherical'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_SinhSphericalv2(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSphericalv2')

        self.module = 'reference_metric'

        self.module_name = 'rfm_SinhSphericalv2'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_NobleSphericalThetaOptionOne(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'NobleSphericalThetaOptionOne')

        self.module = 'reference_metric'

        self.module_name = 'rfm_NobleSphericalThetaOptionOne'

        self.global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(False)']

        run_test(self)

    def test_NobleSphericalThetaOptionTwo(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'NobleSphericalThetaOptionTwo')

        self.module = 'reference_metric'

        self.module_name = 'rfm_NobleSphericalThetaOptionTwo'

        self.global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(False)']

        run_test(self)

    def test_Cylindrical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'Cylindrical')

        self.module = 'reference_metric'

        self.module_name = 'rfm_Cylindrical'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_SinhCylindrical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhCylindrical')

        self.module = 'reference_metric'

        self.module_name = 'rfm_SinhCylindrical'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_SinhCylindricalv2(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhCylindricalv2')

        self.module = 'reference_metric'

        self.module_name = 'rfm_SinhCylindricalv2'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_SymTP(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SymTP')

        self.module = 'reference_metric'

        self.module_name = 'rfm_SymTP'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_SinhSymTP(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSymTP')

        self.module = 'reference_metric'

        self.module_name = 'rfm_SinhSymTP'

        self.global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)

    def test_Cartesian(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'Cartesian')

        self.module = 'reference_metric'

        self.module_name = 'rfm_Cartesian'

        self.global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        self.function_list = ['reference_metric(True)']

        run_test(self)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
