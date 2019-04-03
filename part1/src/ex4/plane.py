from point import *
class Plane:
    def __init__(self, points):
        self.points = points

    def get_points(self,points):
        return self.points

    def print_plane(self):
        print ("***Points of Plane*** are:")
        if self.points == []:
            print("Plane has no points to show")
        for point in self.points:
            point.print_point()
