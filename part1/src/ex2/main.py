from circle import *

def parse_input():
  in_str = input("Give Radius of Circle:")
  r = float(in_str)
  if r <= 0:
    return None
  return Circle(Point(0,0), r)


def main():
  circle = parse_input()
  if circle is None:
    print "Error on input radius"
    return 
  circle.calc_latt() 

if __name__ == "__main__":
  main()