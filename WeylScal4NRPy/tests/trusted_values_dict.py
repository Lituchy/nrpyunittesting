from mpmath import mpf,mp

# Dictionary of trusted values to be used throughout files.
# Standard precision and seed values are precision: 30, seed: 1234.
# Note that changing these may drastically change the calculated values.
trusted_values_dict = {
    "precision": 30,
    "seed": 1234
}

mp.dps = trusted_values_dict["precision"]

# Generated on: 2019-06-19 15:58:07.085418
trusted_values_dict['ScalarWaveCurvilinear_RHSsGlobals'] = {'uu_rhs': mpf('0.763038382428399942157724162730687'), 'vv_rhs': mpf('29.8343379048485150514807183285427')}