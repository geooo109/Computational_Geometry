import math as mt
from point import *

class Circle:
  def __init__(self, cent, r):
    self.cent = cent
    self.r = r

  def calc_latt(self):
    count = 4 
    for val in range(1, int(self.r)):
      xs = self.r*self.r - val*val
      xl = int(mt.sqrt(xs))
      if (xl**2 == xs): 
        count += 4 
    
    print("Total Lattices :" + str(count)) 
