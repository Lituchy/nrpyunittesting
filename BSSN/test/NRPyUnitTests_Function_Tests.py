
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

        self.assertEqual(functions_and_globals([], []), {'function_list': [], 'global_list': []})

        self.assertEqual(functions_and_globals([], basic_global_list),
                         {'function_list': [], 'global_list': basic_global_list})
        self.assertEqual(functions_and_globals(basic_function_list, []),
                         {'function_list': basic_function_list, 'global_list': []})
        self.assertEqual(functions_and_globals(basic_function_list, basic_global_list),
                         {'function_list': basic_function_list, 'global_list': basic_global_list})

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
        rank2 = [rank1, rank1, rank1]
        rank3 = [rank2]
        self.assertEqual(get_variable_dimension(rank0), (0, 1))
        self.assertEqual(get_variable_dimension(rank1), (1, 3))
        self.assertEqual(get_variable_dimension(rank2), (2, 3))
        self.assertEqual(get_variable_dimension(rank3), (3, 1))

        self.assertEqual(get_variable_dimension(rank3[0]), (2, 3))
        self.assertEqual(get_variable_dimension(rank2[0]), (1, 3))
        self.assertEqual(get_variable_dimension(rank2[1]), (1, 3))
        self.assertEqual(get_variable_dimension([rank2, rank2]), (3, 2))
        self.assertEqual(get_variable_dimension([[[[[rank0]]]]]), (5, 1))

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

    def test_variable_dict_to_list(self):
        from variable_dict_to_list import variable_dict_to_list

        variable_dict = dict()
        result_tuple = [], []
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        variable_dict = {'alpha': 1}
        result_tuple = [1], ['alpha']
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        variable_dict = {'alphaD': [1, 2]}
        result_tuple = [1, 2], ['alphaD[0]', 'alphaD[1]']
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        variable_dict = {'alphaDD': [[1, 2], [4, 3]]}
        result_tuple = [1, 2, 4, 3], ['alphaDD[0][0]', 'alphaDD[0][1]', 'alphaDD[1][0]', 'alphaDD[1][1]']
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        variable_dict = {'aDD': [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [10, 8, 9, 7, 6], [0, 0, 0, 0, 0], [3, 1, 4, 1, 5]]}
        result_tuple = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 10, 8, 9, 7, 6, 0, 0, 0, 0, 0, 3, 1, 4, 1, 5], \
                       ['aDD[0][0]', 'aDD[0][1]', 'aDD[0][2]', 'aDD[0][3]', 'aDD[0][4]',
                        'aDD[1][0]', 'aDD[1][1]', 'aDD[1][2]', 'aDD[1][3]', 'aDD[1][4]',
                        'aDD[2][0]', 'aDD[2][1]', 'aDD[2][2]', 'aDD[2][3]', 'aDD[2][4]',
                        'aDD[3][0]', 'aDD[3][1]', 'aDD[3][2]', 'aDD[3][3]', 'aDD[3][4]',
                        'aDD[4][0]', 'aDD[4][1]', 'aDD[4][2]', 'aDD[4][3]', 'aDD[4][4]']
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        variable_dict = {'alpha': 4, 'beta': 5}
        result_tuple = [4, 5], ['alpha', 'beta']
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        variable_dict = {'alphaD': [1, 2], 'beta': 3}
        result_tuple = [1, 2, 3], ['alphaD[0]', 'alphaD[1]', 'beta']
        self.assertEqual(result_tuple, variable_dict_to_list(variable_dict))

        logging.info('\nAll variable_dict_to_list tests passed.\n')

    def ftest_run_test(self):
        self.assertTrue(False)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()