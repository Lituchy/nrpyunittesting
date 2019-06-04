#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`

coverage run BSSN/test/BSSN_Globals_Tests.py #&&
# pypy BSSN/test/BSSN_Constraints_Test.py
# coverage run BSSN/test/BSSN_ADM_Test.py # &&
# coverage run BSSN/test/BSSN_Psi4_test.py #&&
# pypy BSSN/test/BSSN_RHS_test.py #&&
# pypy BSSN/test/BSSN_Quantities_Test.py
# pypy BSSN/test/BSSN_T4UUmunu_vars_Test.py