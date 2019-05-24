from mpmath import *
import random
import logging


## Constants to be used throughout test files
global precision, seed

precision = 30
mp.dps = precision
seed = 1234

## Common functions

def calcError(mod,result_list,trusted_list):
    print
    for res, val in zip(result_list, trusted_list):
        logging.debug('\nResult, value: \n\t' + str(res) + '\n\t'+ str(val)+'\n')
        if val == 0:
            log10_relative_error = log10(fabs(res))
        else:
            log10_relative_error = log10(fabs( (val - res ) / val ) )
        good = (log10_relative_error < (precision / -2))
        if not good:
            logging.error('\n\n Failed with ' + str(mod) + '\n\n')
            return False
    return True
    


# Prints module, result list, and current trusted list to console window
def firstTimePrint(mod,result_list,trusted_list):
    print('\nModule: ')
    print(mod)
    print('\nResult list:')
    print(result_list)
    print('\nTrusted list:')
    print(trusted_list)
    return

# Takes in a list [lst] and returns the list with each index evaluated 
#     according to parameters (seed, precision) in trustedValues 
def listToValueList(lst):
    
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
    

    
    # Set the random seed according to trustedValues.seed:
    random.seed(seed)

    # Next we will write a short Python code that first declares all
    #    of the free variables in the "everything" expression
    #    to random values with 30 significant digits of precision.
    #    (This is accomplished by calling random.random() to get
    #     a 16-significant-digit random number between 0 and 1,
    #     and then taking the 30-significant-digit square root
    #     of that number.)
    stringexec = "from sympy import *\n" + "from mpmath import *\n" + "mp.dps = " + str(precision) + "\n"
    
    for var in list_free_symbols:
        stringexec += str(var)+" = symbols(\'"+str(var)+"\')\n"
        # BE CAREFUL: You must declare all variables using mpf('string')!
        #   http://mpmath.org/doc/1.1.0/basics.html#providing-correct-input
        stringexec += str(var)+" = mpf(\'"+str(sqrt(mpf(random.random())))+"\')\n"

    # Then it creates the code that evaluates the result
    #    to 30 significant digits.
    stringexec += "lst = " + str(lst)
    
    # https://stackoverflow.com/questions/38817962/python-3-need-from-exec-to-return-values
    # Finally we execute stringexec to a local namespace "loc", and store the
    #    result of the evaluated "everything" expression to "result".
    loc = {}
    exec(stringexec, {}, loc)
    return loc['lst']

## Trusted Values:

# These values come from running the tests for the first time on a trusted verison of nrpy.
# Since the current version is known to be correct, these values should be consistent with any
# subsequent versions of the software. If the tests stop working, something was likely broken.

# Trusted values for BSSN ADM
global BSSN_cart_BL_ADM, BSSN_sph_SKS_ADM, BSSN_sph_ST_ADM, BSSN_sph_UBH_ADM


BSSN_cart_BL_ADM = [mpf('0.122483331574515176153136610247666'), 0, 0, mpf('66.6570391079152319165851690989606'), 0, 0, 0, 0, 0, 0, 0, 0, 0, mpf('66.6570391079152319165851690989606'), 0, 0, 0, 0, 0, 0, 0, 0, 0, mpf('66.6570391079152319165851690989606'), 0]


BSSN_sph_SKS_ADM = [mpf('0.611873766692798472488570416618186'), mpf('0.625610493633166822638772330972943'), 0, mpf('2.67101503379259532016438346708211'), mpf('-1.3871883522683154071806190217075'), 0, mpf('0.171664018858514818215855728819767'), mpf('-1.20517572307269882101503709735398'), mpf('0.455406940612776090115394191050947'), 0, 0, 0, mpf('0.171664018858514818215855728819767'), mpf('1.22487699767344797967358950175897'), mpf('1.06437469733833992932303275045972'), 0, mpf('-0.0774556883566536581224962371138576'), 0, 0, mpf('-1.20517572307269882101503709735398'), mpf('0.455406940612776090115394191050947'), 0, mpf('-0.0774556883566536581224962371138576'), mpf('1.37627131033453091934058579009585'), mpf('0.59485248459953340823202605867648')]



BSSN_sph_ST_ADM = [mpf('0.403092176323945252455401083264855'), mpf('0.240608873710370682916226625464511'), 0, mpf('6.15447854588632421730150623325538'), mpf('-2.23056721663690142814440046331094'), 0, 0, 0, 0, 0, 0, 0, 0, mpf('2.71247932609742473472094943837468'), mpf('0.983083687023713543948423277992989'), 0, 0, 0, 0, 0, 0, 0, 0, mpf('0.0202697649478352484117814815031462'), mpf('0.00734636945185188428754902788373153')]


