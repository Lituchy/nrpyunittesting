import unittest
# First we import needed core NRPy+ modules
import NRPy_param_funcs as par
import reference_metric as rfm
import grid as gri
from sympy import Integer,Symbol,symbols,simplify,Rational,Function,srepr,sin,cos,exp,log,Abs,Add,Mul,Pow,preorder_traversal,N,Float,S,var,sympify
from mpmath import *
import random
from trustedValuesDict import tvDict
import calcError as calcErr
import firstTimePrint as ftp

import makeFunctionAndGlobalDict as makeFuncGlobDict
import evaluateGlobals as evalGlobs
import getVariableDimension as getVarDim
import moduleDictToList as modDictToLst
import listToValueList as lstToValLst

import BSSN.BrillLindquist as BrillLindquist
import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
import BSSN.StaticTrumpet as StaticTrumpet
import BSSN.UIUCBlackHole as UIUCBlackHole
import BSSN.ADM_Exact_Spherical_or_Cartesian_to_BSSNCurvilinear as AtoB

import sys
import logging

# Set following line to True if need to calculate trustedValue for the first time
first_time = False

# Setting mp precision
mp.dps = tvDict["precision"]

# Globals we want to calculate
CartGlobalList = ['alphaCart','betaCartU','BCartU', 'gammaCartDD','KCartDD']
SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU','gammaSphDD', 'KSphDD']

