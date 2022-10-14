# Optimal NFL Division Assignment 

This code determines the *optimal* division assignment for the AFC and NFC separately based on the team's lattitude and longitude. It minimizes the following cost: for teams in the North, cost is negative lattitude, teams in the East, cost is negative longitude, for teams in the south, cost is lattitude, and for teams in the west, cost is longitude. 

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
- ```getCurrCost.py``` computes cost of current assignments used by NFL
- ```main.py``` run this to solve the assignment problem 

## Results 

The below lists the optimal division assignments. Teams in bold are in a different division from the current assignment. The division of the current assignment is in brackets. 

### AFC solutions:

Optimal cost = -172.90477270000002

Current cost = -153.5169713


- North:
    -	**Indianapolis (S)**
    -	**Buffalo (E)**
    -	Cincinnati
    -	Cleveland
- East:
    -	New York
    -	**Baltimore (N)**
    - 	**Pittsburgh (N)** 
    -	Boston
- South:
    -    **Miami (E)**
    -	Tennessee
    -	Jacksonville
    -	Houston
- West:
    -	Denver
    -	LA
    -	Kansas City
    -	Las Vegas

### NFC solutions:

Optimal cost = -217.5248536

Current cost: -199.12014370000003

- North:
    -	Detroit
    -	Green Bay WI
    -	minneapolis
    -	Chicago
- East:
    -	New York
    -	Philadelphia
    -	Washington DC
    -	**Charlotte NC (S)**
- South:
    -	**Dallas (E)**
    -	Tampa Bay
    -	Atlanta
    -	New Orleans
- West:
    -	San Francisco
    -	Seattle
    -	LA
    -	Phoenix

## Discussion
The NFC optimal assignment is only one swap away from the current assignment. The Panthers (currently in the south) need to swap with the Cowboys (currently in east). This makes sense and I noticed this before writing any code (why is Dallas in the east??)

The AFC is quite far off optimal. To get to optimal, Buffalo (currently East) and Baltimore (currently North) can swap, and Miami (currently east), Pittsburgh (currently north), and Indianapolis (currently south) can form a chain and ``shuffle left" - Pittsburgh moves to East, Indianapolis to North, and Miami moves to South.
