#!/bin/env bash

echo "python3.9 data_creation.py"
poetry run python3.9 data_creation.py 2> /tmp/mlops_lab1.log

echo "python3.9 data_preprocessing.py"
poetry run python3.9 data_preprocessing.py 2> /tmp/mlops_lab1.log

echo "python3.9 model_preparation.py"
poetry run python3.9 model_preparation.py 2> /tmp/mlops_lab1.log

echo "python3.9 model_testing.py"
poetry run python3.9 model_testing.py 2> /tmp/mlops_lab1.log

