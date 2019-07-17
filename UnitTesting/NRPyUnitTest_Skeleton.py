# Skeleton for NRPyUnitTest_File.py.
# TODO: Replace all [VARIABLES]  in the 'TODO' lines according to their specifications and remove the '# TODO'
# So, for example, if you were testing module BrillLindquist in directory BSSN, with name BL, you'd replace
    # '# TODO: import [MODULE] as [MODULE NAME]'
# with
    # 'import BrillLindquist as BL'

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

Timer = RepeatedTimer(300, logging.info, "\nPrinting every 5 minutes to prevent timeouts.\n")


# Python unittest class
class TestBSSNGlobals(unittest.TestCase):

    # Creating trusted_values_dict.py if it doesn't exist and setting [path] variable
    @classmethod
    def setUpClass(cls):
        import sys
        global path
        path = sys.path[0]
        setup_trusted_values_dict(path)

    # Stopping the threaded timer once the tests complete
    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    # Testing globals for your module
    def test_globals(self):

        # If there appears to be an import error, ignore it -- trusted_values_dict.py will be automatically created.
        import trusted_values_dict

        # Note: Even though it says the modules are unused, these imports are vital for run_test to work properly.
        # Their information gets passed into run_test through locals()
        # TODO: import [MODULE] as [MODULE NAME]

        # Creating list of functions to be called
        # TODO: function_list = [LIST CONTAINING STRINGS OF THE FUNCTIONS TO BE CALLED]

        # Creating lists of globals to calculate
        # TODO: global_list = [LIST CONTAINING STRINGS OF THE GLOBALS TO BE TESTED]

        # Creating Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in mod_dict MUST have the same name as the imported module.
        # Example: If you say 'import My_Modules.Module1 as M1', then mod_dict should have the entry 'M1' as a string.
        # TODO: mod_dict = {[STRING REPRESENTATION OF MODULE NAME]: functions_and_globals(function_list, global_list)}

        # Calling run_test with arguments (self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())
        # TODO: run_test(self, mod_dict, trusted_values_dict.trusted_values_dict, path, locals())


# Necessary for unittest class to correctly communicate with other modules
if __name__ == '__main__':
    unittest.main()
