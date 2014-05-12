
mkdir ./training
mkdir ./test
python split_and_rename.py
python classifier.py 
python calculate_accuracy.py
