import unittest
import logging
from sys import version_info

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


class TestFunctions(unittest.TestCase):

    def test_calc_error(self):

        if version_info[0] == 2 or version_info[1] < 4:
            from UnitTesting.calc_error import calc_error
            from testfixtures import LogCapture
            from mpmath import mpf, mp
            from datetime import date
            from UnitTesting.standard_constants import precision

            mp.dps = precision

            mod = 'TestModule'

            calculated_dict = {}
            trusted_dict = {}

            self.assertEqual(True, calc_error(mod, calculated_dict, trusted_dict))

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict = {}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a']")
            )

            calculated_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}
            trusted_dict = {}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']")
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict =    {'b': mpf('2.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a']"),
                ('root', 'ERROR', '\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['b']")
            )

            calculated_dict = {'a': mpf('2.0'), 'b': mpf('3.0')}
            trusted_dict =    {'c': mpf('1.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']"),
                ('root', 'ERROR', '\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c']")
            )

            calculated_dict = {'a': mpf('2.0'), 'b': mpf('3.0')}
            trusted_dict =    {'a': mpf('1.0'), 'c': mpf('4.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['b']"),
                ('root', 'ERROR', '\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c']")
            )

            calculated_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}
            trusted_dict =    {'c': mpf('3.0'), 'd': mpf('4.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']"),
                ('root', 'ERROR', '\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c', 'd']")
            )

            calculated_dict = {'b': mpf('1.0'), 'a': mpf('2.0')}
            trusted_dict =    {'c': mpf('3.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'ERROR', '\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.'),
                ('root', 'ERROR', '\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']"),
                ('root', 'ERROR', '\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c']")
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict =    {'a': mpf('1.0')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                 ': Trusted:    ' + '1.0' + '\n')
            )

            calculated_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}
            trusted_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                 ': Trusted:    ' + '1.0' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '2.0' + '\nTestModule: ' + 'b' +
                 ': Trusted:    ' + '2.0' + '\n')
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict =    {'a': mpf('2.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                 ': Trusted:    ' + '2.0' + '\n'),
                ('root', 'ERROR', '\n\nVariable(s) ' + "['a']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '1.0' + "')}\n\n" +
                 '#####')
            )

            calculated_dict = {'a': mpf('0.0')}
            trusted_dict =    {'a': mpf('0.0')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' + '\nTestModule: ' + 'a'
                 + ': Trusted:    ' + '0.0' + '\n')
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict =    {'a': mpf('1.00000000000000010000000000000')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a'
                 + ': Trusted:    ' + '1.0000000000000001' + '\n')
            )

            calculated_dict = {'a': mpf('0.0')}
            trusted_dict =    {'a': mpf('0.0000000000000001')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' + '\nTestModule: ' + 'a'
                 + ': Trusted:    ' + '1.0e-16' + '\n')
            )

            calculated_dict = {'b': mpf('0.0')}
            trusted_dict =    {'b': mpf('0.000000000000001')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '0.0' + '\nTestModule: ' + 'b'
                 + ': Trusted:    ' + '1.0e-15' + '\n'),
                ('root', 'ERROR', '\n\nVariable(s) ' + "['b']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'b'" + ": mpf('" + '0.0' + "')}\n\n" +
                 '#####')
            )

            calculated_dict = {'a': mpf('0.0000000000000001')}
            trusted_dict =    {'a': mpf('0.0')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0e-16' + '\nTestModule: ' + 'a'
                 + ': Trusted:    ' + '0.0' + '\n')
            )

            calculated_dict = {'alpha': mpf('0.000000000000001')}
            trusted_dict =    {'alpha': mpf('0.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'alpha' + ': Calculated: ' + '1.0e-15' + '\nTestModule: ' + 'alpha'
                 + ': Trusted:    ' + '0.0' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['alpha']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'alpha'" + ": mpf('" + '1.0e-15' +
                 "')}\n\n#####")
            )

            calculated_dict = {'f': mpf('123.012345678901234567890123456789')}
            trusted_dict =    {'f': mpf('123.012345678901234567890123456789')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'f' + ': Calculated: ' + '123.012345678901234567890123457' +
                 '\nTestModule: ' + 'f' + ': Trusted:    ' + '123.012345678901234567890123457' + '\n')
            )

            calculated_dict = {'f': mpf('123.012345678101234567890123457')}
            trusted_dict =    {'f': mpf('123.012345678901234567890123457')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'f' + ': Calculated: ' + '123.012345678101234567890123457' +
                 '\nTestModule: ' + 'f' + ': Trusted:    ' + '123.012345678901234567890123457' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['f']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'f'" + ": mpf('" +
                 '123.012345678101234567890123457' + "')}\n\n#####")
            )

            calculated_dict = {'f': mpf('123.012345678901234567890123456')}
            trusted_dict =    {'f': mpf('123.012345678901234567890123457')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'f' + ': Calculated: ' + '123.012345678901234567890123456' +
                 '\nTestModule: ' + 'f' + ': Trusted:    ' + '123.012345678901234567890123457' + '\n'),
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0')}
            trusted_dict =    {'a': mpf('0.0'), 'b': mpf('1.0')}

            with LogCapture() as log:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.0' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'),
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0')}
            trusted_dict =    {'a': mpf('0.1'), 'b': mpf('1.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.1' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['a']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                 "'b'" + ": mpf('1.0')" + "}\n\n#####")
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.1')}
            trusted_dict =    {'a': mpf('0.1'), 'b': mpf('1.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.1' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.1' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['a', 'b']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                 "'b'" + ": mpf('1.1')" + "}\n\n#####")
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.1')}
            trusted_dict =    {'a': mpf('0.0'), 'b': mpf('1.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.0' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.1' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['b']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                 "'b'" + ": mpf('1.1')" + "}\n\n#####")
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0'), 'c': mpf('2.0')}
            trusted_dict = {'a': mpf('0.2'), 'b': mpf('1.2'), 'c': mpf('2.2')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.2' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.2' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'c' + ': Calculated: ' + '2.0' +
                 '\nTestModule: ' + 'c' + ': Trusted:    ' + '2.2' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['a', 'b', 'c']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                 "'b'" + ": mpf('1.0')" + ", " + "'c'" + ": mpf('" + '2.0' + "')" "}\n\n#####")
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0'), 'c': mpf('2.0')}
            trusted_dict = {'a': mpf('0.2'), 'b': mpf('1.0'), 'c': mpf('2.2')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.2' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'c' + ': Calculated: ' + '2.0' +
                 '\nTestModule: ' + 'c' + ': Trusted:    ' + '2.2' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['a', 'c']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                 "'b'" + ": mpf('1.0')" + ", " + "'c'" + ": mpf('" + '2.0' + "')" "}\n\n#####")
            )

            calculated_dict = {'c': mpf('2.0'), 'a': mpf('0.0'), 'b': mpf('1.0')}
            trusted_dict = {'c': mpf('2.2'), 'a': mpf('0.2'), 'b': mpf('1.0')}

            with LogCapture() as log:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            log.check(
                ('root', 'DEBUG', '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                 '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.2' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                 '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'),
                ('root', 'DEBUG', '\nTestModule: ' + 'c' + ': Calculated: ' + '2.0' +
                 '\nTestModule: ' + 'c' + ': Trusted:    ' + '2.2' + '\n'),
                ('root',
                 'ERROR', '\n\nVariable(s) ' + "['a', 'c']" + ' in module TestModule failed. Please check values.\n\nIf you '
                 + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                 "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                 'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                 + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                 " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                 "'b'" + ": mpf('1.0')" + ", " + "'c'" + ": mpf('" + '2.0' + "')" "}\n\n#####")
            )

            logging.info('\nAll calc_error tests passed.\n')

        else:

            from UnitTesting.calc_error import calc_error
            from mpmath import mpf, mp
            from datetime import date
            from UnitTesting.standard_constants import precision

            mp.dps = precision

            mod = 'TestModule'

            calculated_dict = {}
            trusted_dict = {}

            self.assertEqual(True, calc_error(mod, calculated_dict, trusted_dict))

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict = {}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                ['ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                 'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a']"])

            calculated_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}
            trusted_dict = {}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                 'ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                 'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']"
                ])

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict = {'b': mpf('2.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                    'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a']",
                    'ERROR:root:\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['b']"
                ]
            )

            calculated_dict = {'a': mpf('2.0'), 'b': mpf('3.0')}
            trusted_dict = {'c': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                    'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']",
                    'ERROR:root:\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c']"
                ]
            )

            calculated_dict = {'a': mpf('2.0'), 'b': mpf('3.0')}
            trusted_dict = {'a': mpf('1.0'), 'c': mpf('4.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                    'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['b']",
                    'ERROR:root:\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c']"
                ]
            )

            calculated_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}
            trusted_dict = {'c': mpf('3.0'), 'd': mpf('4.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                    'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']",
                    'ERROR:root:\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c', 'd']"
                ]
            )

            calculated_dict = {'b': mpf('1.0'), 'a': mpf('2.0')}
            trusted_dict = {'c': mpf('3.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'ERROR:root:\n\tTestModule: Calculated dictionary and trusted dictionary have different variables.',
                    'ERROR:root:\n\tCalculated Dictionary variables not in Trusted Dictionary: \n\t' + "['a', 'b']",
                    'ERROR:root:\n\tTrusted Dictionary variables not in Calculated Dictionary: \n\t' + "['c']"
                ]
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict = {'a': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                 'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                 ': Trusted:    ' + '1.0' + '\n'
                ]
            )

            calculated_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}
            trusted_dict = {'a': mpf('1.0'), 'b': mpf('2.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                 'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                 ': Trusted:    ' + '1.0' + '\n',
                 'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '2.0' + '\nTestModule: ' + 'b' +
                 ': Trusted:    ' + '2.0' + '\n'
                ]
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict = {'a': mpf('2.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                    ': Trusted:    ' + '2.0' + '\n',
                    'ERROR:root:' +
                    '\n\nVariable(s) ' + "['a']" + ' in module TestModule failed. Please check values.\n\nIf you are ' +
                    'confident that the newly calculated values are correct, comment out the old trusted values for ' +
                    "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                    'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be ' +
                    'changed. Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) +
                    '\n# Reason for changing' + " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" +
                    ": mpf('" + '1.0' + "')}\n\n#####"
                ]
            )

            calculated_dict = {'a': mpf('0.0')}
            trusted_dict = {'a': mpf('0.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' + '\nTestModule: ' + 'a' +
                    ': Trusted:    ' + '0.0' + '\n'
                ]
            )

            calculated_dict = {'a': mpf('1.0')}
            trusted_dict = {'a': mpf('1.00000000000000010000000000000')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0' + '\nTestModule: ' + 'a' +
                    ': Trusted:    ' + '1.0000000000000001' + '\n'
                ]
            )

            calculated_dict = {'a': mpf('0.0')}
            trusted_dict = {'a': mpf('0.0000000000000001')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' + '\nTestModule: ' + 'a' +
                    ': Trusted:    ' + '1.0e-16' + '\n'
                ]
            )

            calculated_dict = {'b': mpf('0.0')}
            trusted_dict = {'b': mpf('0.000000000000001')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '0.0' + '\nTestModule: ' + 'b'
                    + ': Trusted:    ' + '1.0e-15' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['b']" + ' in module TestModule failed. Please check values.\n\nIf'
                    + ' you are confident that the newly calculated values are correct, comment out the old trusted ' +
                    'values for ' + "'TestModuleGlobals' in trusted_values_dict and copy the following code between " +
                    "the ##### into " + 'trusted_values_dict. Make sure to fill out the TODO comment describing why ' +
                    'the values had to be changed. Then re-run test script.\n#####\n\n# Generated on: ' +
                    str(date.today()) + '\n# Reason for changing' +
                    " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'b'" + ": mpf('" + '0.0' +
                    "')}\n\n#####"
                ]
            )

            calculated_dict = {'a': mpf('0.0000000000000001')}
            trusted_dict = {'a': mpf('0.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '1.0e-16' + '\nTestModule: ' + 'a'
                    + ': Trusted:    ' + '0.0' + '\n'
                ]
            )

            calculated_dict = {'alpha': mpf('0.000000000000001')}
            trusted_dict = {'alpha': mpf('0.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'alpha' + ': Calculated: ' + '1.0e-15' + '\nTestModule: ' +
                    'alpha' + ': Trusted:    ' + '0.0' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['alpha']" + ' in module TestModule failed. Please check values.' +
                    '\n\nIf you are confident that the newly calculated values are correct, comment out the old ' +
                    'trusted values for ' + "'TestModuleGlobals' in trusted_values_dict and copy the following code" +
                    " between the ##### into " + 'trusted_values_dict. Make sure to fill out the TODO comment' +
                    ' describing why the values had to be changed. Then re-run test script.\n#####\n\n# Generated on: '
                    + str(date.today()) + '\n# Reason for changing values:' +
                    " TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'alpha'" + ": mpf('" + '1.0e-15' +
                    "')}\n\n#####"
                ]
            )

            calculated_dict = {'f': mpf('123.012345678901234567890123456789')}
            trusted_dict = {'f': mpf('123.012345678901234567890123456789')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'f' + ': Calculated: ' + '123.012345678901234567890123457' +
                    '\nTestModule: ' + 'f' + ': Trusted:    ' + '123.012345678901234567890123457' + '\n'
                ]
            )

            calculated_dict = {'f': mpf('123.012345678101234567890123457')}
            trusted_dict = {'f': mpf('123.012345678901234567890123457')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'f' + ': Calculated: ' + '123.012345678101234567890123457' +
                    '\nTestModule: ' + 'f' + ': Trusted:    ' + '123.012345678901234567890123457' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['f']" + ' in module TestModule failed. Please check values.\n\n' +
                    'If you are confident that the newly calculated values are correct, comment out the old trusted ' +
                    'values for ' + "'TestModuleGlobals' in trusted_values_dict and copy the following code between" +
                    ' the ##### into trusted_values_dict. Make sure to fill out the TODO comment describing why the ' +
                    'values had to be changed. Then re-run test script.\n#####\n\n# Generated on: '
                    + str(date.today()) + '\n# Reason for changing values: ' +
                    "TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'f'" + ": mpf('" +
                    '123.012345678101234567890123457' + "')}\n\n#####"
                ]
            )

            calculated_dict = {'f': mpf('123.012345678901234567890123456')}
            trusted_dict = {'f': mpf('123.012345678901234567890123457')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'f' + ': Calculated: ' + '123.012345678901234567890123456' +
                    '\nTestModule: ' + 'f' + ': Trusted:    ' + '123.012345678901234567890123457' + '\n'
                ]
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0')}
            trusted_dict = {'a': mpf('0.0'), 'b': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertTrue(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.0' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n'
                ]
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0')}
            trusted_dict = {'a': mpf('0.1'), 'b': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.1' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['a']" + ' in module TestModule failed. Please check values.\n\n' +
                    'If you are confident that the newly calculated values are correct, comment out the old trusted ' +
                    'values for ' + "'TestModuleGlobals' in trusted_values_dict and copy the following code between" +
                    ' the ##### into trusted_values_dict. Make sure to fill out the TODO comment describing why the' +
                    ' values had to be changed. Then re-run test script.\n#####\n\n# Generated on: ' +
                    str(date.today()) + '\n# Reason for changing values: ' +
                    "TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                    "'b'" + ": mpf('1.0')" + "}\n\n#####"
                ]
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.1')}
            trusted_dict = {'a': mpf('0.1'), 'b': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.1' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.1' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['a', 'b']" + ' in module TestModule failed. Please check values.\n\n' +
                    'If you are confident that the newly calculated values are correct, comment out the old trusted ' +
                    'values for ' + "'TestModuleGlobals' in trusted_values_dict and copy the following code between" +
                    ' the ##### into trusted_values_dict. Make sure to fill out the TODO comment describing why the' +
                    ' values had to be changed. Then re-run test script.\n#####\n\n# Generated on: ' +
                    str(date.today()) + '\n# Reason for changing values: ' +
                    "TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                    "'b'" + ": mpf('1.1')" + "}\n\n#####"
                ]
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.1')}
            trusted_dict = {'a': mpf('0.0'), 'b': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.0' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.1' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['b']" + ' in module TestModule failed. Please check values.\n\n' +
                    'If you are confident that the newly calculated values are correct, comment out the old trusted ' +
                    'values for ' + "'TestModuleGlobals' in trusted_values_dict and copy the following code between" +
                    ' the ##### into trusted_values_dict. Make sure to fill out the TODO comment describing why the' +
                    ' values had to be changed. Then re-run test script.\n#####\n\n# Generated on: ' +
                    str(date.today()) + '\n# Reason for changing values: ' +
                    "TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                    "'b'" + ": mpf('1.1')" + "}\n\n#####"
                ]
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0'), 'c': mpf('2.0')}
            trusted_dict = {'a': mpf('0.2'), 'b': mpf('1.2'), 'c': mpf('2.2')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.2' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.2' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'c' + ': Calculated: ' + '2.0' +
                    '\nTestModule: ' + 'c' + ': Trusted:    ' + '2.2' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['a', 'b', 'c']" + ' in module TestModule failed. Please check values.\n\nIf you '
                    + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                    "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                    'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                    + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                    " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                    "'b'" + ": mpf('1.0')" + ", " + "'c'" + ": mpf('" + '2.0' + "')" "}\n\n#####"
                ]
            )

            calculated_dict = {'a': mpf('0.0'), 'b': mpf('1.0'), 'c': mpf('2.0')}
            trusted_dict = {'a': mpf('0.2'), 'b': mpf('1.0'), 'c': mpf('2.2')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.2' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'c' + ': Calculated: ' + '2.0' +
                    '\nTestModule: ' + 'c' + ': Trusted:    ' + '2.2' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['a', 'c']" + ' in module TestModule failed. Please check values.\n\nIf you '
                    + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                    "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                    'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                    + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                    " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                    "'b'" + ": mpf('1.0')" + ", " + "'c'" + ": mpf('" + '2.0' + "')" "}\n\n#####"
                ]
            )

            calculated_dict = {'c': mpf('2.0'), 'a': mpf('0.0'), 'b': mpf('1.0')}
            trusted_dict = {'c': mpf('2.2'), 'a': mpf('0.2'), 'b': mpf('1.0')}

            with self.assertLogs(level='DEBUG') as logger:
                self.assertFalse(calc_error(mod, calculated_dict, trusted_dict))
            self.assertEqual(logger.output,
                [
                    'DEBUG:root:' + '\nTestModule: ' + 'a' + ': Calculated: ' + '0.0' +
                    '\nTestModule: ' + 'a' + ': Trusted:    ' + '0.2' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'b' + ': Calculated: ' + '1.0' +
                    '\nTestModule: ' + 'b' + ': Trusted:    ' + '1.0' + '\n',
                    'DEBUG:root:' + '\nTestModule: ' + 'c' + ': Calculated: ' + '2.0' +
                    '\nTestModule: ' + 'c' + ': Trusted:    ' + '2.2' + '\n',
                    'ERROR:root:' + '\n\nVariable(s) ' + "['a', 'c']" + ' in module TestModule failed. Please check values.\n\nIf you '
                    + 'are confident that the newly calculated values are correct, comment out the old trusted values for ' +
                    "'TestModuleGlobals' in trusted_values_dict and copy the following code between the ##### into " +
                    'trusted_values_dict. Make sure to fill out the TODO comment describing why the values had to be changed.'
                    + ' Then re-run test script.\n#####\n\n# Generated on: ' + str(date.today()) + '\n# Reason for changing' +
                    " values: TODO\ntrusted_values_dict['TestModuleGlobals'] = {" + "'a'" + ": mpf('" + '0.0' + "')" + ', ' +
                    "'b'" + ": mpf('1.0')" + ", " + "'c'" + ": mpf('" + '2.0' + "')" "}\n\n#####"
                ]
            )

            logging.info('\nAll calc_error tests passed.\n')

    def test_create_dict_string(self):
        from UnitTesting.create_dict_string import create_dict_string
        from mpmath import mpf, mpc

        calculated_dict = {}
        self.assertEqual("{}", create_dict_string(calculated_dict))

        calculated_dict = {'a': 0}
        self.assertEqual("{'a': 0}", create_dict_string(calculated_dict))

        calculated_dict = {'b': mpf('1.0')}
        self.assertEqual("{'b': mpf('1.0')}", create_dict_string(calculated_dict))

        calculated_dict = {'c': mpc(real='1.0', imag='2.0')}
        self.assertEqual("{'c': mpc(real='1.0', imag='2.0')}", create_dict_string(calculated_dict))

        calculated_dict = {'alpha': 4, 'beta': mpf('0.2'), 'gamma': mpc(real='3.14', imag='6.28')}
        self.assertEqual("{'alpha': 4, 'beta': mpf('0.2'), 'gamma': mpc(real='3.14', imag='6.28')}",
                         create_dict_string(calculated_dict))

        calculated_dict = {'beta': mpf('0.2'), 'gamma': mpc(real='3.14', imag='6.28'), 'alpha': 4}
        self.assertEqual("{'alpha': 4, 'beta': mpf('0.2'), 'gamma': mpc(real='3.14', imag='6.28')}",
                         create_dict_string(calculated_dict))

        calculated_dict = {'AZ': mpf('2.4287654'), 'ab': mpc(real='0.0', imag='123.1234123412341234')}
        self.assertEqual("{'ab': mpc(real='0.0', imag='123.1234123412341234'), 'AZ': mpf('2.4287654')}",
                         create_dict_string(calculated_dict))

        logging.info('\nAll create_dict_string tests passed.\n')

    def test_create_trusted_globals_dict(self):
        from UnitTesting.create_trusted_globals_dict import create_trusted_globals_dict
        from mpmath import mpf

        mod_dict = {}
        trusted_values_dict = {}
        first_times = {}
        self.assertEqual({}, create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        mod_dict = {'mod': []}
        trusted_values_dict = {}
        first_times = {'mod': True}
        self.assertEqual({'mod': {}}, create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        mod_dict = {'mod': ['hello', 'world']}
        trusted_values_dict = {}
        first_times = {'mod': True}
        self.assertEqual({'mod': {}}, create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        with self.assertRaises(KeyError):
            mod_dict = {'mod': ['hello', 'world']}
            trusted_values_dict = {}
            first_times = {'mod': False}
            create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times)

        with self.assertRaises(AssertionError):
            mod_dict = {'mod': []}
            trusted_values_dict = {}
            first_times = {'mod': True, 'random': False}
            create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times)

        with self.assertRaises(AssertionError):
            mod_dict = {'mod1': 'hello', 'mod2': 'world'}
            trusted_values_dict = {}
            first_times = {'mod1': True}
            create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times)

        with self.assertRaises(AssertionError):
            mod_dict = {'a': 1, 'b': 2, 'c': 3}
            trusted_values_dict = {}
            first_times = {'d': 4, 'e': 5, 'f': 6}
            create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times)

        with self.assertRaises(AssertionError):
            mod_dict = {'a': 1, 'b': 2, 'c': 3}
            trusted_values_dict = {}
            first_times = {'d': 4, 'e': 5, 'f': 6}
            create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times)

        from BSSN.tests.trusted_values_dict import trusted_values_dict

        mod_dict = {'BrillLindquist': ['foo', 'bar']}
        first_times = {'BrillLindquist': True}
        self.assertEqual({'BrillLindquist': dict()}, create_trusted_globals_dict(mod_dict, trusted_values_dict,
                                                                                 first_times))

        from UnitTesting.calc_error import calc_error

        mod_dict = {'BrillLindquist': ['foo', 'bar']}
        first_times = {'BrillLindquist': False}
        self.assertTrue(calc_error('BrillLindquist', trusted_values_dict['BrillLindquistGlobals']
                        , create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times)['BrillLindquist']))

        mod_dict = {'BrillLindquist': ['foo', 'bar']}
        first_times = {'BrillLindquist': False}
        self.assertEqual({'BrillLindquist': trusted_values_dict['BrillLindquistGlobals']}
                         , create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        mod_dict = {'BrillLindquist': ['foo', 'bar'], 'mod': ['hello world']}
        first_times = {'BrillLindquist': False, 'mod': True}
        self.assertEqual({'BrillLindquist': trusted_values_dict['BrillLindquistGlobals'], 'mod': dict()},
                         create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        mod_dict = {'BrillLindquist': 1, 'ShiftedKerrSchild': 2}
        first_times = {'BrillLindquist': False, 'ShiftedKerrSchild': False}
        self.assertEqual({'BrillLindquist': trusted_values_dict['BrillLindquistGlobals']
                         , 'ShiftedKerrSchild': trusted_values_dict['ShiftedKerrSchildGlobals']}
                         , create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        mod_dict = {'mod1': 1, 'mod2': 2, 'mod3': 3}
        first_times = {'mod1': True, 'mod2': True, 'mod3': True}
        self.assertEqual({'mod1': dict(), 'mod2': dict(), 'mod3': dict()},
                         create_trusted_globals_dict(mod_dict, trusted_values_dict, first_times))

        logging.info('\nAll create_trusted_globals_dict tests passed.\n')

    def test_evaluate_globals(self):
        from UnitTesting.evaluate_globals import evaluate_globals
        from UnitTesting.functions_and_globals import functions_and_globals
        import NRPy_param_funcs as par
        from sympy import sqrt, symbols, sin
        import indexedexp as ixp
        import BSSN.BrillLindquist as BrillLindquist
        import BSSN.StaticTrumpet as StaticTrumpet

        self.assertEqual(dict(), evaluate_globals(dict(), dict()))

        mod_dict = {'BrillLindquist': functions_and_globals(['BrillLindquist(ComputeADMGlobalsOnly = True)'], ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD'])}

        locs = dict(locals())

        thismodule = "Brill-Lindquist"
        BH1_posn_x, BH1_posn_y, BH1_posn_z = par.Cparameters("REAL", thismodule,
                                                             ["BH1_posn_x", "BH1_posn_y", "BH1_posn_z"])
        BH1_mass = par.Cparameters("REAL", thismodule, ["BH1_mass"])
        BH2_posn_x, BH2_posn_y, BH2_posn_z = par.Cparameters("REAL", thismodule,
                                                             ["BH2_posn_x", "BH2_posn_y", "BH2_posn_z"])
        BH2_mass = par.Cparameters("REAL", thismodule, ["BH2_mass"])
        Cartxyz = ixp.declarerank1("Cartxyz")
        Cartxyz0, Cartxyz1, Cartxyz2 = Cartxyz

        result_dict = {'BrillLindquist': {'alphaCart': (BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**(-2), 'betaCartU': [0, 0, 0], 'BCartU': [0, 0, 0], 'gammaCartDD': [[(BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**4, 0, 0], [0, (BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**4, 0], [0, 0, (BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**4]], 'KCartDD': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}}

        self.assertEqual(result_dict, evaluate_globals(mod_dict, locs))

        mod_dict = {'BrillLindquist': functions_and_globals(['BrillLindquist(ComputeADMGlobalsOnly = True)'], ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']),
                    'StaticTrumpet': functions_and_globals(['StaticTrumpet(ComputeADMGlobalsOnly = True)'], ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD'])}

        locs = locals()

        r, th, ph = symbols('r th ph', real=True)
        M = par.Cparameters("REAL", thismodule, ["M"])

        result_dict = {'BrillLindquist': {'alphaCart': (BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**(-2), 'betaCartU': [0, 0, 0], 'BCartU': [0, 0, 0], 'gammaCartDD': [[(BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**4, 0, 0], [0, (BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**4, 0], [0, 0, (BH1_mass/(2*sqrt((-BH1_posn_x + Cartxyz0)**2 + (-BH1_posn_y + Cartxyz1)**2 + (-BH1_posn_z + Cartxyz2)**2)) + BH2_mass/(2*sqrt((-BH2_posn_x + Cartxyz0)**2 + (-BH2_posn_y + Cartxyz1)**2 + (-BH2_posn_z + Cartxyz2)**2)) + 1)**4]], 'KCartDD': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]},
                       'StaticTrumpet': {'alphaSph': r/(M + r), 'betaSphU': [M*r/(M + r)**2, 0, 0], 'BSphU': [0, 0, 0], 'gammaSphDD': [[(M/r + 1)**2, 0, 0], [0, r**2*(M/r + 1)**2, 0], [0, 0, r**2*(M/r + 1)**2*sin(th)**2]], 'KSphDD': [[-M/r**2, 0, 0], [0, M, 0], [0, 0, M*sin(th)**2]]}}

        self.assertEqual(result_dict, evaluate_globals(mod_dict, locs))

        logging.info('\nAll evaluate_globals tests passed.\n')

    def test_expand_variable_dict(self):
        from UnitTesting.expand_variable_dict import expand_variable_dict

        variable_dict = dict()
        result_dict = dict()
        self.assertEqual(result_dict, expand_variable_dict(variable_dict))

        variable_dict = {'alpha': 1}
        result_tuple = {'alpha': 1}
        self.assertEqual(result_tuple, expand_variable_dict(variable_dict))

        variable_dict = {'alphaD': [1, 2]}
        result_tuple = {'alphaD[0]': 1, 'alphaD[1]': 2}
        self.assertEqual(result_tuple, expand_variable_dict(variable_dict))

        variable_dict = {'alphaDD': [[1, 2], [4, 3]]}
        result_tuple = {'alphaDD[0][0]': 1, 'alphaDD[0][1]': 2, 'alphaDD[1][0]':4 , 'alphaDD[1][1]':3}
        self.assertEqual(result_tuple, expand_variable_dict(variable_dict))

        variable_dict = {'aDD': [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 8, 9, 7, 6], [0, 0, 0, 0, 0], [3, 1, 4, 1, 5]]}
        result_tuple = {'aDD[0][0]': 1, 'aDD[0][1]': 2, 'aDD[0][2]': 3, 'aDD[0][3]': 4, 'aDD[0][4]': 5,
                        'aDD[1][0]': 2, 'aDD[1][1]': 3, 'aDD[1][2]': 4, 'aDD[1][3]': 5, 'aDD[1][4]': 6,
                        'aDD[2][0]': 2, 'aDD[2][1]': 8, 'aDD[2][2]': 9, 'aDD[2][3]': 7, 'aDD[2][4]': 6,
                        'aDD[3][0]': 0, 'aDD[3][1]': 0, 'aDD[3][2]': 0, 'aDD[3][3]': 0, 'aDD[3][4]': 0,
                        'aDD[4][0]': 3, 'aDD[4][1]': 1, 'aDD[4][2]': 4, 'aDD[4][3]': 1, 'aDD[4][4]': 5}
        self.assertEqual(result_tuple, expand_variable_dict(variable_dict))

        variable_dict = {'alpha': 4, 'beta': 5}
        result_tuple = {'alpha': 4, 'beta': 5}
        self.assertEqual(result_tuple, expand_variable_dict(variable_dict))

        variable_dict = {'alphaD': [1, 2], 'beta': 3}
        result_tuple = {'alphaD[0]': 1, 'alphaD[1]': 2, 'beta': 3}
        self.assertEqual(result_tuple, expand_variable_dict(variable_dict))

        logging.info('\nAll expand_variable_dict tests passed.\n')

    def test_first_time_print(self):
        from UnitTesting.first_time_print import first_time_print
        from datetime import date
        from UnitTesting.standard_constants import precision
        import os
        import sys
        from mpmath import mpf, mp

        mp.dps = precision

        path = os.path.abspath(__file__)

        mod = 'TestModule'
        value_dict = {}

        captured_output = create_StringIO()
        first_time_print(mod, value_dict, path, False)
        self.assertEqual('\nModule: TestModule\nPlease copy the following code between the ##### and paste it into' +
                         ' your trusted_values_dict.py file:\n#####\n\n# Generated on: ' + str(date.today()) +
                         "\ntrusted_values_dict['TestModuleGlobals'] = {}\n\n#####\n", captured_output.getvalue())

        mod = 'TestModule2'
        value_dict = {'alpha': 0, 'beta': 1, 'gamma': 3}

        captured_output = create_StringIO()
        first_time_print(mod, value_dict, path, False)
        self.assertEqual('\nModule: TestModule2\nPlease copy the following code between the ##### and paste it into' +
                         ' your trusted_values_dict.py file:\n#####\n\n# Generated on: ' + str(date.today()) +
                         "\ntrusted_values_dict['TestModule2Globals'] = {'alpha': 0, 'beta': 1, 'gamma': 3}\n\n#####\n",
                         captured_output.getvalue())

        mod = 'TestModule3'
        value_dict = {'beta': 0, 'gamma': 1, 'alpha': 3}

        captured_output = create_StringIO()
        first_time_print(mod, value_dict, path, False)
        self.assertEqual('\nModule: TestModule3\nPlease copy the following code between the ##### and paste it into' +
                         ' your trusted_values_dict.py file:\n#####\n\n# Generated on: ' + str(date.today()) +
                         "\ntrusted_values_dict['TestModule3Globals'] = {'alpha': 3, 'beta': 0, 'gamma': 1}\n\n#####\n",
                         captured_output.getvalue())

        mod = 'TestModule4'
        value_dict = {'x': mpf('0.0'), 'y': mpf('1.23456789012345678912345')}

        captured_output = create_StringIO()
        first_time_print(mod, value_dict, path, False)
        self.assertEqual('\nModule: TestModule4\nPlease copy the following code between the ##### and paste it into' +
                         ' your trusted_values_dict.py file:\n#####\n\n# Generated on: ' + str(date.today()) +
                         "\ntrusted_values_dict['TestModule4Globals'] = {'x': mpf('0.0'), "
                         "'y': mpf('1.23456789012345678912345')}\n\n#####\n", captured_output.getvalue())

        mod = 'TestModule5'
        value_dict = {'AZ': mpf('0.0'), 'ab': mpf('1.0')}

        captured_output = create_StringIO()
        first_time_print(mod, value_dict, path, False)
        self.assertEqual('\nModule: TestModule5\nPlease copy the following code between the ##### and paste it into' +
                         ' your trusted_values_dict.py file:\n#####\n\n# Generated on: ' + str(date.today()) +
                         "\ntrusted_values_dict['TestModule5Globals'] = {'ab': mpf('1.0'), "
                         "'AZ': mpf('0.0')}\n\n#####\n", captured_output.getvalue())

        sys.stdout = sys.__stdout__


        logging.info('\nAll first_time_print tests passed.\n')

    def test_functions_and_globals(self):
        from UnitTesting.functions_and_globals import functions_and_globals

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
        from UnitTesting.get_variable_dimension import get_variable_dimension

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
        from UnitTesting.is_first_time import is_first_time
        from BSSN.tests.trusted_values_dict import trusted_values_dict

        mod_dict = {'BrillLindquist': 'Hello World'}
        fake_mod_dict = {'fake_module': 'Goodbye World'}

        self.assertEqual(is_first_time(dict(), dict()), dict())

        self.assertEqual(is_first_time(mod_dict, trusted_values_dict), {'BrillLindquist': False})
        self.assertEqual(is_first_time(fake_mod_dict, trusted_values_dict), {'fake_module': True})

        large_mod_dict = {'BrillLindquist': 'Hello World', 'fake_module': 'Goodbye World'}

        self.assertEqual(is_first_time(large_mod_dict, trusted_values_dict),
                         {'BrillLindquist': False, 'fake_module': True})

        mod_dict_wrong_capitalization = {'brillLindquist': 2}

        self.assertEqual(is_first_time(mod_dict_wrong_capitalization, trusted_values_dict), {'brillLindquist': True})

        logging.info('\nAll is_first_time tests passed.\n')

    def test_run_test(self):
        from UnitTesting.run_test import run_test

        mod_dict = {}
        trusted_values_dict = {}
        with self.assertRaises(AssertionError):
            run_test(self, mod_dict, trusted_values_dict, '', locals())

        logging.info('\nAll run_test tests passed.\n')

    def test_trusted_values_dict_creation(self):

        # Tests the setup_trusted_values_dict and the file-writing portion of first_time_print
        from UnitTesting.setup_trusted_values_dict import setup_trusted_values_dict
        import sys
        import os

        path = sys.path[0]

        self.assertFalse(os.path.exists(path + '/trusted_values_dict.py'))

        setup_trusted_values_dict(path)

        try:
            fr = open(path + '/trusted_values_dict.py', 'r')
            self.assertEqual(fr.read(), 'from mpmath import mpf, mp, mpc\nfrom UnitTesting.standard_constants import '
                                        'precision\n\nmp.dps = precision\ntrusted_values_dict = {}\n')
            fr.close()
            os.remove(path + '/trusted_values_dict.py')
        except IOError:
            self.assertFalse(True, msg='trusted_values_dict.py not created in correct location.')




        logging.info('\nAll setup_trusted_values_dict tests passed.\n')

        logging.info('\nAll file-writing first_time_print tests passed.\n')

    def test_simplify_and_evaluate_sympy_expressions(self):
        from UnitTesting.simplify_and_evaluate_sympy_expressions import simplify_and_evaluate_sympy_expressions
        from mpmath import mpf, mp, pi, sqrt
        import random
        import UnitTesting.standard_constants as sc
        from sympy import symbols
        import hashlib
        from UnitTesting.calc_error import calc_error

        mp.dps = sc.precision

        var_dict = {}
        self.assertEqual({}, simplify_and_evaluate_sympy_expressions(var_dict))
        self.assertEqual({}, simplify_and_evaluate_sympy_expressions(var_dict, True))

        M_PI, M_SQRT1_2 = symbols('M_PI M_SQRT1_2')

        var_dict = {'a': M_PI}
        trusted_dict = {'a': mpf(pi)}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        var_dict = {'b': M_SQRT1_2}
        trusted_dict = {'b': mpf(1/sqrt(2))}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        var_dict = {'alpha': M_PI+M_SQRT1_2}
        trusted_dict = {'alpha': mpf(pi)+mpf(1/sqrt(2))}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        x, y, z = symbols('x y z')

        symbs = {x: 0, y: 0, z: 0}

        for symb in symbs:
            random.seed(int(hashlib.md5(str(symb).encode()).hexdigest(), 16))
            symbs[symb] = mpf(random.random())

        var_dict = {'a': x}
        trusted_dict = {'a': symbs[x]}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        var_dict = {'b': x+y}
        trusted_dict = {'b': symbs[x] + symbs[y]}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        var_dict = {'a': x, 'b': y, 'c': z}
        trusted_dict = {'a': symbs[x], 'b': symbs[y], 'c': symbs[z]}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        var_dict = {'a': x**2, 'b': (x+y)/z}
        trusted_dict = {'a': symbs[x]**2, 'b': (symbs[x]+symbs[y])/symbs[z]}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        var_dict = {'a': x**2 + 1, 'b': (x**2)**2, 'c': x**2 + y**2, 'd': 1-x**2, 'e': x**2*z}
        trusted_dict = {'a': symbs[x]**2 + 1, 'b': symbs[x]**4, 'c': symbs[x]**2 + symbs[y]**2,
                        'd': 1-symbs[x]**2, 'e': symbs[x]**2*symbs[z]}
        self.assertTrue(calc_error('mod', simplify_and_evaluate_sympy_expressions(var_dict), trusted_dict, False))

        logging.info('\nAll simplify_and_evaluate_sympy_expressions tests passed\n')


# Sub-function for test_first_time_print
def create_StringIO():
    import sys

    if version_info[0] == 2:
        import StringIO
        captured_output = StringIO.StringIO()
    else:
        import io
        captured_output = io.StringIO()

    sys.stdout = captured_output
    return captured_output


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()
