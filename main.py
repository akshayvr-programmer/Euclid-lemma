

import math

def euclid(x, y):
  
  x = int(input("Please Enter the first number"))
  y = int(input("Please enter the second  number"))
  q = math.floor(x / y)
  r = x % y
  
  print(str(x)  + " " + "=" + " " + str(y) + "*" + str(q) + " " + str(r))
  
  
  
  
euclid(256, 64) 
  
