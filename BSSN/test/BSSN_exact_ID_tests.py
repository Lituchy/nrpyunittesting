import unittest
# First we import needed core NRPy+ modules
import NRPy_param_funcs as par
import reference_metric as rfm
import grid as gri
from sympy import Integer,Symbol,symbols,simplify,Rational,Function,srepr,sin,cos,exp,log,Abs,Add,Mul,Pow,preorder_traversal,N,Float,S,var,sympify
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

import sys
import logging

mp.dps = tv.precision


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

# Change level based on desired amount of output. 
# ERROR -> Ouputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
logging.basicConfig(level=logging.DEBUG)

# Set following line to True if need to calculate trustedValue for the first time
first_time = False

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
    
    
    # Testing [alpha,beta,...,K] for cartesian modules
    def test_cart_ADM(self):
        
        for mod, trusted_list in zip(cartMods,cartSumADM):
            
            logging.info('\nChecking Cartesian ADM ID generated by module ' + str(mod))
            
            # Creates list of parameters
            lst = createADMList(mod.alphaCart,mod.betaCartU,mod.BCartU,mod.gammaCartDD,mod.KCartDD)
            
            # Creates list of values
            result_list = tv.listToValueList(mod,lst)

            if first_time == True:
                tv.firstTimePrint(mod,result_list,trusted_list)
            else:
                # Next we compute the log_10 of the relative error. It should
                #    be a number < -2/3 * precision (i.e., when precision is 30, we
                #    should get more than 20 significant digits of agreement with the 
                #    trusted result, or the test fails.
                good = tv.calcError(mod,result_list,trusted_list)
                if good:
                    logging.info('\nJust completed checking Cartesian ADM ID generated by module ' + str(mod) + '\n')
                else:
                    self.assertTrue(good)
            
                
    # Testing [alpha,beta,...,K] for spherical modules
    def test_sph_ADM(self):
        for mod, trusted_list in zip(sphMods,sphSumADM):
            
            logging.info('\nChecking Spherical ADM ID generated by module ' + str(mod))
            
            # Creates list of parameters
            lst = createADMList(mod.alphaSph,mod.betaSphU,mod.BSphU,mod.gammaSphDD,mod.KSphDD)
            
            # Creates list of values
            result_list = tv.listToValueList(mod,lst)
            
            # Uncomment following line if need to calculate trustedValue for the first time

            if first_time == True:
                tv.firstTimePrint(mod,result_list,trusted_list)
            else:
                # Next we compute the log_10 of the relative error. It should
                #    be a number < -2/3 * precision (i.e., when precision is 30, we
                #    should get more than 20 significant digits of agreement with the 
                #    trusted result, or the test fails.
                good = tv.calcError(mod,result_list,trusted_list)
                if good:
                    logging.info('\nJust completed checking Spherical ADM ID generated by module ' + str(mod) + '\n')
                else:
                    self.assertTrue(good)
            
    # Testing [cf,hDD,...,bet] for cartesian modules
    def test_cart_ID(self):
        for mod, trusted_list in zip(cartMods,cartSumID):
            
            logging.info('\nChecking BSSN quantities (from Cartesian ADM) in ' + str(mod))
            
            cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Cartesian", mod.Cartxyz, mod.gammaCartDD,mod.KCartDD, mod.alphaCart, mod.betaCartU, mod.BCartU)
            
            lst = createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)
            
            result_list = tv.listToValueList(mod,lst)

            if first_time == True:
                tv.firstTimePrint(mod,result_list,trusted_list)
            else:
                good = tv.calcError(mod,result_list,trusted_list)
                if good:
                    logging.info('\nJust completed checking BSSN quantities (from Cartesian ADM) in ' + str(mod) + '\n')
                else:
                    self.assertTrue(good)
            
    # Testing [cf,hDD,...,bet] for spherical modules
    def test_sph_ID(self):
        for mod, trusted_list in zip(sphMods,sphSumID):
                        
            logging.info('\nChecking BSSN quantities (from Spherical ADM) in ' + str(mod))
            
            Sph_r_th_ph = [mod.r,mod.th,mod.ph]
            cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Spherical", Sph_r_th_ph, mod.gammaSphDD, mod.KSphDD, mod.alphaSph, mod.betaSphU, mod.BSphU)
            
            lst = createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

            result_list = tv.listToValueList(mod,lst)
            
            # Uncomment following line if need to calculate trustedValue for the first time
            if first_time == True:
                tv.firstTimePrint(mod,result_list,trusted_list)
            else:
                good = tv.calcError(mod,result_list,trusted_list)
                if good:
                    logging.info('\nJust completed checking BSSN quantities (from Spherical ADM) in ' + str(mod) + '\n')
                else:
                    self.assertTrue(good)
            

                
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
