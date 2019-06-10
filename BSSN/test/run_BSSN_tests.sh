#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`

pypy BSSN/test/UnitTesting_Functions_Tests.py &&
pypy BSSN/test/BSSN_Globals_Tests.py