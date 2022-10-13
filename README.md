# Optimal NFL Conference Assignment 

This code determines the *optimal* conference assignment for the AFC and NFC separately based on their lattitude and longitude. It minimizes the following cost: for teams in the North, cost is negative lattitude, teams in the East, cost is negative longitude, for teams in the south, cost is lattitude, and for teams in the west, cost is longitude. 

The assignment problem is sovled with google's OR-tools. 

## Installation
Recommend creating a fresh conda environment. 
```
conda activate orTools_env
conda install python 
python -m pip install --upgrade --user ortools
pip install geopy
```

## Files 
- ```google_example.py``` provides a simple example using OR-tools to solve an assignment problem from https://developers.google.com/optimization/assignment/assignment_example
- ```get_lat_long.py``` uses ```geopy``` package to get lat and long data for each city
- ```lat_longNFC.pickle``` and ```lat_longAFC.pickle``` cached lat/long data so you don't need to run ```get_lat_long.py``` again
- ```main.py``` run this to solve the assignment problem 
