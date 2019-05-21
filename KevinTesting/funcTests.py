# Proof of concept: modules with same methods and variables can be abstracted
import unittest

# Import modules to be tested
import myFunc as mF
import myFunc2 as mF2

# Store modules in a list
modules = [mF,mF2]

# Predetermined values that we know to be correct
# magSq for funcTests -> hashed string for BSSN
magSq = [29,2]

# Unit testing class
class testFuncs(unittest.TestCase):
    
    # Initialize variables for all modules
    for mod in modules:
        mod.run()
    
    
    # Apply given tests to all modules
    def test_x_lt_y(self):
        for mod in modules:
            self.assertTrue(mod.x < mod.y)
   
    def test_y_lt_z(self):
        for mod in modules:
            self.assertTrue(mod.y < mod.z)
    
    
    # Test current values against values we know to be correct
    # to ensure that we didn't break anything
    def test_mags_same(self):
        for mod, val in zip(modules,magSq):
            self.assertTrue(mod.magSq() == val)

        
if __name__ == '__main__':
    unittest.main()
        