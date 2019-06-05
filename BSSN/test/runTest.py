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
# [locs]- The current local variables in the workspace. Should ALWAYS be locals()
# It then runs a unittest, comparing calculated values with trusted values.
def runTest(self, ModDict, locs):

    # Determining if this is the first time the code is run based of the existence of trusted values
    first_times = isFirstTime(ModDict)

    # Creating trusted dictionary based off names of modules in ModDict
    TrustedDict = createTrustedGlobalsDict(ModDict, first_times)

    # Creating dictionary of expressions for all modules in ModDict
    resultDict = evaluateGlobals(ModDict, locs)

    del ModDict

    # If it is the first time for at least one module, sort the module dictionary based on first_times.
    # This makes it so the new modules are done last. This makes it easy to copy the necessary modules' code.
    if True in first_times:
        # https://stackoverflow.com/questions/13668393/python-sorting-two-lists
        first_times, resultMods = (list(x) for x in zip(*sorted(zip(first_times, resultDict))))

        tempDict = dict()

        # Creates dictionary based on order of first_times
        for mod in resultMods:
            tempDict[mod] = resultDict[mod]


        # Updates resultDict to be in this new order
        resultDict = tempDict
        del tempDict, resultMods

    # Looping through each module in resultDict
    for (mod, res), first_time in zip(resultDict.items(), first_times):

        if not first_time:
            logging.info('Currently working on module ' + mod + '...')

        # Generating variable list and name list for module
        (varList, nameList) = moduleDictToList(res)


        # Calculating numerical list for module
        numList = listToValueList(varList, first_time)

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

            del symbolicDict

            # If at least one value differs, print exit message and fail the unittest
            if not valuesIdentical:
                self.assertTrue(valuesIdentical,
                                'Variable above has different calculated and trusted values. Follow '
                                'above instructions.')

            # If every value is the same, completed module.
            else:
                logging.info('Completed module ' + mod + ' with no errors.\n')
            self.assertTrue(valuesIdentical)

    if first_times[-1]:
        self.assertTrue(False, 'Automatically failing due to first time for at least one module. Please see above'
                               'for the code to copy into your trustedValuesDict.')
