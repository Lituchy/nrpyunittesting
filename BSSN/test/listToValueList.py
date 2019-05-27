from sympy import Integer,Symbol,symbols,simplify,Rational,Function,srepr,sin,cos,exp,log,Abs,Add,Mul,Pow,preorder_traversal,N,Float,S,var,sympify,sqrt,sign,mathematica_code
# WARNING: Importing more than the bare minimum with mpmath will result in errors on eval() below. This is because we need SymPy to evaluate that expression, not mpmath.
from mpmath import mpf,mp,log10,fabs #
import random
import logging
import re
import trustedValues as tv


# Takes in a list [lst] and returns the list with each index evaluated 
# according to parameters (seed, precision) in trustedValues 
def listToValueList(modname,lst,first_time):

    # Replace all integer fractions with the correct floating point representation:
    index = 0
    orig_lst = []
    for expr in lst:
        orig_lst.append(expr)
        string = srepr(expr)
        string2 = re.sub('Rational\(([0-9]+), ([0-9]+)\)',
                         "((Float('\\1',"+str(2*tv.precision)+"))/(Float('\\2',"+str(2*tv.precision)+")))", string)
        string3 = re.sub('Rational\((-[0-9]+), ([0-9]+)\)',
                         "((Float('\\1',"+str(2*tv.precision)+"))/(Float('\\2',"+str(2*tv.precision)+")))", string2)
        newexpr = eval(string3)
        lst[index] = newexpr
        index += 1

    # List all the free symbols in the expressions in [lst].
    #   These variables will be automatically set to random
    #   values in the range [0,1) below.
    list_free_symbols = sum(lst).free_symbols
    #print(modname,list_free_symbols)
    
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
    
    # Set the random seed according to trustedValues.seed:
    random.seed(tv.seed)

    # Next we will write a short Python code that first declares all
    #    of the free variables in the "everything" expression
    #    to random values with 30 significant digits of precision.
    #    (This is accomplished by calling random.random() to get
    #     a 16-significant-digit random number between 0 and 1,
    #     and then taking the 30-significant-digit square root
    #     of that number.)
    stringexec = """
from sympy import Integer,Symbol,symbols,simplify,Rational,Function,srepr,sin,cos,exp,log,Abs,Add,Mul,Pow,preorder_traversal,N,Float,S,var,sympify
from mpmath import *
mp.dps = """+str(tv.precision)+"\n"
    
    for var in list_free_symbols:
        stringexec += str(var)+" = symbols(\'"+str(var)+"\',Real=True)\n"
        # BE CAREFUL: You must declare all variables using mpf('string')!
        #   http://mpmath.org/doc/1.1.0/basics.html#providing-correct-input
        stringexec += str(var)+" = mpf(\'"+str(sqrt(mpf(random.random())))+"\')\n"

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

    if first_time == True:
        index = 0
        for result in evaled_lst:
            if result != 0 and fabs(result) < 100*10**(-tv.precision):
                print("Found |result| ("+str(fabs(result))+") close to zero. Checking if indeed it should be zero.")
                # Now double the precision and redo. If number drops in magnitude
                loc2xprec = {}
                stringexec = stringexec.replace("mp.dps = "+str(tv.precision),"mp.dps = "+str(2*tv.precision))
                exec(stringexec, {}, loc2xprec)
                evaled_lst2xprec = loc2xprec['lst']
                if fabs(evaled_lst2xprec[index]) < 100*10**(-2*tv.precision):
                    print("After re-evaluating with twice the digits of precision, |result| dropped to "+str(evaled_lst2xprec[index])+". Setting value to zero")
                    evaled_lst[index] = 0
            index += 1

    # Make sure that all results in evaled_lst *except* zeros are mpf type!
    for i in range(len(evaled_lst)):
        if evaled_lst[i] != 0:
            evaled_lst[i] = mpf(str(evaled_lst[i]))
        
    return evaled_lst