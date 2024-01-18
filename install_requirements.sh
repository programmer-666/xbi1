#!/bin/sh

# run after creating virtualenv

pip install -r requirements.txt &
pip install -r requirements_dev.txt &
