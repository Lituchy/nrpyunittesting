#!/bin/bash

failed_tests_file=UnitTesting/failed_tests.txt
contents=$(<$failed_tests_file)

IFS=': ' read -ra ADDR <<< "$contents"

for i in "${ADDR[@]}"; do
  echo "$i"
done

#while read line; do
#    split=$(echo $line | tr ":" "\n")
#    #echo "$split"
#    for part in $split
#    do
#      echo "$part"
#    done
#    #echo "$line"
#done < "$failed_tests_file"