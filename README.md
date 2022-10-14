# Optimal NFL Division Assignment 

This code determines the *optimal* division assignment for the AFC and NFC separately based on their lattitude and longitude. It minimizes the following cost: for teams in the North, cost is negative lattitude, teams in the East, cost is negative longitude, for teams in the south, cost is lattitude, and for teams in the west, cost is longitude. 

The assignment problem is sovled with google's OR-tools. 

## Installation
Recommend creating a fresh conda environment. Something.
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

## Results 
AFC solutions:
Total cost = -172.90477270000002

- North:
    -	Indianapolis
    -	Buffalo
    -	Cincinnati
    -	Cleveland
- East:
    -	New York
    -	Baltimore
    - 	Pittsburgh
    -	Boston
- South:
    -    Miami
    -	Tennessee
    -	Jacksonville
    -	Houston
- West:
    -	Denver
    -	LA
    -	Kansas City
    -	Las Vegas

NFC solutions:
Total cost = -217.5248536

- North:
    -	Detroit
    -	Green Bay WI
    -	minneapolis
    -	Chicago
- East:
    -	New York
    -	Philadelphia
    -	Washington DC
    -	Charlotte NC
- South:
    -	Dallas
    -	Tampa Bay
    -	Atlanta
    -	New Orleans
- West:
    -	San Francisco
    -	Seattle
    -	LA
    -	Phoenix

## To Do
- Highlight which Cities have been moved
- Implement function to compute the cost of an arbitrary assignment so we can compare cost of current assignment
