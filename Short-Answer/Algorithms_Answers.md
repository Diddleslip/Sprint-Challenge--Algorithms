#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Run time for A is O(n) because it will keep going until a > n.

 
b) Run time is O(nlog n) because every time j is incremented it gets double the value so the time gets cut in half



c) Run time is O(n) because since it's recursion it needs to loop through all the subtraction/addition


## Exercise II

function calculateEggsBroken(eggs, floors):
  floorlimit = len(floors) // 2
  tempegg = eggs
  dropegg(tempegg)
  if eggs > tempegg:
    floorlimit -= 1
  else:
    return floorlimit

  # Run time for this is O(n) because worst case scenenario we start at the half-way mark and go to to the very first floor.  
