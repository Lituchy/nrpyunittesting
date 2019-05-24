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
    
    logging.basicConfig(level=logging.DEBUG)
    
    # Testing [alpha,beta,...,K] for cartesian modules
    def test_cart_ADM(self):
        
        for mod, trusted_list in zip(cartMods,cartSumADM):
            
            logging.info('\nCurrently working on ADM module ' + str(mod))
            
            # Creates list of parameters
            lst = createADMList(mod.alphaCart,mod.betaCartU,mod.BCartU,mod.gammaCartDD,mod.KCartDD)
            
            # Creates list of values
            result_list = tv.listToValueList(lst)
            
            # Uncomment following line if need to calculate trustedValue for the first time
            # tv.firstTimePrint(mod,result_list,trusted_list)

            # Next we compute the log_10 of the relative error. It should
            #    be a number < -2/3 * precision (i.e., when precision is 30, we
            #    should get more than 20 significant digits of agreement with the 
            #    trusted result, or the test fails.
            for res, val in zip(result_list, trusted_list):
                if val == 0:
                    log10_relative_error = log10(fabs(res))
                else:
                    log10_relative_error = log10(fabs( (val - res ) / val ) )
                good = (log10_relative_error < (tv.precision / -2))
                if not good:
                    logging.error('\n\n Failed with ' + str(mod) + '\n\n')
                    self.assertTrue(good)

            logging.info('\nJust completed ADM module ' + str(mod))
            
                
    # Testing [alpha,beta,...,K] for spherical modules
    def test_sph_ADM(self):
        for mod, trusted_list in zip(sphMods,sphSumADM):
            
            logging.info('\nCurrently working on ADM module ' + str(mod))
            
            # Creates list of parameters
            lst = createADMList(mod.alphaSph,mod.betaSphU,mod.BSphU,mod.gammaSphDD,mod.KSphDD)
            
            # Creates list of values
            result_list = tv.listToValueList(lst)
            
            # Uncomment following line if need to calculate trustedValue for the first time
            # tv.firstTimePrint(mod,result_list,trusted_list)
            
            
            # Next we compute the log_10 of the relative error. It should
            #    be a number < -2/3 * precision (i.e., when precision is 30, we
            #    should get more than 20 significant digits of agreement with the 
            #    trusted result, or the test fails.
            for res, val in zip(result_list, trusted_list):
                if val == 0:
                    log10_relative_error = log10(fabs(res))
                else:
                    log10_relative_error = log10(fabs( (val - res ) / val ) )
                good = (log10_relative_error < (tv.precision / -2))
                if not good:
                    logging.error('\n\n Failed with ' + str(mod) + '\n\n')
                    self.assertTrue(good)

            logging.info('\nJust completed ADM module ' + str(mod))
            
    # Testing [cf,hDD,...,bet] for cartesian modules
    def test_cart_ID(self):
        for mod, trusted_list in zip(cartMods,cartSumID):
            
            logging.info('\nCurrently working on ID module ' + str(mod))
            
            cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Cartesian", mod.Cartxyz, mod.gammaCartDD,mod.KCartDD, mod.alphaCart, mod.betaCartU, mod.BCartU)
            
            lst = createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)
            
            result_list = tv.listToValueList(lst)
            
            # Uncomment following line if need to calculate trustedValue for the first time
            # tv.firstTimePrint(mod,result_list,trusted_list)
            
            for res, val in zip(result_list, trusted_list):
                if val == 0:
                    log10_relative_error = log10(fabs(res))
                else:
                    log10_relative_error = log10(fabs( (val - res ) / val ) )
                good = (log10_relative_error < (tv.precision / -2))
                if not good:
                    logging.error('\n\n Failed with ' + str(mod) + '\n\n')
                    self.assertTrue(good)

            logging.info('\nJust completed ID module ' + str(mod))
            
    # Testing [cf,hDD,...,bet] for spherical modules
    def test_sph_ID(self):
        for mod, trusted_list in zip(sphMods,sphSumID):
                        
            logging.info('\nCurrently working on ID module ' + str(mod))
            
            Sph_r_th_ph = [mod.r,mod.th,mod.ph]
            cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Spherical", Sph_r_th_ph, mod.gammaSphDD, mod.KSphDD, mod.alphaSph, mod.betaSphU, mod.BSphU)
            
            lst = createIDList(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

            result_list = tv.listToValueList(lst)
            
            # Uncomment following line if need to calculate trustedValue for the first time
            # tv.firstTimePrint(mod,result_list,trusted_list)

            for res, val in zip(result_list, trusted_list):
                if val == 0:
                    log10_relative_error = log10(fabs(res))
                else:
                    log10_relative_error = log10(fabs( (val - res ) / val ) )
                good = (log10_relative_error < (tv.precision / -2))
                if not good:
                    logging.error('\n\n Failed with ' + str(mod) + '\n\n')
                    self.assertTrue(good)

            logging.info('\nJust completed ID module ' + str(mod))
            

                
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

