#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Run time for A is O(n) because it will keep going until a > n.

 
b) Run time is O(n^2) because the while loop is insde and it will keep going until j > n



c) Run time is O(1) because it's doing simple addition/subtraction. 


## Exercise II

function calculateEggsBroken(eggs, floors):
  floorlimit = len(floors) // 2
  tempegg = eggs
  dropegg(tempegg)
  if eggs > tempegg:
    floorlimit -= 1
  else:
    return floorlimit

  # Run time for this is O(nlogn) because worst case scenenario we start at the half-way mark and go to to the very first floor.  
