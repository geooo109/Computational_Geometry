'''
 Class to represent point
'''
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

    def can_construct_triangle(self, point2, point3):
        return abs(((point2.get_x()-self.x)*(point3.get_y()-self.y))
                 -((point2.get_y()-self.y)*(point3.get_x()-self.x))) != 0
