import unittest
import sympy as sp
from mpmath import *
import random
import sys
import trustedValues as tv

import BSSN.BrillLindquist as bl

mp.dps = tv.precision

def helper(mod):
    # Add all symbolic expressions generated in bl.BrillLindquist, store expression to SymPy variable "everything"

    arr = [mod.alphaCart]
    for i in range(3):
        arr.append(mod.betaCartU[i])
        arr.append(mod.BCartU[i])
        for j in range(3):
            arr.append(mod.gammaCartDD[i][j])
            arr.append(mod.KCartDD[i][j])
    
    
    # List all the free symbols in the "everything" expression.
    #   These variables will be automatically set to random
    #   values in the range [0,1) below.
    list_free_symbols = sum(arr).free_symbols
        
    # To ensure the random values are consistent for testing purposes, we will
    #    sort the list of free symbols. This requires that we first convert
    #    all SymPy symbols to strings, storing to list_symbol_strings,
    #    and then we'll use zip() to sort both lists in alphabetical order,
    #    based on the strings in the first list:
    list_symbol_strings = []
    for var in list_free_symbols:
        list_symbol_strings.append(str(var))
    
#     print(list_free_symbols)
#     print("\n\n")
#     print(list_symbol_strings)

    # https://stackoverflow.com/questions/13668393/python-sorting-two-lists
    list_symbol_strings, list_free_symbols = (list(x) for x in zip(*sorted(zip(list_symbol_strings, list_free_symbols))))
    
#     print("\n\n")
#     print(list_free_symbols)
    
#     print("\n\n")
#     print(list_symbol_strings)

#     print("\n\n")
#     print(arr[23])
    # Set the random seed:
    random.seed(tv.seed)

    # Next we will write a short Python code that first declares all
    #    of the free variables in the "everything" expression
    #    to random values with 30 significant digits of precision.
    #    (This is accomplished by calling random.random() to get
    #     a 16-significant-digit random number between 0 and 1,
    #     and then taking the 30-significant-digit square root
    #     of that number.)
    stringexec = "import sympy as sp\n" + "from mpmath import *\n" + "mp.dps =" + str(30) + "\n"
    
    for var in list_free_symbols:
#         print(var)
#         print('\n')
        stringexec += str(var)+" = sp.symbols(\'"+str(var)+"\')\n"
        stringexec += str(var)+" = "+str(sqrt(mpf(random.random())))+"\n"

    # Then it creates the code that evaluates the result
    #    to 30 significant digits.
#     stringexec += "result_local_namespace = mpf("+str(everything)+")"
    stringexec += "arr = " + str(arr)
    
#     print(stringexec)
    
    # https://stackoverflow.com/questions/38817962/python-3-need-from-exec-to-return-values
    # Finally we execute stringexec to a local namespace "loc", and store the
    #    result of the evaluated "everything" expression to "result".
    loc = {}
    exec(stringexec, {}, loc)
    result = loc['arr']
    return result

    
class MyTest(unittest.TestCase):
    # Keep 30 significant digits of precision

    bl.BrillLindquist(ComputeADMGlobalsOnly=True)
    
    def test_new(self):
        
        # BE CAREFUL: http://mpmath.org/doc/1.1.0/basics.html#providing-correct-input
        # We must import the trusted result manually:
        result_list = helper(bl)
#         print(result_list)
#         print(tv.cart_ID_ADM)
        
        for num, tnum in zip(result_list,tv.BSSN_cart_BL_ADM):
            if tnum == 0:
                log10_relative_error = log10(fabs(num))
            else:
                log10_relative_error = log10(fabs( (tnum - num ) / tnum ) )
            self.assertTrue(log10_relative_error < -20)
        
        #self.assertEqual(result,tv.cart_ID_ADM[0])
        
        # Next we compute the log_10 of the relative error. It should
        #    be a number < -20 (i.e., we should get more than 20 significant
        #    digits of agreement with the trusted result, or the test fails.
#         log10_relative_error = log10(fabs( ( BL_trusted_result - s ) / BL_trusted_result) )
#         self.assertTrue(log10_relative_error < -20)    
        

        
if __name__ == '__main__':
    unittest.main()

