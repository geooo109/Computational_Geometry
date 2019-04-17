import numpy as np
from sympy.geometry import *
from sympy.plotting.pygletplot import PygletPlot as Plot
import matplotlib.pyplot as plt
import matplotlib.path as mpltPath

def find_points():
    return [(0.2,0), (0.5,0.886), (1.5,1.0), (2.0,0.0)]

def construct_poly(points):
    p1, p2, p3, p4 = points
    points.append(p1)
    return Polygon(p1, p2, p3, p4)

def check_sympy(poly,p1,p2):
    print(poly.encloses_point(p1))
    print(poly.encloses_point(p2))
    print(poly.encloses(poly))

def check_matplot(points,p1,p2):
    path = mpltPath.Path(points)
    print(path.contains_point(list(p1),radius=0.1))
    print(path.contains_point(list(p2),radius=0.1))
    print(path.contains_points(points,radius=0.1))

def plot_poly(points,poly):
    x_val = [x[0] for x in points]
    y_val = [x[1] for x in points]

    pa = (0.8,0.5)
    pb = (1.0,1.0)

    plt.plot(x_val,y_val)
    plt.plot(x_val,y_val,'or')
    plt.plot(pa[0],pa[1],'ro')
    plt.plot(pb[0],pb[1],'ro')
    plt.show()
    check_sympy(poly,pa,pb)
    check_matplot(points,pa,pb)

def main():
    points = find_points()
    poly = construct_poly(points)
    print(poly)
    plot_poly(points,poly)

if __name__ == "__main__":
    main()
