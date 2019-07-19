# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.functions_and_globals import functions_and_globals
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
        global path
        path = sys.path[0]
        setup_trusted_values_dict(path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def setUp(self):
        # Deleting all attributes of reference_metric before running test
        import reference_metric as rfm
        from UnitTesting.reload_module import reload_module
        reload_module(rfm)
        for attr in dir(rfm):
            if attr[0:2] != '__':
                delattr(rfm, attr)
        reload_module(rfm)


    # Testing globals for reference_metric
    def ftest_reference_metric_globals(self):

        import trusted_values_dict
        import NRPy_param_funcs as par

        # Globals used by all coordinate systems
        basic_global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat', 'detgammahatdD',
                             'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD', 'ghatDDdDD',
                             'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        # Dictionary of coordinate systems and their additional globals
        coord_dict = {'Spherical': ('True', ['xxmin', 'xxmax']), 'SinhSpherical': ('True', []),
                      'SinhSphericalv2': ('True', []), 'NobleSphericalThetaOptionOne': ('False', []),
                      'NobleSphericalThetaOptionTwo': ('False', []), 'Cylindrical': ('True', []),
                      'SinhCylindrical': ('True', []), 'SinhCylindricalv2': ('True', []), 'SymTP': ('True', []),
                      'SinhSymTP': ('True', []), 'Cartesian': ('True', [])}

        #coord_dict = {'Spherical': ('True', ['xxmin', 'xxmax']), 'SinhCylindricalv2': ('True', [])}

        import sys

        # For each module and its respective boolean and additional globals
        for coord, bool_global_tuple in coord_dict.items():

            # Import module based on string
            exec('import reference_metric as rfm_' + coord)

            # Set reference metric
            par.set_parval_from_str("reference_metric::CoordSystem", coord)

            # Create mod_dict
            global_list = bool_global_tuple[1] + basic_global_list
            mod_dict = {('rfm_' + coord): functions_and_globals(['reference_metric(' + bool_global_tuple[0] + ')'],
                                                                global_list)}

            # Run test and delete old entry
            run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

            if sys.version_info[0] == 2:
                reload(locals()['rfm_' + coord])
            elif sys.version_info[1] <= 3:
                import imp
                imp.reload(locals()['rfm_' + coord])
            else:
                import importlib
                importlib.reload(locals()['rfm_' + coord])

    def test_Spherical(self):

        #par.set_parval_from_str("reference_metric::CoordSystem", 'Spherical')

        module = 'reference_metric'

        module_name = 'rfm_Spherical'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_SinhSpherical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSpherical')

        module = 'reference_metric'

        module_name = 'rfm_SinhSpherical'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_SinhSphericalv2(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSphericalv2')

        module = 'reference_metric'

        module_name = 'rfm_SinhSphericalv2'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_NobleSphericalThetaOptionOne(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'NobleSphericalThetaOptionOne')

        module = 'reference_metric'

        module_name = 'rfm_NobleSphericalThetaOptionOne'

        global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(False)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_NobleSphericalThetaOptionTwo(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'NobleSphericalThetaOptionTwo')

        module = 'reference_metric'

        module_name = 'rfm_NobleSphericalThetaOptionTwo'

        global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(False)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_Cylindrical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'Cylindrical')

        module = 'reference_metric'

        module_name = 'rfm_Cylindrical'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_SinhCylindrical(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhCylindrical')

        module = 'reference_metric'

        module_name = 'rfm_SinhCylindrical'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_SinhCylindricalv2(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhCylindricalv2')

        module = 'reference_metric'

        module_name = 'rfm_SinhCylindricalv2'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_SymTP(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SymTP')

        module = 'reference_metric'

        module_name = 'rfm_SymTP'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_SinhSymTP(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSymTP')

        module = 'reference_metric'

        module_name = 'rfm_SinhSymTP'

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)

    def test_Cartesian(self):

        par.set_parval_from_str("reference_metric::CoordSystem", 'Cartesian')

        module = 'reference_metric'

        module_name = 'rfm_Cartesian'

        global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        function_list = ['reference_metric(True)']

        run_test(self, path, module, module_name, global_list, function_list)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
