from sympy import srepr, Pow, Add, Mul, Float, Symbol, Integer, cos, sin
# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below. This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mp, mpf, fabs, sqrt
from random import seed, random
from re import sub
from trustedValuesDict import trustedValuesDict

# Takes in a list [lst] and returns the list with each index evaluated 
# according to parameters (seed, precision) in trustedValues

# Called by runTest

def listToValueList(lst,first_time):
    
    precision = trustedValuesDict["precision"]

    mp.dps = precision
    
    # Replace all integer fractions with the correct floating point representation:
    index = 0
    orig_lst = []
    for expr in lst:
        orig_lst.append(expr)
        string = srepr(expr)
        string2 = sub('Rational\(([0-9]+), ([0-9]+)\)',
                         "((Float('\\1',"+str(2*precision)+"))/(Float('\\2',"+str(2*precision)+")))", string)
        string3 = sub('Rational\((-[0-9]+), ([0-9]+)\)',
                         "((Float('\\1',"+str(2*precision)+"))/(Float('\\2',"+str(2*precision)+")))", string2)
        newexpr = eval(string3)
        lst[index] = newexpr
        index += 1

        del string, string2, string3, newexpr

    del index

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

    del list_symbol_strings

    # Set the random seed according to trustedValues.seed:
    seed(trustedValuesDict["seed"])

    # Next we will write a short Python code that first declares all
    #    of the free variables in the "everything" expression
    #    to random values with 30 significant digits of precision.
    #    (This is accomplished by calling random.random() to get
    #     a 16-significant-digit random number between 0 and 1,
    #     and then taking the 30-significant-digit square root
    #     of that number.)
    stringexec = """
from sympy import Integer,Symbol,symbols,simplify,Rational,Function,srepr,sin,cos,exp,log,Abs,Add,Mul,Pow,preorder_traversal,N,Float,S,var,sympify
import mpmath as mpm
mpm.mp.dps = """+str(precision)+"\n"
    
    for var in list_free_symbols:
        # BE CAREFUL: You must declare all variables using mpm.mpf('string')!
        #   http://mpmath.org/doc/1.1.0/basics.html#providing-correct-input
        # First make sure M_PI is set to its correct value, pi, to the desired number of significant digits:
        if str(var) == "M_PI":
            stringexec += str(var)+" = mpm.pi\n"
        # Then make sure M_SQRT1_2 is set to its correct value, 1/sqrt(2), to the desired number of significant digits:
        elif str(var) == "M_SQRT1_2":
            stringexec += str(var)+" = mpm.mpf(1/mpm.sqrt(2))\n"
        # All other free variables are set to random numbers
        else:
            stringexec += str(var)+" = mpm.mpf(\'"+str(sqrt(mpf(random())))+"\')\n"

    del list_free_symbols

    # Then it creates the code that evaluates the result
    #    to 30 significant digits.
    stringexec += "lst = " + str(lst)
    #print(str(lst[2]))
    
    #print(stringexec)
    # https://stackoverflow.com/questions/38817962/python-3-need-from-exec-to-return-values
    # Finally we execute stringexec to a local namespace "loc", and store the
    #    result of the evaluated "everything" expression to "result".
    #
    loc = {}
    exec(stringexec, {}, loc)
    evaled_lst = loc['lst']

    if first_time:
        index = 0
        for result in evaled_lst:
            if result != 0 and fabs(result) < 100*10**(-precision):
                print("Found |result| ("+str(fabs(result))+") close to zero. Checking if indeed it should be zero.")
                # Now double the precision and redo. If number drops in magnitude
                loc2xprec = {}
                stringexec = stringexec.replace("mpm.mp.dps = "+str(precision),"mpm.mp.dps = "+str(2*precision))
                exec(stringexec, {}, loc2xprec)
                evaled_lst2xprec = loc2xprec['lst']
                if fabs(evaled_lst2xprec[index]) < 100*10**(-2*precision):
                    print("After re-evaluating with twice the digits of precision, |result| dropped to "+str(evaled_lst2xprec[index])+". Setting value to zero")
                    evaled_lst[index] = 0
            index += 1

    # Make sure that all results in evaled_lst *except* zeros are mpm.mpf type!
    for i in range(len(evaled_lst)):
        if evaled_lst[i] != 0:
            evaled_lst[i] = mpf(str(evaled_lst[i]))
        
    return evaled_lst
