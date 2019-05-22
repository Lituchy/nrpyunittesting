import unittest
# First we import needed core NRPy+ modules
import NRPy_param_funcs as par
import reference_metric as rfm
import grid as gri


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
cartHashADM = ['d1d9fb9bd0c0ce61c06e6e2f6e386040']
sphHashADM = ['41a4babe88c5572f99856d8488d2dd33','aa6595a764673abcd90d0cee586695ca','9e64640593017f2cbdba08da59690674']

# ID test hash values
cartHashID = ['eb6f859a0016fc1679c45af662ea32ef']
sphHashID = ['d3d62ac5b46869dd94d2bf19441822b2','b20d6ca8bf5dfeee0ad73a4018837585','6a0d074ccafa4f9361811032ce4c0e08']

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
    def test_cart_ID_ADM(self):
        for mod, val in zip(cartMods,cartHashADM):
            everything = mod.alphaCart
            for i in range(3):
                everything += mod.betaCartU[i] + mod.BCartU[i]
                for j in range(3):
                    everything += mod.gammaCartDD[i][j] + mod.KCartDD[i][j]
            md5sum = "empty"
            if sys.version_info[0]==2:
                md5sum = hashlib.md5(str(everything)).hexdigest()
            elif sys.version_info[0]==3:
                md5sum = hashlib.md5(str(everything).encode('utf-8')).hexdigest()

            #print(md5sum)
            self.assertEqual(md5sum, val)
    
    # Testing sum of parameters for spherical modules
    def test_sph_ID_ADM(self):
        for mod, val in zip(sphMods,sphHashADM):
            everything = mod.alphaSph
            for i in range(3):
                everything += mod.betaSphU[i] + mod.BSphU[i]
                for j in range(3):
                    everything += mod.gammaSphDD[i][j] + mod.KSphDD[i][j]
            md5sum = "empty"
            if sys.version_info[0]==2:
                md5sum = hashlib.md5(str(everything)).hexdigest()
            elif sys.version_info[0]==3:
                md5sum = hashlib.md5(str(everything).encode('utf-8')).hexdigest()
            
            #print(md5sum)
            self.assertEqual(md5sum, val)
        
    # Testing sum of converted parameters for cartesian modules
    def test_cart_ID(self):
        for mod, val in zip(cartMods,cartHashID):
            cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Cartesian", mod.Cartxyz, mod.gammaCartDD,mod.KCartDD, mod.alphaCart, mod.betaCartU, mod.BCartU)
            
            md5sum = generateIDHash(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

            #print(md5sum)
            self.assertEqual(md5sum, val)
            
            
    # Testing sum of converted parameters for spherical modules        
    def test_sph_ID(self):
        for mod, val in zip(sphMods,sphHashID):
            Sph_r_th_ph = [mod.r,mod.th,mod.ph]
            cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU = AtoB.Convert_Spherical_or_Cartesian_ADM_to_BSSN_curvilinear( "Spherical", Sph_r_th_ph, mod.gammaSphDD, mod.KSphDD, mod.alphaSph, mod.betaSphU, mod.BSphU)
            
            md5sum = generateIDHash(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU)

            #print(md5sum)
            self.assertEqual(md5sum, val)     

# Subfunction to generate the hash value for ID tests
def generateIDHash(cf,hDD,lambdaU,aDD,trK,alpha,vetU,betU):
    everything = cf+alpha+trK
    for i in range(3):
        everything += lambdaU[i]+vetU[i]+betU[i]
        for j in range(i,3):
            everything += hDD[i][j] + aDD[i][j]
    md5sum = "empty"
    if sys.version_info[0]==2:
        md5sum = hashlib.md5(str(everything)).hexdigest()
    elif sys.version_info[0]==3:
        md5sum = hashlib.md5(str(everything).encode('utf-8')).hexdigest()
    return md5sum

if __name__ == '__main__':
    unittest.main()

