# Necessary imports for unit testing framework
import unittest
import logging
from UnitTesting.run_test import run_test
from UnitTesting.functions_and_globals import functions_and_globals
from UnitTesting.RepeatedTimer import RepeatedTimer
from trusted_values_dict import trusted_values_dict

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
        import os
        path = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        try:
            open(path + '/trusted_values_dict.py', 'r')
        except IOError:
            logging.info('trusted_values_dict.py does not exist. Creating it...\n')
            f = open(path + '/trusted_values_dict.py', 'w+')
            f.write('from mpmath import mpf,mp,mpc\nfrom UnitTesting.standard_constants import precision\n\n'
                    'mp.dps = precision\ntrusted_values_dict = dict()\n\n# Paste your trusted values here!\n')
            logging.error('Automatically failing...please rerun code now that trusted_values_dict.py has been created.')

    @classmethod
    def tearDownClass(cls):
        Timer.stop()

    def tearDown(self):
        import grid as gri
        gri.glb_gridfcs_list = []

    # Testing globals
    def test_evol_globals(self):

        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for run_test to work properly.
        # Their information gets passed into run_test through locals()
        import Maxwell.MaxwellCartesian_Evol as MaxwellCartesian_Evol

        # TODO: Create lists of globals to calculate

        evol_global_list = ['ArhsD', 'ErhsD', 'psi_rhs', 'Gamma_rhs', 'Cviola']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in mod_dict MUST have the same name as the imported module.
        # Example: If you say 'import My_Modules.Module1 as M1', then mod_dict should have the entry 'M1' as a string.
        mod_dict = {'MaxwellCartesian_Evol': functions_and_globals(['MaxwellCartesian_Evol()'], evol_global_list)}

        # TODO: Call run_test with arguments (self, mod_dict, locals())
        run_test(self, mod_dict, trusted_values_dict, locals())

    def test_id_globals(self):
        # TODO: Import modules to be tested
        # Note: Even though it says the modules are unused, these imports are vital for run_test to work properly.
        # Their information gets passed into run_test through locals()
        import Maxwell.MaxwellCartesian_ID as MaxwellCartesian_ID

        # TODO: Create lists of globals to calculate

        id_global_list = ['AidD', 'EidD', 'psi_ID', 'Gamma_ID']

        # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
        # Note that the name of the modules in mod_dict MUST have the same name as the imported module.
        # Example: If you say 'import My_Modules.Module1 as M1', then mod_dict should have the entry 'M1' as a string.
        mod_dict = {'MaxwellCartesian_ID': functions_and_globals(['MaxwellCartesian_ID()'], id_global_list)}

        # TODO: Call run_test with arguments (self, mod_dict, locals())
        run_test(self, mod_dict, trusted_values_dict, locals())


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
