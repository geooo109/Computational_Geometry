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

def encloses_point(poly,point):
    if poly.encloses_point(point) == False :
        print("\nPolygon does not enclose :", point)
    else :
        print("\nPolygon encloses :", point)

def encloses_poly(poly):
    if poly.encloses(poly) == False :
        print("\nPolygon does not enclose itself")
    else :
        print("\nPolygon does not enclose itself")

def contains_point(path,point):
    if path.contains_point(list(point),radius=0.1) == False :
        print("\nPolygon does not enclose :", point)
    else :
        print("\nPolygon encloses :", point)

def contains_poly(path,points):
    if np.all(path.contains_points(points,radius=0.1)) == False :
        print("\nPolygon does not enclose itself")
    else :
        print("\nPolygon encloses itself")

def check_sympy(poly,p1,p2):
    encloses_point(poly,p1)
    encloses_point(poly,p2)
    encloses_poly(poly)

def check_matplot(points,p1,p2):
    path = mpltPath.Path(points)
    contains_point(path,p1)
    contains_point(path,p2)
    contains_poly(path,points)

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
    print("\n\nUsing sympy library:")
    print("---------------------")
    check_sympy(poly,pa,pb)
    print("\n\nUsing matplot library:")
    print("-----------------------")
    check_matplot(points,pa,pb)

def main():
    points = find_points()
    poly = construct_poly(points)
    print(poly)
    plot_poly(points,poly)

if __name__ == "__main__":
    main()
