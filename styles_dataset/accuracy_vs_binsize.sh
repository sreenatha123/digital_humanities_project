#!/bin/bash
for i in {2..64}
do
  echo $i | cat > input
  mkdir ./training
  mkdir ./test
  python split_and_rename.py
  python classifier.py < input
  python calculate_accuracy.py
  rm -rf results
  rm -rf svm_data.dat
  rm -rf train*
  rm -rf test*
done
