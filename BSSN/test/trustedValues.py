from mpmath import *

global precision, seed

precision = 30
mp.dps = precision
seed = 1234

global BSSN_cart_BL_ADM, BSSN_sph_SKS_ADM, BSSN_sph_SKS_ADM, BSSN_sph_UBH_ADM

BSSN_cart_BL_ADM = [mpf('0.122483331574515184532072595714915'), 0, 0, mpf('66.6570391079152227967309573244502'), 0, 0, 0, 0, 0, 0, 0, 0, 0, mpf('66.6570391079152227967309573244502'), 0, 0, 0, 2, 0, 0, 0, 0, 0, mpf('66.6570391079152227967309573244502'), 0]

BSSN_sph_SKS_ADM = [mpf('inf')]
BSSN_sph_SKS_ADM = [mpf('inf')]
BSSN_sph_UBH_ADM = [mpf('inf')]

global BSSN_cart_BL_ID, BSSN_sph_SKS_ID, BSSN_sph_SKS_ID, BSSN_sph_UBH_ID

BSSN_cart_BL_ID = [mpf('inf')]

BSSN_sph_SKS_ID = [mpf('inf')]
BSSN_sph_SKS_ID = [mpf('inf')]
BSSN_sph_UBH_ID = [mpf('inf')]

# Add ReadMe.md