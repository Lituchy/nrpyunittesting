import unittest
# First we import needed core NRPy+ modules
import NRPy_param_funcs as par
import reference_metric as rfm
import grid as gri

import BSSN.Psi4 as psi

class TestStringMethods(unittest.TestCase):
    
    # Set spatial dimension (must be 3 for BSSN)
    global DIM = 3
    par.set_parval_from_str("grid::DIM",DIM)

    # Then we set the coordinate system for the numerical grid
    par.set_parval_from_str("reference_metric::CoordSystem","Spherical")
    rfm.reference_metric() # Create ReU, ReDD needed for rescaling B-L initial data, generating BSSN RHSs, etc.
    
    psi.Psi4(specify_tetrad=False)
    
    def test_real_part(self):
        
        everything = 0
        
        for i in range(DIM):
            everything += psi.psi4_re_pt[i]
            
        md5sum = "empty"
        if sys.version_info[0]==2:
            md5sum = hashlib.md5(str(everything)).hexdigest()
        elif sys.version_info[0]==3:
            md5sum = hashlib.md5(str(everything).encode('utf-8')).hexdigest()
            
        self.assertEqual(md5sum, "real")
        
    def test_im_part(self)
    
        everything = 0
        
        for i in range(DIM): 
            everything += psi.psi4_im_pt[i]
            
        md5sum = "empty"
        if sys.version_info[0]==2:
            md5sum = hashlib.md5(str(everything)).hexdigest()
        elif sys.version_info[0]==3:
            md5sum = hashlib.md5(str(everything).encode('utf-8')).hexdigest()
            
        self.assertEqual(md5sum, "real")
