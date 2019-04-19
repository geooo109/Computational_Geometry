import random
from scipy.spatial import KDTree as KDTree
import numpy as np
import matplotlib.pyplot as plt
import time


#changed it if you want it
RANGE_XY = 1000
def gen_points():
    num_points = int(input("Give number of Points to create KDTree: "))
    return np.array([[np.random.randint(0, RANGE_XY),np.random.randint(0, RANGE_XY)] for i in range(num_points)])

def NN_kd_tree(point_search, kd_tree):
    start = time.clock()
    nn_res  = kd_tree.query(point_search)
    total_time = (time.clock() - start)
    print("Time {%s} | Min dist {%s} | NN in kd-Tree (%s)"%(total_time, nn_res[0], kd_tree.data[nn_res[1]]))

def search(points):
    #construct k-d tree
    kd_tree = KDTree(points)
    print("---Points in the kd-tree---")
    for pt in points:
        print("(%s,%s)"%(pt[0],pt[1]))
    print("---END of Points-----\n")
    point_search = []
    while True:
        ch = input("Give point in form (x,y) or x,y to apply NN search on k-d Tree else type <quit>: ")
        if ch == "quit":
            break
        if ch[0] == "(":
            ch = ch.replace("(","")
            ch = ch.replace(")","")
            ch = ch.split(",")
            point_search = [int(ch[0]),int(ch[1])]
        else:
            ch = ch.split(",")
            point_search = [int(ch[0]),int(ch[1])]
        if len(point_search) == 2:
            NN_kd_tree(point_search, kd_tree)

def main():
    #generate random points
    try :
        points = gen_points()
    except:
        print("ERROR on generating random points")
        return
    try :
        search(points)
    except:
        print("ERROR on input point for NN search")
if __name__ == "__main__":
    main()
