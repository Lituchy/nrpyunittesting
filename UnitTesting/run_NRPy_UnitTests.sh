#!/bin/bash

export PYTHONPATH=`pwd`:`pwd`/UnitTesting

if [ -z "$1" ]
then
    echo "ERROR: Was expecting parameter."
    echo " Usage: ./run_NRPy_UnitTests.sh [Python interpreter; e.g., python]"
    exit
fi

PYTHONEXEC=$1

echo "########################################"
echo $PYTHONPATH
echo Using $PYTHONEXEC as Python interpreter.
echo $PYTHONEXEC version info:
$PYTHONEXEC --version
echo "########################################"

#$PYTHONEXEC UnitTesting/test_functions.py #&&

$PYTHONEXEC BSSN/tests/test_BSSN.py &&
$PYTHONEXEC FishboneMoncriefID/tests/test_FishboneMoncriefID.py &&
# TODO: argc argv in python -- might give access to PYTHONEXEC. Otherwise, pass it in as an additional argument.
$PYTHONEXEC GiRaFFE_HO/tests/test_GiRaFFE_HO.py &&
$PYTHONEXEC GiRaFFEfood_HO/tests/test_GiRaFFEfood_HO.py &&
$PYTHONEXEC Maxwell/tests/test_Maxwell.py && #TODO: MaxwellCartesian_ID not working
$PYTHONEXEC ScalarWave/tests/test_ScalarWave.py &&
$PYTHONEXEC ScalarWaveCurvilinear/tests/test_ScalarWaveCurvilinear.py &&
$PYTHONEXEC TOV/tests/test_TOV.py &&
$PYTHONEXEC u0_smallb_Poynting__Cartesian/tests/test_u0_smallb_Poynting__Cartesian.py &&
$PYTHONEXEC WeylScal4NRPy/tests/test_WeylScal4NRPy.py &&
$PYTHONEXEC tests/test_reference_metric.py
