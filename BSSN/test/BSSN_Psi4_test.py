import unittest
# First we import needed core NRPy+ modules
import NRPy_param_funcs as par
import reference_metric as rfm
import grid as gri
import sympy as sp

import BSSN.Psi4 as psi
import BSSN.Psi4_tetrads as psit

import hashlib
import sys

# Turns expression into hashed value
def get_md5sum(sympy_expr):
    if sys.version_info[0]==2:
        return hashlib.md5(str(sympy_expr)).hexdigest()
    elif sys.version_info[0]==3:
        return hashlib.md5(str(sympy_expr).encode('utf-8')).hexdigest()
    sys.exit(1)
    
class TestStringMethods(unittest.TestCase):
    
    # Set spatial dimension (must be 3 for BSSN)
    DIM = 3
    par.set_parval_from_str("grid::DIM",DIM)

    # Then we set the coordinate system for the numerical grid
    par.set_parval_from_str("reference_metric::CoordSystem","Spherical")
    rfm.reference_metric() # Create ReU, ReDD needed for rescaling B-L initial data, generating BSSN RHSs, etc.
    
    # Calling initial functions for Psi modules
    psi.Psi4(specify_tetrad=False)
    psit.Psi4_tetrads()
    
    def test_real_part_tetrad_false(self):
        
        everyvector = sp.sympify(0)
        
        for i in range(3):
            everyvector += psi.psi4_re_pt[i]
                        
        self.assertEqual(get_md5sum(everyvector), 'ff50fef2003fedf3a1466f707d6fce54')
        
    def test_im_part_tetrad_false(self):
    
        everyvector = sp.sympify(0)
        
        for i in range(3): 
            everyvector += psi.psi4_im_pt[i]
                       
        self.assertEqual(get_md5sum(everyvector), '645f487f414e489af60189160c533383')
        
    def test_tetrads(self):
        
        everyvector = sp.sympify(0)
        
        for i in range(4):
            everyvector += psit.l4U[i] + psit.n4U[i] + psit.mre4U[i] +  psit.mim4U[i]
            
        self.assertEqual(get_md5sum(everyvector), '7413124a0d0f978c297ec6060b4fdbcc')        
        
        
if __name__ == '__main__':
    unittest.main()
