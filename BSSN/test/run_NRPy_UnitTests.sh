#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`

pypy BSSN/test/NRPyUnitTests_Function_Tests.py &&
pypy BSSN/test/NRPyUnitTests_Globals_Tests.py