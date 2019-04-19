import random
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt


RANGE_XY = 100000
def gen_points():
    num_points = int(input("Give number of Points to generate Dalauny Triangulation: "))
    return np.array([[np.random.randint(0, RANGE_XY),np.random.randint(0, RANGE_XY)] for i in range(num_points)])

def compute_delauny_shortest_path(points):
    del_triag = Delaunay(points)
    

def main():
    #generate random points
    try :
        points = gen_points()
    except:
        print("ERROR on generating random points")
        return

    #compute/plot voronoi
    compute_delauny_shortest_path(points)

if __name__ == "__main__":
    main()
