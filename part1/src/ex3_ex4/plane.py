from point import *
import matplotlib.pyplot as plt
#define
COLINEAR = 0
CCW = 1
CW = -1

class Plane:
    def __init__(self, points):
        self.points = points

    def __getitem__(self, key):
        return self.points[key]

    def get_points(self,points):
        return self.points

    def print_plane(self):
        print ("***Points of Plane*** are:")
        if self.points == []:
            print("Plane has no points to show")
        for point in self.points:
            point.print_point()

    #this functions check if 2 points share shame x
    def check_points(self):
        curr = 0
        l_size = len(self.points)
        while True:
            if curr >= l_size:
                break
            for i in range(curr+1,l_size):
                if self.points[i].get_x() == self.points[curr].get_x():
                    print("Poss are (%s,%s)"%(i,curr))
                    return True
            curr += 1
        return False

    #if we start from left to right
    def ort_min_max(self, pt1 , pt2, r):
        v = ((pt2.get_y()-pt1.get_y())*(r.get_x()-pt2.get_x())
            -(pt2.get_x()-pt1.get_x())*(r.get_y()-pt2.get_y()))
        if v == 0:
            return COLINEAR
        elif v > 0:
            return CW
        else:
            return CCW

    #if we start from right to left
    def ort_max_min(self, pt1 , pt2, r):
        v = ((pt2.get_x()-pt1.get_x())*(r.get_y()-pt2.get_y())
            -(pt2.get_y()-pt1.get_y())*(r.get_x()-pt2.get_x()))
        if v == 0:
            return COLINEAR
        elif v < 0:
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
        hx.append(hull_points[0].get_x())
        hy = [pt.get_y() for pt in hull_points]
        hy.append(hull_points[0].get_y())
        plt.plot(hx, hy, "r-")
        plt.title('Convex Hull Points (red color)')
        #plt.ion()
        plt.show()
        #plt.draw()
        #plt.pause(100)

    def find_left_most_pt(self):
        left_pt = 0
        for i in range(1, len(self.points)):
            if self.points[i].get_x() < self.points[left_pt].get_x():
                left_pt = i
        return left_pt

    def sort_function(self,point):
        return point.get_x()

    def incremental_convex_hull(self):
        lower_hull = []
        upper_hull = []

        if len(self.points) <= 1:
            return self.points

        #sorting list based on x coord {max -> min}
        self.points = sorted(self.points,key = self.sort_function, reverse = True)
        N = len(self.points)

        # culculating lower hull #
        for idx in range(N):
            while True:
                curr_len = len(lower_hull)
                if (curr_len >= 2):
                    ort = self.ort_max_min(lower_hull[-2], lower_hull[-1], self.points[idx])
                    if ort == CW:
                        lower_hull.pop()
                    elif ort == CCW:
                        break
                    else:
                        print ("COLINEAR points in the lower_hull")
                else:
                    break
            lower_hull.append(self.points[idx])

        # culculating upper hull #
        self.points.reverse()
        for idx in range(N):
            while True:
                curr_len = len(upper_hull)
                if (curr_len >= 2):
                    ort = self.ort_max_min(upper_hull[-2], upper_hull[-1], self.points[idx])
                    if ort == CW:
                        upper_hull.pop()
                    elif ort == CCW:
                        break
                    else:
                        print ("COLINEAR points in the lower_hull")
                else:
                    break
            upper_hull.append(self.points[idx])

        hull = lower_hull + upper_hull
        self.display_hull(hull)
        return


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
                ort = self.ort_min_max(self.points[cr_pt], self.points[i], self.points[curr_pt])
                if ort == CCW:
                    curr_pt = i
            cr_pt = curr_pt
            if cr_pt == left_pt:
                break
        self.display_hull(hull_points)
        return