BSSN_sph_UBH_ADM = [1, 0, 0, mpf('1395.79778503827727330438811733733'), 0, 0, 0, 0, mpf('4.81517781103762810906853631572986'), 0, 0, 0, 0, mpf('9.61434498113641434805550645852601'), 0, 0, mpf('0.0035315484611782893268295136320798'), 0, 0, 0, mpf('4.81517781103762810906853631572986'), 0, mpf('0.0035315484611782893268295136320798'), mpf('6.70941611174433767041669495976436'), 0]

# Trusted values for BSSN ID
global BSSN_cart_BL_ID, BSSN_sph_SKS_ID, BSSN_sph_ST_ID, BSSN_sph_UBH_ID

BSSN_cart_BL_ID = [mpf('0.00000152945193754914710102797581545575'), mpf('0.10733861131411676664350139844293'), 0, mpf('-1265651143.91068964151022994739147'), 0, 0, mpf('74.9869010504432794736061336923654'), 0, mpf('-3.15544362088404722164691426113114e-30'), 0, 0, 0, mpf('-983861841.67201246515566452541449'), 0, 0, mpf('74.9869010504432794736061336923527'), 0, 0, 0, mpf('-1.40483805438325262556020170609561e-23'), 0, 0, mpf('74.9869010504432794736061336923654'), 0]

BSSN_sph_SKS_ID = [mpf('0.207086860796909267930015101794759'), mpf('0.611873766692798472488570416618186'), mpf('0.749645216318693661248829716552832'), mpf('-8.50190543299665899499977111718708'), mpf('0.625610493633166822638772330972943'), 0, mpf('1.54935192205356147315597570906562'), mpf('-1.72253947936521621293110146059516'), 0, mpf('0.171664018858514818215855728819791'), mpf('-1.4618645924034047842700509229606'), mpf('0.917696761284986595107747687088108'), mpf('-6.16212271223487296034208633277397'), 0, 0, mpf('0.283331989997330860016181144884251'), mpf('0.794488784748600832389890610705952'), 0, mpf('-0.098436606099007129277967101068217'), mpf('0.509787083317040113656220567402534'), 0, 0, mpf('1.12160310825131108428924137074257'), mpf('0.386850190774130044881220547059668')]

BSSN_sph_ST_ID = [0.403092176323945252455401083265, mpf('0.403092176323945252455401083264855'), mpf('0.362429928060732398869599212975653'), 0, mpf('0.240608873710370682916226625464511'), 0, 0, mpf('-0.483239904080976531826132283967554'), 0, 0, 0, 0, mpf('0.0'), 0, 0, 0, mpf('0.241619952040488265913066141983777'), 0, 0, 0, 0, 0, 0, mpf('0.241619952040488265913066141983777')]

BSSN_sph_UBH_ID = [mpf('0.000000000415033854876444477286285893579512'), 1, 0, mpf('-95747350686634955.2990447037942658'), 0, 0, mpf('1394.79778503827727330438811733733'), 0, 0, 0, 0, mpf('68.1774297079879249492943239915913'), mpf('-38201931430976591.6020627256016624'), 0, 0, mpf('1282.37227619509095380577148705319'), 0, 0, mpf('0.57771007481884038882051828035855'), 0, 0, 0, mpf('1344.05894729887689495988360659524'), 0]

# Trusted values for BSSN RHS
global BSSN_rhs_scalars, BSSN_rhs_vectors, BSSN_rhs_tensors, BSSN_gaugerhs_scalars, BSSN_gaugerhs_vectors

BSSN_rhs_scalars = [mpf('1.17088725081123717976036013389338'), mpf('2.4203168731041778276785631821572')]
BSSN_gaugerhs_scalars = [mpf('-0.642547930155001380559044161367303')]

BSSN_rhs_vectors = [mpf('4.5416685128144842973532181122077'), mpf('-26.292021081498246002785894358253'), mpf('-3.91565108795835425950242828436205')]
BSSN_gaugerhs_vectors = [mpf('19.1253301349717903059126760275783'), mpf('6.73377751498821779817923223971379'), mpf('-14.3252852575698761674049866366367'), mpf('-0.416046528730366515540680736079711'), mpf('111.380322321824694940721028671132'), mpf('13.097737197938302234221188787723')]

BSSN_rhs_tensors = [mpf('-0.0263260284069148577059637000538504'), mpf('0.975839919679223756941181380326283'), mpf('1.38130334638529214604701755241765'), mpf('-0.133052195096384779869483191297963'), mpf('2.74699696368025413060359760185334'), mpf('3.37462047768649834195688176828246'), mpf('0.181924456363985578660086274768599'), mpf('-0.390726294642051073527657924515473'), mpf('2.97745157106802559535679276411241'), mpf('2.64061873661409646885708292890556'), mpf('3.0897580173644791657503704144862'), mpf('6.99877414802463331695008858530444')]





# Add ReadMe.md