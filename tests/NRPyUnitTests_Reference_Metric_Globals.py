# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.functions_and_globals import functions_and_globals
from UnitTesting.RepeatedTimer import RepeatedTimer
from UnitTesting.setup_trusted_values_dict import setup_class
import sys

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
        setup_class(path)

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

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

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_Spherical
        par.set_parval_from_str("reference_metric::CoordSystem", 'Spherical')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_Spherical': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_Spherical)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_Spherical)
        else:
            import importlib
            importlib.reload(rfm_Spherical)

    def test_SinhSpherical(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_SinhSpherical
        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSpherical')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_SinhSpherical': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_SinhSpherical)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_SinhSpherical)
        else:
            import importlib
            importlib.reload(rfm_SinhSpherical)

    def test_SinhSphericalv2(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_SinhSphericalv2
        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSphericalv2')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_SinhSphericalv2': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_SinhSphericalv2)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_SinhSphericalv2)
        else:
            import importlib
            importlib.reload(rfm_SinhSphericalv2)

    def test_NobleSphericalThetaOptionOne(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_NobleSphericalThetaOptionOne
        par.set_parval_from_str("reference_metric::CoordSystem", 'NobleSphericalThetaOptionOne')

        global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_NobleSphericalThetaOptionOne': functions_and_globals(['reference_metric(False)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_NobleSphericalThetaOptionOne)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_NobleSphericalThetaOptionOne)
        else:
            import importlib
            importlib.reload(rfm_NobleSphericalThetaOptionOne)

    def test_NobleSphericalThetaOptionTwo(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_NobleSphericalThetaOptionTwo
        par.set_parval_from_str("reference_metric::CoordSystem", 'NobleSphericalThetaOptionTwo')

        global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_NobleSphericalThetaOptionTwo': functions_and_globals(['reference_metric(False)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_NobleSphericalThetaOptionTwo)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_NobleSphericalThetaOptionTwo)
        else:
            import importlib
            importlib.reload(rfm_NobleSphericalThetaOptionTwo)

    def test_Cylindrical(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_Cylindrical
        par.set_parval_from_str("reference_metric::CoordSystem", 'Cylindrical')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_Cylindrical': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_Cylindrical)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_Cylindrical)
        else:
            import importlib
            importlib.reload(rfm_Cylindrical)

    def test_SinhCylindrical(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_SinhCylindrical
        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhCylindrical')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_SinhCylindrical': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_SinhCylindrical)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_SinhCylindrical)
        else:
            import importlib
            importlib.reload(rfm_SinhCylindrical)

    def test_SinhCylindricalv2(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_SinhCylindricalv2
        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhCylindricalv2')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_SinhCylindricalv2': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_SinhCylindricalv2)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_SinhCylindricalv2)
        else:
            import importlib
            importlib.reload(rfm_SinhCylindricalv2)

    def test_SymTP(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_SymTP
        par.set_parval_from_str("reference_metric::CoordSystem", 'SymTP')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_SymTP': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_SymTP)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_SymTP)
        else:
            import importlib
            importlib.reload(rfm_SymTP)

    def test_SinhSymTP(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_SinhSymTP
        par.set_parval_from_str("reference_metric::CoordSystem", 'SinhSymTP')

        global_list = ['xxmin', 'xxmax', 'UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_SinhSymTP': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_SinhSymTP)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_SinhSymTP)
        else:
            import importlib
            importlib.reload(rfm_SinhSymTP)

    def test_Cartesian(self):

        import trusted_values_dict
        import NRPy_param_funcs as par
        import reference_metric as rfm_Cartesian
        par.set_parval_from_str("reference_metric::CoordSystem", 'Cartesian')

        global_list = ['UnitVectors', 'ReU', 'ReDD', 'ghatDD', 'ghatUU', 'detgammahat',
                       'detgammahatdD', 'detgammahatdDD', 'ReUdD', 'ReUdDD', 'ReDDdD', 'ReDDdDD', 'ghatDDdD',
                       'ghatDDdDD', 'GammahatUDD', 'GammahatUDDdD', 'Cart_to_xx','xxCart','xxSph','scalefactor_orthog']

        mod_dict = {'rfm_Cartesian': functions_and_globals(['reference_metric(True)'], global_list)}

        run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())

        if sys.version_info[0] == 2:
            reload(rfm_Cartesian)
        elif sys.version_info[1] <= 3:
            import imp
            imp.reload(rfm_Cartesian)
        else:
            import importlib
            importlib.reload(rfm_Cartesian)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
