#!/bin/env bash

echo "python3.10 data_creation.py"
python3.10 data_creation.py 2> /tmp/mlops_lab1.log

echo "python3.10 data_preprocessing.py"
python3.10 data_preprocessing.py 2> /tmp/mlops_lab1.log

echo "python3.10 model_preparation.py"
python3.10 model_preparation.py 2> /tmp/mlops_lab1.log

echo "python3.10 model_testing.py"
python3.10 model_testing.py 2> /tmp/mlops_lab1.log

