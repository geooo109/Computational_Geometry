from point import *
import matplotlib.pyplot as plt

'''
 Class to represent a triangle
'''
class Triangle:
    def __init__(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3

    def print_triangle(self):
        print("\n**Points of Possible Triangle** /_\\ are:")
        self.pt1.print_point()
        self.pt2.print_point()
        self.pt3.print_point()

    def get_all_points(self):
        return (self.pt1, self.pt2, self.pt3)

    #area of triangle :
    def area(self):
        return 0.5*abs(((self.pt1.get_x()*(self.pt2.get_y()-self.pt3.get_y()))
                        +(self.pt2.get_x()*(self.pt3.get_y()-self.pt1.get_y()))
                        +(self.pt3.get_x()*(self.pt1.get_y()-self.pt2.get_y()))))

    # True if point inside the triangle else False
    # https://www.youtube.com/watch?v=H9qu9Xptf-w
    def check_pt_triangle(self, pt_test):
        tr1 = Triangle(pt_test, self.pt1, self.pt2)
        tr2 = Triangle(pt_test, self.pt2, self.pt3)
        tr3 = Triangle(pt_test, self.pt3, self.pt1)
        return tr1.area()+tr2.area()+tr3.area() == self.area()

    def display_triangle_and_test_point(self, pt_test):
        # all points of dataset
        x = []
        y = []
        x.append(self.pt1.get_x())
        x.append(self.pt2.get_x())
        x.append(self.pt3.get_x())
        y.append(self.pt1.get_y())
        y.append(self.pt2.get_y())
        y.append(self.pt3.get_y())
        plt.plot(x, y, "r-")

        #for test point
        plt.scatter([pt_test.get_x()], [pt_test.get_y()])

        plt.title('Triangle (red color), Test Point (blue color)')
        plt.show()
        return
