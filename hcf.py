import math

def getHCF(x, y):
  x = int(input())
  y = int(input())
  q = math.floor(x / y)
  r = x % y
  while (r != 0):
    x = q
    r = y
    if (r == 0):
      print(x)
      break
    
