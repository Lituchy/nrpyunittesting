
import unittest
import logging

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


class TestFunctions(unittest.TestCase):

    def ftest_calc_error(self):
        self.assertTrue(False)

    def ftest_create_trusted_globals_dict(self):
        self.assertTrue(False)

    def ftest_list_to_value_list(self):
        self.assertTrue(False)

    def ftest_evaluate_globals(self):
        self.assertTrue(False)

    def test_functions_and_globals(self):
        from functions_and_globals import functions_and_globals

        basic_function_list = ['func1(), func2()']
        basic_global_list = ['x', 'y', 'z']

        self.assertEqual(functions_and_globals([], []), {'functionList': [], 'globalList': []})

        self.assertEqual(functions_and_globals([], basic_global_list),
                         {'functionList': [], 'globalList': basic_global_list})
        self.assertEqual(functions_and_globals(basic_function_list, []),
                         {'functionList': basic_function_list, 'globalList': []})
        self.assertEqual(functions_and_globals(basic_function_list, basic_global_list),
                         {'functionList': basic_function_list, 'globalList': basic_global_list})

        with self.assertRaises(AssertionError):
            functions_and_globals([1, 'hello', 'world'], [])

        with self.assertRaises(AssertionError):
            functions_and_globals(['hello', 'world'], [2])

        with self.assertRaises(AssertionError):
            functions_and_globals(['hello', 'world', 42], basic_global_list)

        with self.assertRaises(AssertionError):
            functions_and_globals('function()', [])

        with self.assertRaises(AssertionError):
            functions_and_globals([], 'glob')

        logging.info('\nAll functions_and_globals tests passed.\n')

    def test_get_variable_dimension(self):
        from get_variable_dimension import get_variable_dimension

        rank0 = 4
        rank1 = [rank0, rank0+1, rank0]
        rank2 = [rank1, rank1]
        rank3 = [rank2]
        self.assertEqual(get_variable_dimension(rank0), 0)
        self.assertEqual(get_variable_dimension(rank1), 1)
        self.assertEqual(get_variable_dimension(rank2), 2)
        self.assertEqual(get_variable_dimension(rank3), 3)

        self.assertEqual(get_variable_dimension(rank3[0]), 2)
        self.assertEqual(get_variable_dimension(rank2[0]), 1)
        self.assertEqual(get_variable_dimension(rank2[1]), 1)
        self.assertEqual(get_variable_dimension([rank2, rank2]), 3)
        self.assertEqual(get_variable_dimension([[[[[rank0]]]]]), 5)

        with self.assertRaises(IndexError):
            get_variable_dimension([])

        logging.info('\nAll get_variable_dimension tests passed.\n')

    def test_is_first_time(self):
        from is_first_time import is_first_time

        mod_dict = {'BrillLindquist': 'Hello World'}
        fake_mod_dict = {'fake_module': 'Goodbye World'}

        self.assertEqual(is_first_time({}), [])

        self.assertEqual(is_first_time(mod_dict), [False])
        self.assertEqual(is_first_time(fake_mod_dict), [True])

        mod_dict.update(fake_mod_dict)

        self.assertEqual(is_first_time(mod_dict), [False, True])

        mod_dict_wrong_capitalization = {'brillLindquist': 2}

        self.assertEqual(is_first_time(mod_dict_wrong_capitalization), [True])

        logging.info('\nAll is_first_time tests passed.\n')

    def ftest_list_to_value_list(self):
        self.assertTrue(False)

    def ftest_module_dict_to_list(self):
        self.assertTrue(False)

    def ftest_run_test(self):
        self.assertTrue(False)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()