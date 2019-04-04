from point import *
import matplotlib.pyplot as plt

#define
COLINEAR = 0
CCW = 1
CW = -1

def sort_function(point):
        return point.get_x()

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

    def ort(self, pt1 , pt2, r):
        v = ((pt2.get_y()-pt1.get_y())*(r.get_x()-pt2.get_x())
            -(pt2.get_x()-pt1.get_x())*(r.get_y()-pt2.get_y()))
        if v == 0:
            return COLINEAR
        elif v > 0:
            return CW
        else:
            return CCW

    def display_hull(self, hull_points):
        if hull_points == []:
            print("No points on the hull list to display")
            return
        # all points of dataset
        x = [pt.get_x() for pt in self.points]
        y = [pt.get_y() for pt in self.points]
        plt.scatter(x, y)

        # hull points
        hx = [pt.get_x() for pt in hull_points]
        hy = [pt.get_y() for pt in hull_points]
        plt.plot(hx, hy, "r-")
        plt.title('Convex Hull Points (red color)')
        plt.ion()
        plt.show()
        plt.draw()
        plt.pause(1)

    def find_left_most_pt(self):
        left_pt = 0
        for i in range(1, len(self.points)):
            if self.points[i].get_x() < self.points[left_pt].get_x():
                left_pt = i
        return left_pt

    def gift_wrap_convex_hull(self):
        hull_points = []
        #find leftmost point
        left_pt = self.find_left_most_pt()
        total_points = len(self.points)
        cr_pt = left_pt
        while True:
            hull_points.append(self.points[cr_pt])
            curr_pt = (cr_pt+1)%total_points
            #check for orientation of all other Points
            for i in range(0, total_points):
                if self.ort(self.points[cr_pt], self.points[i], self.points[curr_pt]) == CCW:
                    curr_pt = i
            cr_pt = curr_pt
            if cr_pt == left_pt:
                break
        self.display_hull(hull_points)
        return

    def incremental_convex_hull(self):
        sorted(self.points,key = sort_function)
        self.print_plane()