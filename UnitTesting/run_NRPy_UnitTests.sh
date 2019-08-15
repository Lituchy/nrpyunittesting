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

failed_tests_file=UnitTesting/failed_tests.txt

:> $failed_tests_file
printf "Failures:\n\n" > $failed_tests_file

# Usage: add_test [path to test file]
add_test () {
  $PYTHONEXEC $1 $PYTHONEXEC $failed_tests_file $2 $3
}

# Change boolean to true/false depending on if you want the tests that fail to automatically re-run with
# logging_level='DEBUG'
rerun_if_fail=true

add_test UnitTesting/Test_UnitTesting/test_module.py
#add_test BSSN/tests/test_BSSN.py
#add_test FishboneMoncriefID/tests/test_FishboneMoncriefID.py
#add_test GiRaFFE_HO/tests/test_GiRaFFE_HO.py
#add_test GiRaFFEfood_HO/tests/test_GiRaFFEfood_HO.py
#add_test Maxwell/tests/test_Maxwell.py
#add_test ScalarWave/tests/test_ScalarWave.py
#add_test ScalarWaveCurvilinear/tests/test_ScalarWaveCurvilinear.py
#add_test tests/test_reference_metric.py
#add_test TOV/tests/test_TOV.py
#add_test u0_smallb_Poynting__Cartesian/tests/test_u0_smallb_Poynting__Cartesian.py
#add_test WeylScal4NRPy/tests/test_WeylScal4NRPy.py

#$PYTHONEXEC UnitTesting/Test_UnitTesting/test_functions.py

# TODO: add your tests here


contents=$(<$failed_tests_file)

if [ "$contents" == $"Failures:" ]
then
  printf "All tests passed!\n\n"
  exit 0
else
  printf "Tests failed!\n\n"
  printf "$contents \n\n"
  printf '%s\n' '----------------------------------------------------------------------'

  if $rerun_if_fail
  then
    printf "Re-running failed tests with logging_level=DEBUG:\n\n"
    while IFS=': ' read -r col1 col2
    do
      if [ "$col1" != "Failures" ] && [ "$col1" != "" ]
      then
        add_test "$col1" "DEBUG" "$col2"
      fi
    done <UnitTesting/failed_tests.txt

    printf "Completed by re-running following tests with logging_level=DEBUG\n\n"
    printf "$contents \n\n"
    printf '%s\n' '----------------------------------------------------------------------'
  fi

  exit 1
fi
