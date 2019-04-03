from point import *
#define
COLINEAR = 0
CCW = 1
CW = -1
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

    def ort(pt1,pt2,r):
        v = ((pt2.get_y()-pt1.get_y())*(r.get_x()-pt2.get_x())
            -(pt2.get_x()-pt1.get_x())*(r.get_y()-pt2.get_y()))
        if v == 0:
            return COLINEAR
        elif val > 0:
            return CW
        else:
            return CCW

    '''
    jarvis(S):
      // S is the set of points
      pointOnHull = leftmost point in S // which is guaranteed to be part of the CH(S)
      i = 0
      repeat
        P[i] = pointOnHull
        endpoint = S[0]      // initial endpoint for a candidate edge on the hull
        for j from 1 to |S|
          if (endpoint == pointOnHull) or (S[j] is on left of line from P[i] to endpoint)
              endpoint = S[j]   // found greater left turn, update endpoint
        i = i+1
        pointOnHull = endpoint
      until endpoint == P[0]      // wrapped around to first hull point
    '''
    def gift_wrap_convex_hull(self):
        return
