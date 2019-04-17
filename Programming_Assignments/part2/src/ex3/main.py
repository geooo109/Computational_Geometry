import random
from scipy.sparse.csgraph import *
from scipy.sparse import csr_matrix
import numpy as np
import matplotlib.pyplot as plt

RANGE_XY = 100
def gen_points():
    num_points = int(input("Give number of Points to generate Dalauny Triangulation: "))
    list = [np.random.randint(0, RANGE_XY) for i in range(num_points*num_points)]
    return split_list(list,num_points)

def split_list (big_list,x):
   return [big_list[i:i+x] for i in range(0, len(big_list), x)]

def construct_graph(points):
    graph = csr_matrix(points)
    print(graph)
    return graph
    # plt.triplot(points[:,0], points[:,1], del_triag.simplices.copy())
    # plt.plot(points[:,0], points[:,1], 'o')
    # plt.show()

def sortest_path(graph):
    dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=0, return_predecessors=True)
    print(dist_matrix)
#    print(predecessors)

def main():
    #generate random points
    try :
        points = gen_points()
        print(points)
    except:
        print("ERROR on generating random points")
        return

    graph = construct_graph(points)
    sortest_path(graph)

if __name__ == "__main__":
    main()
