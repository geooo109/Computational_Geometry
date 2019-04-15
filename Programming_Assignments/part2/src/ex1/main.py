import random
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt


RANGE_XY = 100000
def gen_points():
    num_points = int(input("Give number of Points to generate Voronoi Diagram: "))
    return np.array([[np.random.randint(0, RANGE_XY),np.random.randint(0, RANGE_XY)] for i in range(num_points)])

def compute_plot_voronoi(points):
    vor_diag = Voronoi(points)
    voronoi_plot_2d(vor_diag)
    plt.show()

def main():
    #generate random points
    try :
        points = gen_points()
    except:
        print("ERROR on generating random points")
        return

    #compute/plot voronoi
    compute_plot_voronoi(points)

if __name__ == "__main__":
    main()
