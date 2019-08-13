#!/bin/bash

while IFS=': ' read -r col1 col2
do
    if [ "$col1" != "Failures" ] && [ "$col1" != "" ]
    then
      add_test "$col1" "DEBUG" "$col2"
      echo "col1: $col1"
      echo "col2: $col2"
    fi
done <UnitTesting/failed_tests.txt

