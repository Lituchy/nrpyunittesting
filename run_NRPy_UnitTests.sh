#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`

PYTHONEXEC=python
if [ -x "$(command -v pypy)" ]; then
    # pypy is NOT installed
    PYTHONEXEC=pypy
fi

echo "########################################"
echo Using $PYTHONEXEC as Python interpreter.
echo $PYTHONEXEC version info:
$PYTHONEXEC --version
echo "########################################"

$PYTHONEXEC UnitTesting/NRPyUnitTests_Function_Tests.py &&
$PYTHONEXEC BSSN/tests/NRPyUnitTests_BSSN_Globals_Tests.py
