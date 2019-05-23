import unittest
# First we import needed core NRPy+ modules
import NRPy_param_funcs as par
import reference_metric as rfm
import grid as gri
import sympy as sp
from mpmath import *
import random
import trustedValues as tv


# Cartesian
import BSSN.BrillLindquist as bl

# Spherical
import BSSN.ShiftedKerrSchild as sks
import BSSN.StaticTrumpet as st
import BSSN.UIUCBlackHole as ubh

import BSSN.ADM_Exact_Spherical_or_Cartesian_to_BSSNCurvilinear as AtoB

import hashlib
import sys

# Lists of modules
cartMods = [bl]
sphMods = [sks,st,ubh]

# Lists of hash values for respective modules

# ADM test hash values
cartSumADM = [tv.BSSN_cart_BL_ADM]
sphSumADM = [tv.BSSN_sph_SKS_ADM,tv.BSSN_sph_ST_ADM,tv.BSSN_sph_UBH_ADM]

# ID test hash values
cartSumID = [tv.BSSN_cart_BL_ID]
sphSumID = [tv.BSSN_sph_SKS_ID,tv.BSSN_sph_ST_ID,tv.BSSN_sph_UBH_ID]

mp.dps = tv.precision

# Python unittest class
class TestStringMethods(unittest.TestCase):
    
    # Set spatial dimension (must be 3 for BSSN)
    DIM = 3
    par.set_parval_from_str("grid::DIM",DIM)

    # Then we set the coordinate system for the numerical grid
    par.set_parval_from_str("reference_metric::CoordSystem","Spherical")
    rfm.reference_metric() # Create ReU, ReDD needed for rescaling B-L initial data, generating BSSN RHSs, etc.
    
    # Calling functions to initialize each module
    cartMods[0].BrillLindquist(ComputeADMGlobalsOnly = True)
    sphMods[0].ShiftedKerrSchild(ComputeADMGlobalsOnly = True)
    sphMods[1].StaticTrumpet(ComputeADMGlobalsOnly = True)
    sphMods[2].UIUCBlackHole(ComputeADMGlobalsOnly = True)
    
    # Testing sum of parameters for cartesian modules
    def test_cart_ADM(self):
        for mod, trusted_list in zip(cartMods,cartSumADM):
            
            # Creates list of parameters
            lst = createADMList(mod.alphaCart,mod.betaCartU,mod.BCartU,mod.gammaCartDD,mod.KCartDD)
            
            # Creates list of values
            result_list = listToValueList(lst)

            # Next we compute the log_10 of the relative error. It should
            #    be a number < -2/3 * precision (i.e., when precision is 30, we
            #    should get more than 20 significant digits of agreement with the 
            #    trusted result, or the test fails.
            for res, val in zip(result_list, trusted_list):
                if val == 0:
                    log10_relative_error = log10(fabs(res))
                else:
                    log10_relative_error = log10(fabs( (val - res ) / val ) )
                self.assertTrue(log10_relative_error < tv.precision * (-2/3))
                
    # Testing sum of parameters for spherical modules
    def test_sph_ADM(self):
        for mod, trusted_list in zip(sphMods,sphSumADM):
            
            # Creates list of parameters
            lst = createADMList(mod.alphaSph,mod.betaSphU,mod.BSphU,mod.gammaSphDD,mod.KSphDD)
            
            # Creates list of values
            result_list = listToValueList(lst)
            
            # Uncomment if need to calculate trustedValue for the first time
            # print(mod)
            # print(result_list)
            
            # Next we compute the log_10 of the relative error. It should
            #    be a number < -2/3 * precision (i.e., when precision is 30, we
            #    should get more than 20 significant digits of agreement with the 
            #    trusted result, or the test fails.
            for res, val in zip(result_list, trusted_list):
                if val == 0:
                    log10_relative_error = log10(fabs(res))
                else:
                    log10_relative_error = log10(fabs( (val - res ) / val ) )
                self.assertTrue(log10_relative_error < tv.precision * (-2/3))                
        
# # Testing sum of converted parameters for cartesian modules
#     def test_cart_ID(self):
#         for mod, val in zip(cartMods,cartSumID):
#             cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Cartesian", mod.Cartxyz, mod.gammaCartDD,mod.KCartDD, mod.alphaCart, mod.betaCartU, mod.BCartU)
            
#             everything = idTestEverything(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

#             #print(md5sum)
#             self.assertEqual(expression2num(everything), val)
            
            
#     # Testing sum of converted parameters for spherical modules        
#     def test_sph_ID(self):
#         for mod, val in zip(sphMods,sphSumID):
#             Sph_r_th_ph = [mod.r,mod.th,mod.ph]
#             cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Spherical", Sph_r_th_ph, mod.gammaSphDD, mod.KSphDD, mod.alphaSph, mod.betaSphU, mod.BSphU)
            
#             everything = idTestEverything(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

#             #print(md5sum)
#             self.assertEqual(expression2num(everything), val)  

################################
######## Subfunctions ##########
################################
            
def idTestEverything(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU):
    everything = cf+alpha+trK
    for i in range(3):
        everything += lambdaU[i]+vetU[i]+betU[i]
        for j in range(i,3):
            everything += hDD[i][j] + aDD[i][j]
    return everything  
            
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

# Takes in a list [lst] and returns the list with each index evaluated 
#     according to parameters (seed, precision) in trustedValues 
def listToValueList(lst):
    
    # List all the free symbols in the expressions in [lst].
    #   These variables will be automatically set to random
    #   values in the range [0,1) below.
    list_free_symbols = sum(lst).free_symbols

    # To ensure the random values are consistent for testing purposes, we will
    #    sort the list of free symbols. This requires that we first convert
    #    all SymPy symbols to strings, storing to list_symbol_strings,
    #    and then we'll use zip() to sort both lists in alphabetical order,
    #    based on the strings in the first list:
    list_symbol_strings = []
    for var in list_free_symbols:
        list_symbol_strings.append(str(var))

    # https://stackoverflow.com/questions/13668393/python-sorting-two-lists
    list_symbol_strings, list_free_symbols = (list(x) for x in zip(*sorted(zip(list_symbol_strings, list_free_symbols))))

    # Set the random seed according to trustedValues.seed:
    random.seed(tv.seed)

    # Next we will write a short Python code that first declares all
    #    of the free variables in the "everything" expression
    #    to random values with 30 significant digits of precision.
    #    (This is accomplished by calling random.random() to get
    #     a 16-significant-digit random number between 0 and 1,
    #     and then taking the 30-significant-digit square root
    #     of that number.)
    stringexec = "from sympy import *\n" + "from mpmath import *\n" + "mp.dps = " + str(tv.precision) + "\n"
    
    for var in list_free_symbols:
        stringexec += str(var)+" = symbols(\'"+str(var)+"\')\n"
        stringexec += str(var)+" = "+str(sqrt(mpf(random.random())))+"\n"

    # Then it creates the code that evaluates the result
    #    to 30 significant digits.
    stringexec += "lst = " + str(lst)
    
    # https://stackoverflow.com/questions/38817962/python-3-need-from-exec-to-return-values
    # Finally we execute stringexec to a local namespace "loc", and store the
    #    result of the evaluated "everything" expression to "result".
    loc = {}
    exec(stringexec, {}, loc)
    return loc['lst']

# Necessary for unittest class to work properly
if __name__ == '__main__':
    unittest.main()

