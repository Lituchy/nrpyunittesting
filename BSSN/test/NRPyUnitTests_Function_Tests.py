
import unittest
import logging

# TODO: Change level based on desired amount of output.
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.INFO)


class TestFunctions(unittest.TestCase):

    def ftestCalcError(self):
        self.assertTrue(False)

    def ftestCreateTrustedGlobalsDict(self):
        self.assertTrue(False)

    def ftestEfficientListToValueList(self):
        self.assertTrue(False)

    def ftestEvaluateGlobals(self):
        self.assertTrue(False)

    def testFunctionsAndGlobals(self):
        from functionsAndGlobals import functionsAndGlobals

        basicFunctionList = ['func1(), func2()']
        basicGlobalList = ['x', 'y', 'z']

        self.assertEqual(functionsAndGlobals([], []), {'functionList': [], 'globalList': []})

        self.assertEqual(functionsAndGlobals([], basicGlobalList),
                         {'functionList': [], 'globalList': basicGlobalList})
        self.assertEqual(functionsAndGlobals(basicFunctionList, []),
                         {'functionList': basicFunctionList, 'globalList': []})
        self.assertEqual(functionsAndGlobals(basicFunctionList, basicGlobalList),
                         {'functionList': basicFunctionList, 'globalList': basicGlobalList})

        with self.assertRaises(AssertionError):
            functionsAndGlobals([1,'hello','world'], [])

        with self.assertRaises(AssertionError):
            functionsAndGlobals(['hello','world'], [2])

        with self.assertRaises(AssertionError):
            functionsAndGlobals(['hello', 'world', 42], basicGlobalList)

        with self.assertRaises(AssertionError):
            functionsAndGlobals('function()', [])

        with self.assertRaises(AssertionError):
            functionsAndGlobals([], 'glob')

        logging.info('\nAll functionsAndGlobals tests passed.\n')

    def testGetVariableDimension(self):
        from getVariableDimension import getVariableDimension

        rank0 = 4
        rank1 = [rank0, rank0+1, rank0]
        rank2 = [rank1, rank1]
        rank3 = [rank2]
        self.assertEqual(getVariableDimension(rank0), 0)
        self.assertEqual(getVariableDimension(rank1), 1)
        self.assertEqual(getVariableDimension(rank2), 2)
        self.assertEqual(getVariableDimension(rank3), 3)

        self.assertEqual(getVariableDimension(rank3[0]), 2)
        self.assertEqual(getVariableDimension(rank2[0]), 1)
        self.assertEqual(getVariableDimension(rank2[1]), 1)
        self.assertEqual(getVariableDimension([rank2, rank2]), 3)
        self.assertEqual(getVariableDimension([[[[[rank0]]]]]), 5)

        with self.assertRaises(IndexError):
            getVariableDimension([])

        logging.info('\nAll getVariableDimension tests passed.\n')

    def testIsFirstTime(self):
        from isFirstTime import isFirstTime

        ModDict = {'BrillLindquist': 'Hello World'}
        FakeModDict = {'FakeModule': 'Goodbye World'}

        self.assertEqual(isFirstTime({}), [])

        self.assertEqual(isFirstTime(ModDict), [False])
        self.assertEqual(isFirstTime(FakeModDict), [True])

        ModDict.update(FakeModDict)

        self.assertEqual(isFirstTime(ModDict), [False, True])

        ModDictWrongCapitalization = {'brillLindquist': 2}

        self.assertEqual(isFirstTime(ModDictWrongCapitalization), [True])

        logging.info('\nAll isFirstTime tests passed.\n')

    def ftestListToValueList(self):
        self.assertTrue(False)

    def ftestModuleDictToList(self):
        self.assertTrue(False)

    def ftestRunTest(self):
        self.assertTrue(False)


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()