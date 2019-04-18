import random
from scipy.sparse.csgraph import *
from scipy.sparse import csr_matrix
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

RANGE_XY = 100
# def gen_points():
#     num_points = int(input("Give number of Points to generate Dalauny Triangulation: "))
#     return np.array([[np.random.randint(0, RANGE_XY),np.random.randint(0, RANGE_XY)] for i in range(num_points)])
#     construct_graph_list(arr,num_points)

def gen_points():
    num_points = int(input("Give number of Points to generate Dalauny Triangulation: "))
    list = [np.random.randint(0, RANGE_XY) for i in range(num_points*num_points)]
    return split_list(list,num_points)

def split_list (big_list,x):
   return [big_list[i:i+x] for i in range(0, len(big_list), x)]

def compute_plot_delauny(points):
    del_triag = Delaunay(points)
    print(points[0,0])
    plt.triplot(points[:,0], points[:,1], del_triag.simplices.copy())
    plt.plot(points[:,0], points[:,1], 'o')
    plt.show()

def construct_graph(points):
    graph = csr_matrix(points)
    print(graph)
    return graph

def sortest_path(graph):
    shortest_path(graph, method='auto', directed=False, return_predecessors=False,
                  unweighted=False, overwrite=False, indices=None)
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
    G_masked = np.ma.masked_values(points, 0)
    G2_sparse = csgraph_from_dense(points, null_value=np.inf)
    # k = np.array(G_masked)
    print(G2_sparse)
    compute_plot_delauny(G_masked)
    # graph = construct_graph(points)
    #sortest_path(G2_sparse)

if __name__ == "__main__":
    main()
