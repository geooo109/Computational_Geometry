class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("Point(%s,%s)"%(self.x, self.y)) 
    return

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

  def get_point(self):
    return (self.x, self.y)