
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

    def test_create_trusted_globals_dict(self):
        from create_trusted_globals_dict import create_trusted_globals_dict
        from mpmath import mpf
        from trusted_values_dict import trusted_values_dict

        mod_dict = dict()
        first_times = []
        self.assertEqual(dict(), create_trusted_globals_dict(mod_dict, first_times))

        mod_dict = {'mod': []}
        first_times = [True]
        self.assertEqual({'mod': dict()}, create_trusted_globals_dict(mod_dict, first_times))

        mod_dict = {'mod': ['hello', 'world']}
        first_times = [True]
        self.assertEqual({'mod': dict()}, create_trusted_globals_dict(mod_dict, first_times))

        with self.assertRaises(KeyError):
            mod_dict = {'mod1': ['hello', 'world']}
            first_times = [False]
            create_trusted_globals_dict(mod_dict, first_times)

        with self.assertRaises(AssertionError):
            mod_dict = {'mod': []}
            first_times = [True, False]
            create_trusted_globals_dict(mod_dict, first_times)

        with self.assertRaises(AssertionError):
            mod_dict = {'mod1': 'hello', 'mod2': 'world'}
            first_times = [True]
            create_trusted_globals_dict(mod_dict, first_times)

        mod_dict = {'BrillLindquist': ['foo', 'bar']}
        first_times = [True]
        self.assertEqual({'BrillLindquist': dict()}, create_trusted_globals_dict(mod_dict, first_times))

        self.maxDiff = None

        mod_dict = {'BrillLindquist': ['foo', 'bar']}
        first_times = [False]
        self.assertEqual({'BrillLindquist': {'alphaCart': mpf('0.12248333157451517615309'), 'betaCartU[0]': mpf('0.0'), 'betaCartU[1]': mpf('0.0'), 'betaCartU[2]': mpf('0.0'), 'BCartU[0]': mpf('0.0'), 'BCartU[1]': mpf('0.0'), 'BCartU[2]': mpf('0.0'), 'gammaCartDD[0][0]': mpf('66.657039107915231916559'), 'gammaCartDD[0][1]': mpf('0.0'), 'gammaCartDD[0][2]': mpf('0.0'), 'gammaCartDD[1][0]': mpf('0.0'), 'gammaCartDD[1][1]': mpf('66.657039107915231916559'), 'gammaCartDD[1][2]': mpf('0.0'), 'gammaCartDD[2][0]': mpf('0.0'), 'gammaCartDD[2][1]': mpf('0.0'), 'gammaCartDD[2][2]': mpf('66.657039107915231916559'), 'KCartDD[0][0]': mpf('0.0'), 'KCartDD[0][1]': mpf('0.0'), 'KCartDD[0][2]': mpf('0.0'), 'KCartDD[1][0]': mpf('0.0'), 'KCartDD[1][1]': mpf('0.0'), 'KCartDD[1][2]': mpf('0.0'), 'KCartDD[2][0]': mpf('0.0'), 'KCartDD[2][1]': mpf('0.0'), 'KCartDD[2][2]': mpf('0.0')}}
                         , create_trusted_globals_dict(mod_dict, first_times))

        mod_dict = {'BrillLindquist': ['foo', 'bar']}
        first_times = [False]
        self.assertEqual({'BrillLindquist': trusted_values_dict['BrillLindquistGlobals']}
                         , create_trusted_globals_dict(mod_dict, first_times))

        mod_dict = {'BrillLindquist': ['foo', 'bar'], 'mod': ['hello world']}
        first_times = [False, True]
        self.assertEqual({'BrillLindquist': trusted_values_dict['BrillLindquistGlobals'], 'mod': dict()}
                         , create_trusted_globals_dict(mod_dict, first_times))

        mod_dict = {'BrillLindquist': 1, 'ShiftedKerrSchild': 2}
        first_times = [False, False]
        self.assertEqual({'BrillLindquist': trusted_values_dict['BrillLindquistGlobals']
                         , 'ShiftedKerrSchild': trusted_values_dict['ShiftedKerrSchildGlobals']}
                         , create_trusted_globals_dict(mod_dict, first_times))

        mod_dict = {'mod1': 1, 'mod2': 2, 'mod3': 3}
        first_times = [True, True, True]
        self.assertEqual({'mod1': dict(), 'mod2': dict(), 'mod3': dict()},
                         create_trusted_globals_dict(mod_dict, first_times))

        logging.info('\nAll create_trusted_globals_dict tests passed.\n')

    def test_list_to_value_list(self):
        from list_to_value_list import list_to_value_list
        from mpmath import mpf
        from sympy.abc import x, y, z

        var_list = []
        self.assertEqual([], list_to_value_list(var_list))

        var_list = [x]
        result_list = [mpf('0.983083687023713543948423277992792')]
        self.assertEqual(result_list, list_to_value_list(var_list))

        var_list = [y]
        result_list = [mpf('0.983083687023713543948423277992792')]
        self.assertEqual(result_list, list_to_value_list(var_list))

        var_list = [x, y]
        result_list = [mpf('0.983083687023713543948423277992792'), mpf('0.663876945807995865736242729317412')]
        self.assertEqual(result_list, list_to_value_list(var_list))

        var_list = [y, x]
        result_list = [mpf('0.663876945807995865736242729317412'), mpf('0.983083687023713543948423277992792')]
        self.assertEqual(result_list, list_to_value_list(var_list))

        var_list = [x, y, z]
        result_list = [mpf('0.983083687023713543948423277992792'), mpf('0.663876945807995865736242729317412'),
                       mpf('0.0865532787281174619276152516348816')]
        self.assertEqual(result_list, list_to_value_list(var_list))

        var_list = [x+y]
        result_list = [mpf('1.6469606328317094096846660073103')]
        self.assertEqual(result_list, list_to_value_list(var_list))

        logging.info('All list_to_value_list tests passed')

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