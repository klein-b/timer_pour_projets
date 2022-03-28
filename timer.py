"""petit code pour chronometrer une application"""

import time

def timer():
  list1=[]
  """insert your code here"""
  start=time.perf_counter()
  for i in range(1000000):
    list1.append(i**2)
  end=time.perf_counter()
  return f'Code Run time is {end - start:0.2f} secondes'

if __name__=="__main__":
  print (timer())
  
