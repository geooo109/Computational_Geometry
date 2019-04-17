import random
from scipy.spatial import KDTree as KDTree
import numpy as np
import matplotlib.pyplot as plt


RANGE_XY = 100000
def gen_points():
    num_points = int(input("Give number of Points to create KDTree: "))
    return np.array([[np.random.randint(0, RANGE_XY),np.random.randint(0, RANGE_XY)] for i in range(num_points)])

def NN_kd_tree(points):
    kd_tree = KDTree(points)
    nn_res  = kd_tree.query(points)
    print nn_res

def main():
    #generate random points
    try :
        points = gen_points()
    except:
        print("ERROR on generating random points")
        return

    #compute NN for points
    NN_kd_tree(points)

if __name__ == "__main__":
    main()




















