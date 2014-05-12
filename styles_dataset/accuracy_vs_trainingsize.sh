#!/bin/bash
for i in {12..19}
do
  echo $i | cat > train_size
  echo $((20-i)) | cat > test_size
  mkdir ./training
  mkdir ./test
  python split_and_rename.py
  python classifier.py
  python calculate_accuracy.py
  rm -rf results
  rm -rf svm_data.dat
  rm -rf train*
  rm -rf test*
  rm -rf train_size
  rm -rf test_size
done
