import unittest
import sympy as sp
import NRPy_param_funcs as par
import BSSN.BSSN_RHSs_new as rhs
import BSSN.BSSN_gauge_RHSs as gaugerhs
import random
import sys
import logging
import trustedValues as tv
from mpmath import *


RHS_scalars = [tv.BSSN_rhs_scalars,tv.BSSN_gaugerhs_scalars]
RHS_vectors = [tv.BSSN_rhs_vectors,tv.BSSN_gaugerhs_vectors]
RHS_tensors = [tv.BSSN_rhs_tensors]

# Change level based on desired amount of output. 
# ERROR -> Ouputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
logging.basicConfig(level=logging.DEBUG)

class TestStringMethods(unittest.TestCase):
    par.set_parval_from_str("BSSN.BSSN_gauge_RHSs::ShiftEvolutionOption", "GammaDriving2ndOrder_Covariant")
    rhs.BSSN_RHSs()
    gaugerhs.BSSN_gauge_RHSs()
    

    def test_BSSN_RHSs_scalars(self):
        
        # Testing RHS scalars
        logging.info('\nCurrently working on RHS scalars module ' + str(rhs))
        
        lst = [rhs.cf_rhs,rhs.trK_rhs]
        
        result_list = tv.listToValueList(lst)
        trusted_list = RHS_scalars[0]
        
        # Uncomment following line if need to calculate trustedValue for the first time
        # tv.firstTimePrint(rhs,result_list,trusted_list) 
        
        good = tv.calcError(rhs,result_list,trusted_list)
        if good:     
            logging.info('\nJust completed RHS scalars module ' + str(rhs) + '\n')
        else:
            self.assertTrue(good)
        
        # Testing gauge RHS scalars
        logging.info('\nCurrently working on gauge RHS scalars module ' + str(gaugerhs))
        
        lst = [gaugerhs.alpha_rhs]
        
        result_list = tv.listToValueList(lst)
        trusted_list = RHS_scalars[1]
        
        # Uncomment following line if need to calculate trustedValue for the first time
        # tv.firstTimePrint(gaugerhs,result_list,trusted_list) 
        
        good = tv.calcError(gaugerhs,result_list,trusted_list)
        if good:     
            logging.info('\nJust completed gauge RHS scalars module ' + str(gaugerhs) + '\n')
        else:
            self.assertTrue(good)

    def test_BSSN_RHSs_vectors(self):
    
        # Testing RHS scalars
        logging.info('\nCurrently working on RHS vectors module ' + str(rhs))
        
        lst = []
        for i in range(3):
            lst.append(rhs.lambda_rhsU[i])
        
        result_list = tv.listToValueList(lst)
        trusted_list = RHS_vectors[0]
        
        # Uncomment following line if need to calculate trustedValue for the first time
        # tv.firstTimePrint(rhs,result_list,trusted_list) 
        
        good = tv.calcError(rhs,result_list,trusted_list)
        if good:     
            logging.info('\nJust completed RHS vectors module ' + str(rhs) + '\n')
        else:
            self.assertTrue(good)
        
        # Testing gauge RHS scalars
        logging.info('\nCurrently working on gauge RHS vectors module ' + str(gaugerhs))
        
        lst = []
        for i in range(3):
            lst.append(gaugerhs.bet_rhsU[i])
            lst.append(gaugerhs.vet_rhsU[i])
        
        result_list = tv.listToValueList(lst)
        trusted_list = RHS_vectors[1]
        
        # Uncomment following line if need to calculate trustedValue for the first time
        # tv.firstTimePrint(gaugerhs,result_list,trusted_list) 
        
        good = tv.calcError(gaugerhs,result_list,trusted_list)
        if good:     
            logging.info('\nJust completed gauge RHS scalars vectors ' + str(gaugerhs) + '\n')
        else:
            self.assertTrue(good)


    def test_BSSN_RHSs_tensors(self):
#         everytensor = sp.sympify(0)
#         for i in range(3):
#             for j in range(i,3):
#                 everytensor += rhs.a_rhsDD[i][j] + rhs.h_rhsDD[i][j]
#         md5sum = get_md5sum(everytensor)
# #        print("tensor: ",md5sum)
#         self.assertEqual(md5sum, 'd84fc94358305b7135dc18680089dff9')
    
        # Testing RHS tensors
        logging.info('\nCurrently working on RHS tensors module ' + str(rhs)+ '\n Note: This may take a while.')
        
        lst = []
        for i in range(3):
            for j in range(i,3):
                lst.append(rhs.a_rhsDD[i][j])
                lst.append(rhs.h_rhsDD[i][j])
        
        result_list = tv.listToValueList(lst)
        trusted_list = RHS_tensors[0]
        
        # Uncomment following line if need to calculate trustedValue for the first time
        tv.firstTimePrint(rhs,result_list,trusted_list) 
        
        good = tv.calcError(rhs,result_list,trusted_list)
        if good:     
            logging.info('\nJust completed RHS tensors module ' + str(rhs) + '\n')
        else:
            self.assertTrue(good)

if __name__ == '__main__':
    unittest.main()
    
