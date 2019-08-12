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

# You can change this to any file you'd like the output to be directed to
failed_tests_file=UnitTesting/failed_tests.txt

:> $failed_tests_file
printf "Failures:\n\n" > $failed_tests_file

add_test () {
  $PYTHONEXEC $1 $PYTHONEXEC $failed_tests_file
}

#$PYTHONEXEC UnitTesting/Test_UnitTesting/test_functions.py &&
add_test UnitTesting/Test_UnitTesting/test_module.py

#add_test BSSN/tests/test_BSSN.py
#add_test FishboneMoncriefID/tests/test_FishboneMoncriefID.py
add_test GiRaFFE_HO/tests/test_GiRaFFE_HO.py
#add_test GiRaFFEfood_HO/tests/test_GiRaFFEfood_HO.py
#add_test Maxwell/tests/test_Maxwell.py
#add_test ScalarWave/tests/test_ScalarWave.py
#add_test ScalarWaveCurvilinear/tests/test_ScalarWaveCurvilinear.py
#add_test tests/test_reference_metric.py
#add_test TOV/tests/test_TOV.py
add_test u0_smallb_Poynting__Cartesian/tests/test_u0_smallb_Poynting__Cartesian.py
#add_test WeylScal4NRPy/tests/test_WeylScal4NRPy.py

file=$(<$failed_tests_file)

if [ "$file" == $"Failures:" ]
then
  printf "All tests passed!\n\n"
  exit 0
else
  printf "Tests failed!\n\n"
  printf "$file \n\n"
  #printf "Re-running failed tests with logging_level=DEBUG:\n\n"
  #add_test UnitTesting/failed_tests_rerun.py
  exit 1
fi

# TODO: Change 'successes' to completions
