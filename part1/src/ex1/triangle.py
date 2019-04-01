from point import *
'''
 Class to represent a triangle
'''
class Triangle:
  def __init__(self, point1, point2, point3):
    self.point1 = point1
    self.point2 = point2
    self.point3 = point3

  def print_triangle(self):
    print "\n**Points of Triangle** /_\\ are:"
    self.point1.print_point()
    self.point2.print_point()
    self.point3.print_point() 
    return 

  def get_all_points(self):
    return (self.point1, self.point2, self.point3)