# Creating our module dictionary
ModDict = {
    'BrillLindquist': makeFuncGlobDict.makeFunctionAndGlobalDict( ['BrillLindquist(ComputeADMGlobalsOnly = True)'] , CartGlobalList ),
    
    'ShiftedKerrSchild': makeFuncGlobDict.makeFunctionAndGlobalDict( ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'StaticTrumpet': makeFuncGlobDict.makeFunctionAndGlobalDict( ['StaticTrumpet(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'UIUCBlackHole': makeFuncGlobDict.makeFunctionAndGlobalDict( ['UIUCBlackHole(ComputeADMGlobalsOnly = True)'] , SphGlobalList )
}

# Pulling trusted values from trustedValuesDict and storing them in a dictionary
TrustedDict = {
    'BrillLindquist': tvDict['BSSNExactBrillLindquist'],
    'ShiftedKerrSchild': tvDict['BSSNExactShiftedKerrSchild'],
    'StaticTrumpet': tvDict['BSSNExactStaticTrumpet'],
    'UIUCBlackHole': tvDict['BSSNExactUIUCBlackHole']
}

# Change level based on desired amount of output. 
# ERROR -> Ouputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
logging.basicConfig(level=logging.INFO)
    
# Python unittest class
class TestBSSNExact(unittest.TestCase):
    
    # Function calls that need to be done before testing
    def setUp(self):
        
        # Assert that the module dictionary and trusted values dictionary have the same keys
        self.assertEqual(set(ModDict),set(TrustedDict))
        
        # Set spatial dimension (must be 3 for BSSN)
        DIM = 3
        par.set_parval_from_str("grid::DIM",DIM)

        # Then we set the coordinate system for the numerical grid
        par.set_parval_from_str("reference_metric::CoordSystem","Spherical")
        rfm.reference_metric() # Create ReU, ReDD needed for rescaling B-L initial data, generating BSSN RHSs, etc.
    
    
    # Testing globals for BSSN exact modules
    def testExactGlobals(self):
        
        # Creating dictionary of expressions for all modules in ModDict
        resultDict = evalGlobs.evaluateGlobals(ModDict,globals())
        
        # Looping through each module in resultDict
        for mod in resultDict:
            
            logging.info('Currently working on module ' + mod + '...\n')
            
            # Generating variable list and name list for module
            (varList,nameList) = modDictToLst.moduleDictToList(resultDict[mod])
            # Calculating numerical list for module
            numList = lstToValLst.listToValueList(mod,varList,first_time)
            
            # Initalizing dictionary for the current module
            modDict = dict()
            
            # Assigning each numerical value to a name in the module's dictionary
            for num, name in zip(numList,nameList):
                modDict[name] = num
            
            if first_time == True:
                ftp.firstTimePrint(mod,modDict,TrustedDict[mod])
            else:
            
                # If in debug mode, print symbolic dictionary
                if logging.getLogger().getEffectiveLevel() == 10:

                    # Create temporary dictionary
                    tempDict = dict()

                    # Store symbolic expressions in dictionary
                    for var, name in zip(varList,nameList):
                        tempDict[name] = var

                    logging.debug('Symbolic expression: \n' + str(tempDict) + '\n')
                    logging.debug('Trusted values: \n' + str(TrustedDict[mod]) + '\n')

                    del tempDict
                
                logging.debug('Calculated values: \n' + str(modDict) + '\n')
                
                # Comparing calculated values and trusted values
                valuesIdentical = cmp(modDict,TrustedDict[mod])
                
                if valuesIdentical != 0:
                    logging.error(mod + ': Found difference between calculated values and trusted values.')
                    logging.error('Now printing each value.')
                    
                    for var in modDict:
                        logging.error('\n' + var + ': Trusted value = ' + str(TrustedDict[mod][var]) + ' , Calculated Value = ' + str(modDict[var]))
                
                else:
                    logging.info('Completed module ' + mod + ' with no errors.\n')
                self.assertEqual(valuesIdentical, 0)
            
               
            
#     # Testing [cf,hDD,...,bet] for cartesian modules
#     def test_cart_ID(self):
#         for mod, trusted_list in zip(cartMods,cartSumID):
            
#             logging.info('\nChecking BSSN quantities (from Cartesian ADM) in ' + str(mod))
            
#             cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Cartesian", mod.Cartxyz, mod.gammaCartDD,mod.KCartDD, mod.alphaCart, mod.betaCartU, mod.BCartU)
            
#             lst = createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)
            
#             result_list = ltvl.listToValueList(mod,lst,first_time)

#             if first_time == True:
#                 ftp.firstTimePrint(mod,result_list,trusted_list)
#             else:
#                 good = ce.calcError(mod,result_list,trusted_list)
#                 if good:
#                     logging.info('\nJust completed checking BSSN quantities (from Cartesian ADM) in ' + str(mod) + '\n')
#                 else:
#                     self.assertTrue(good)
            
#     # Testing [cf,hDD,...,bet] for spherical modules
#     def test_sph_ID(self):
#         for mod, trusted_list in zip(sphMods,sphSumID):
                        
#             logging.info('\nChecking BSSN quantities (from Spherical ADM) in ' + str(mod))
            
#             Sph_r_th_ph = [mod.r,mod.th,mod.ph]
#             cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Spherical", Sph_r_th_ph, mod.gammaSphDD, mod.KSphDD, mod.alphaSph, mod.betaSphU, mod.BSphU)
            
#             lst = createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

#             result_list = ltvl.listToValueList(mod,lst,first_time)
            
#             if first_time == True:
#                 ftp.firstTimePrint(mod,result_list,trusted_list)
#             else:
#                 good = ce.calcError(mod,result_list,trusted_list)
#                 if good:
#                     logging.info('\nJust completed checking BSSN quantities (from Spherical ADM) in ' + str(mod) + '\n')
#                 else:
#                     self.assertTrue(good)
            

                
################################
######## Subfunctions ##########
################################

# Creates [lst] which contains all information stored in inputs [cf,...,betU]
def createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU):
    lst = [cf,alpha,trK]
    for i in range(3):
        lst.append(lambdaU[i])
        lst.append(vetU[i])
        lst.append(betU[i])
        for j in range(i,3):
            lst.append(hDD[i][j])
            lst.append(aDD[i][j])
    return lst 
            
# Creates [lst] which contains all information stored in inputs [alpha,...,K]
def createADMList(alpha,beta,B,gamma,K):
    
    lst = [alpha]
    for i in range(3):
        lst.append(beta[i])
        lst.append(B[i])
        for j in range(3):
            lst.append(gamma[i][j])
            lst.append(K[i][j])   
    return lst       


# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()

