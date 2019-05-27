#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`

python BSSN/test/BSSN_exact_ID_tests.py #&&
# pypy BSSN/test/BSSN_Psi4_test.py &&
# pypy BSSN/test/BSSN_RHS_test.py 

