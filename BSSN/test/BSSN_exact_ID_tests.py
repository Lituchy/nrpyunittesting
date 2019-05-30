import unittest
import logging

from trustedValuesDict import trustedValuesDict
from calcError import calcError
from firstTimePrint import firstTimePrint

from makeFunctionAndGlobalDict import makeFunctionAndGlobalDict
from evaluateGlobals import evaluateGlobals
from moduleDictToList import moduleDictToList
from listToValueList import listToValueList
from createTrustedGlobalsDict import createTrustedGlobalsDict

import BSSN.BrillLindquist as BrillLindquist
import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
import BSSN.StaticTrumpet as StaticTrumpet
import BSSN.UIUCBlackHole as UIUCBlackHole


# Set following line to True if you need to generate the trusted values for your modules.
# Set following line to False if the trusted values for your modules are correctly pasted into trustedValuesDict
first_time = False

# Change level based on desired amount of output. 
# ERROR -> Ouputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG
logging.basicConfig(level=logging.DEBUG)

# Globals we want to calculate
CartGlobalList = ['alphaCart','betaCartU','BCartU', 'gammaCartDD','KCartDD']
SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU','gammaSphDD', 'KSphDD']

# Change to BSSN.BrillLindquist soon
# Creating our module dictionary
ModDict = {
    'BrillLindquist': makeFunctionAndGlobalDict( ['BrillLindquist(ComputeADMGlobalsOnly = True)'] , CartGlobalList ),
    
    'ShiftedKerrSchild': makeFunctionAndGlobalDict( ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'] ,SphGlobalList),
    
    'StaticTrumpet': makeFunctionAndGlobalDict( ['StaticTrumpet(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'UIUCBlackHole': makeFunctionAndGlobalDict( ['UIUCBlackHole(ComputeADMGlobalsOnly = True)'] , SphGlobalList )
}


# Creating trusted dictionary based off names of modules in ModDict
TrustedDict = createTrustedGlobalsDict(ModDict,first_time)

    
# Python unittest class
class TestBSSNExact(unittest.TestCase):
        
    # Testing globals for BSSN exact modules
    def testExactGlobals(self):
        
        # Creating dictionary of expressions for all modules in ModDict
        resultDict = evaluateGlobals(ModDict,globals())            
        
        # Looping through each module in resultDict
        for mod in resultDict:
            
            logging.info('Currently working on module ' + mod + '...')
            
            # Generating variable list and name list for module
            (varList,nameList) = moduleDictToList(resultDict[mod])
            
            # Calculating numerical list for module
            numList = listToValueList(mod,varList,first_time)
            
            # Initalizing dictionary for the current module
            modDict = dict()
            
            # Assigning each numerical value to a name in the module's dictionary
            for num, name in zip(numList,nameList):
                modDict[name] = num
            
            # If being run for the first time, print the code that must be copied into trustedValuesDict
            if first_time:
                firstTimePrint(mod,modDict)
            # Otherwise, compare calculated values to trusted values
            else:
            
                # If in NOTSET mode, print symbolic dictionary
                if logging.getLogger().getEffectiveLevel() == 0:

                    # Create temporary dictionary
                    tempDict = dict()

                    # Store symbolic expressions in dictionary
                    for var, name in zip(varList,nameList):
                        tempDict[name] = var

                    logging.debug('Symbolic expression: \n' + str(tempDict) + '\n')

                    del tempDict
                
                # TODO: Update this. Should be calling calcError
                valuesIdentical = calcError(mod,modDict,TrustedDict[mod])

                # If at least one value differs, print exit message and fail the unittest
                if not valuesIdentical:
                    logging.debug('Now exiting. Please check trusted values and result values and update if necessary.')
                    self.assertTrue(valuesIdentical)
                
                # If every value is the same, completed module.
                else:
                    logging.info('Completed module ' + mod + ' with no errors.\n')
                self.assertTrue(valuesIdentical)
                
        if first_time:
            print("\n### WARNING: ###\nDon't forget to change first_time to False")


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()

