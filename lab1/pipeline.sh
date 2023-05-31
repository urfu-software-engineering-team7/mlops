#!/bin/env bash

echo "python3.9 data_creation.py"
python3.9 data_creation.py 

echo "python3.9 data_preprocessing.py"
python3.9 data_preprocessing.py 

echo "python3.9 model_preparation.py"
python3.9 model_preparation.py 

echo "python3.9 model_testing.py"
python3.9 model_testing.py 
