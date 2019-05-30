import logging

from calcError import calcError
from firstTimePrint import firstTimePrint
from evaluateGlobals import evaluateGlobals
from moduleDictToList import moduleDictToList
from listToValueList import listToValueList
from isFirstTime import isFirstTime
from createTrustedGlobalsDict import createTrustedGlobalsDict


# runTest takes in :
# [self]- The unittest self object,
# [ModDict]- The user-supplied dictionary of Modules
# [TrustedDict]- The dictionary of trusted values based on ModDict
# [first_time]- A boolean describing if this is the first time the code is being run
# [globs]- The current globals in the workspace. Should ALWAYS be globals()
# It then runs a unittest, comparing calculated values with trusted values.
def runTest(self, ModDict, globs):

    # Determining if this is the first time the code is run based of the existence of trusted values
    first_time = isFirstTime(ModDict)

    # Creating trusted dictionary based off names of modules in ModDict
    TrustedDict = createTrustedGlobalsDict(ModDict, first_time)

    # Creating dictionary of expressions for all modules in ModDict
    resultDict = evaluateGlobals(ModDict, globs)

    # Looping through each module in resultDict
    for mod in resultDict:

        if not first_time:
            logging.info('Currently working on module ' + mod + '...')

        # Generating variable list and name list for module
        (varList, nameList) = moduleDictToList(resultDict[mod])

        # Calculating numerical list for module
        numList = listToValueList(mod, varList, first_time)

        # Initalizing dictionary for the current module
        modDict = dict()

        # Assigning each numerical value to a name in the module's dictionary
        for num, name in zip(numList, nameList):
            modDict[name] = num

        # If being run for the first time, print the code that must be copied into trustedValuesDict
        if first_time:
            firstTimePrint(mod, modDict)
        # Otherwise, compare calculated values to trusted values
        else:

            symbolicDict = dict()

            # Store symbolic expressions in dictionary
            for var, name in zip(varList, nameList):
                symbolicDict[name] = var

            # Calculates the error between modDict and TrustedDict[mod] for the current module
            valuesIdentical = calcError(mod, modDict, TrustedDict[mod], symbolicDict)

            # If at least one value differs, print exit message and fail the unittest
            if not valuesIdentical:
                self.assertTrue(valuesIdentical,
                                'Variable above has different calculated and trusted values. Follow '
                                'above instructions.')

            # If every value is the same, completed module.
            else:
                logging.info('Completed module ' + mod + ' with no errors.\n')
            self.assertTrue(valuesIdentical)
    if first_time:
        self.assertTrue(False, 'Automatically fails after running for the first time. Follow above instructions'
                               ' and run again')
