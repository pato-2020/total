# Name: total App

## Introduction:

This projects aims to create a simple app in Flask using Python 3. When queries it will return the sum of list of numbers in a range. For simplicity purpose the range is hardcoded. The url to access is http://localhost:5000/total

## Prerequisites:

1. Python >= 3.6
2. export PYTHONPATH=${PYTHONPATH}:<projectrootdir>
3. create virtual environment python -m venv  .venv
4. Activate the venv : source .venv/bin/activate
5. Install the Python modules : pip install -r requirements.txt
  
## Run:
1. Go to {ProjectDir}/src 
2. python app.py
3. Access http://localhost:5000/total

## Testing:
1. Run python -m pytest tests
