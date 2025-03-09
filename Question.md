A city Bus is a Ring Route Bus which runs in a circular fashion.That is ,Bus once starts at the 
source Bus Stop ,halts at each Bus stop in its Route and at the end it reaches the source
Bus Stop again.

If there are n number of stops and if the bus starts at Bus stop 1, then after nth Bus Stop the 
next stop in the Route will be Bus Stop number 1 always .

If there are n stops ,there will be n paths .One path connects two stops. Distances (in meters) 
for all paths in Ring Route is given in array Path[] as given below

Path = [800,600,750,900,1400,1200,1100,1500]

Question : 
Fare is determined based on the distance covered from source to destination stop as Distance 
between Input Source and Destination Stops can be measured by looking at values in array Path[] 
and fare can be calculated as per following criteria: 

If d =1000 meters, then fare=5 INR 

NOTE : 

When calculating fare for others, the calculated fare containing any fraction value should be 
ceiled. 

For example, for distance 900n when fare initially calculated is 4.5 which must be ceiled to 5.

Path is circular in function. Value at each index indicates distance till current stop from the 
previous one. And each index position can be mapped with values at same index in 
Bus Stops [] array, which is a string array holding abbreviation of names for all stops as-

THANERAILWAYSTN = TH 
NITINCOMPANYJUNCTION = NI 
GAONDEVI = GA 
CADBURRYJUNCTION = CA 
ICEFACTROY = IC 
LUISWADI = LU 
HARINIWASCIRCLE = HA 
TEENHATHΝΑΚΑ = ΤΕ

Given, n=8, where n is number of total Bus Stops. 

BusStops = ["TH","GA","IC","HA","TE","LU","NI","CA"] 

Write a code with function getFare(String Source, String Destination) 
which take Input as source and destination stops(in the format 
containing first two characters of the Name of the Bus Stop) and calculate and 
return travel fare.

```python

import math

def getFare(Source: str, Destination: str) -> int:
    BusStops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]
    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    
    # Find indices of source and destination
    try:
        src_index = BusStops.index(Source)
        dest_index = BusStops.index(Destination)
    except ValueError:
        return -1  # Invalid stop name
    
    # Calculate distance in the circular route
    if src_index <= dest_index:
        distance = sum(Path[src_index:dest_index])
    else:
        distance = sum(Path[src_index:]) + sum(Path[:dest_index])
    
    # Calculate fare
    fare = math.ceil(distance / 1000 * 5)
    return fare

# Example Usage
print(getFare("TH", "LU"))  # Example call
