import unittest
from sympy import Integer,Symbol,symbols,simplify,Rational,Function,srepr,sin,cos,exp,log,Abs,Add,Mul,Pow,preorder_traversal,N,Float,S,var,sympify
import NRPy_param_funcs as par
import BSSN.BSSN_RHSs_new as rhs
import BSSN.BSSN_gauge_RHSs as gaugerhs
import random
import sys
import logging
import trustedValues as tv
import calcError as ce
import firstTimePrint as ftp
import listToValueList as ltvl
from mpmath import *

# Trusted values for scalars, vectors, and tensors
RHS_scalars = [tv.BSSN_rhs_scalars,tv.BSSN_gaugerhs_scalars]
RHS_vectors = [tv.BSSN_rhs_vectors,tv.BSSN_gaugerhs_vectors]
RHS_tensors = [tv.BSSN_rhs_tensors]

# Change level based on desired amount of output. 
# ERROR -> Ouputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
logging.basicConfig(level=logging.DEBUG)

# Set following line to True if need to calculate trustedValue for the first time
first_time = True

class TestStringMethods(unittest.TestCase):
    
    # Initial setup for calculations
    par.set_parval_from_str("BSSN.BSSN_gauge_RHSs::ShiftEvolutionOption", "GammaDriving2ndOrder_Covariant")
    rhs.BSSN_RHSs()
    gaugerhs.BSSN_gauge_RHSs()
    
    # Testing scalars
    def test_BSSN_RHSs_scalars(self):
        
        ## Testing RHS scalars
        logging.info('\nCurrently working on RHS scalars module ' + str(rhs))
        
        lst = [rhs.cf_rhs,rhs.trK_rhs]
        
        result_list = ltvl.listToValueList(rhs,lst,first_time)
        trusted_list = RHS_scalars[0]
        
        if first_time == True:
            ftp.firstTimePrint(rhs,result_list,trusted_list) 
        else:
            good = ce.calcError(rhs,result_list,trusted_list)
            if good:     
                logging.info('\nJust completed RHS scalars module ' + str(rhs) + '\n')
            else:
                self.assertTrue(good)
        
        ## Testing gauge RHS scalars
        logging.info('\nCurrently working on gauge RHS scalars module ' + str(gaugerhs))
        
        lst = [gaugerhs.alpha_rhs]
        
        result_list = ltvl.listToValueList(gaugerhs,lst,first_time)
        trusted_list = RHS_scalars[1]
        
        if first_time == True:
            ftp.firstTimePrint(rhs,result_list,trusted_list) 
        else:
            good = ce.calcError(rhs,result_list,trusted_list)
            if good:     
                logging.info('\nJust completed gauge RHS scalars module ' + str(rhs) + '\n')
            else:
                self.assertTrue(good)
    
    # Testing vectors
    def test_BSSN_RHSs_vectors(self):
    
        ## Testing RHS scalars
        logging.info('\nCurrently working on RHS vectors module ' + str(rhs))
        
        lst = []
        for i in range(3):
            lst.append(rhs.lambda_rhsU[i])
        
        result_list = ltvl.listToValueList(rhs,lst,first_time)
        trusted_list = RHS_vectors[0]
        
        if first_time == True:
            ftp.firstTimePrint(rhs,result_list,trusted_list) 
        else:
            good = ce.calcError(rhs,result_list,trusted_list)
            if good:     
                logging.info('\nJust completed RHS vectors module ' + str(rhs) + '\n')
            else:
                self.assertTrue(good)
        
        ## Testing gauge RHS scalars
        logging.info('\nCurrently working on gauge RHS vectors module ' + str(gaugerhs))
        
        lst = []
        for i in range(3):
            lst.append(gaugerhs.bet_rhsU[i])
            lst.append(gaugerhs.vet_rhsU[i])
        
        result_list = ltvl.listToValueList(gaugerhs,lst,first_time)
        trusted_list = RHS_vectors[1]
        
        if first_time == True:
            ftp.firstTimePrint(rhs,result_list,trusted_list) 
        else:
            good = ce.calcError(rhs,result_list,trusted_list)
            if good:     
                logging.info('\nJust completed gauge RHS vectors module ' + str(rhs) + '\n')
            else:
                self.assertTrue(good)

    # Testing tensors
    def test_BSSN_RHSs_tensors(self):
    
        ## Testing RHS tensors
        logging.info('\nCurrently working on RHS tensors module ' + str(rhs)+ '\n Note: This may take a while.')
        
        lst = []
        for i in range(3):
            for j in range(i,3):
                lst.append(rhs.a_rhsDD[i][j])
                lst.append(rhs.h_rhsDD[i][j])
        
        result_list = ltvl.listToValueList(rhs,lst,first_time)
        trusted_list = RHS_tensors[0]
        
        if first_time == True:
            ftp.firstTimePrint(rhs,result_list,trusted_list) 
        else:
            good = ce.calcError(rhs,result_list,trusted_list)
            if good:     
                logging.info('\nJust completed RHS tensors module ' + str(rhs) + '\n')
            else:
                self.assertTrue(good)
        
        ## No gauge RHS tensors to test

if __name__ == '__main__':
    unittest.main()
    
