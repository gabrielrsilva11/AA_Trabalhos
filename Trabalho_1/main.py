# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:44:09 2019

@author: Gabriel Silva, 100451

Main file to run the vertex cover problem, graphs with 4,6,8,10,11,12,13,14 vertices are used to test the algorithm.
It outputs the the number of vertices our graph has, the minimum vertex cover needed for that graph, number of basic operations
running time.
"""
from VertexCover import VertexCover
from ExpFit import ExpFit
import datetime
import numpy as np

graph_1 = [[0, 1, 1, 1],
         [1, 0, 0, 0],
         [1, 0, 0, 1],
         [1, 0, 1, 0]]

graph_2 = [[0,1,1,0,0,1],
           [1,0,0,1,1,1],
           [1,0,0,0,1,0],
           [0,1,0,0,0,1],
           [0,1,0,0,0,0],
           [1,1,0,1,0,0]]

graph_3 = [[0,1,0,0,1,1,0,1],
           [1,0,1,0,1,0,0,1],
           [0,1,0,1,1,0,1,0],
           [0,0,1,0,0,1,1,1],
           [1,1,1,1,0,0,0,0],
           [1,0,0,1,0,0,1,0],
           [0,0,1,1,0,1,0,1],
           [1,1,0,1,0,0,1,0]]

graph_4 = [[0,1,0,0,1,1,0,1,0,1],
           [1,0,1,0,1,0,0,1,1,0],
           [0,1,0,1,1,0,1,0,1,0],
           [0,0,1,0,0,1,1,1,0,0],
           [1,1,1,1,0,0,0,0,1,1],
           [1,0,0,1,0,0,1,0,0,0],
           [0,0,1,1,0,1,0,1,1,0],
           [1,1,0,1,0,0,1,0,0,1],
           [0,1,1,0,1,0,1,0,0,1],
           [1,0,0,0,1,0,0,1,1,0]]

graph_5 = [[0,1,0,0,1,1,0,1,0,1,1],
           [1,0,1,0,1,0,0,1,1,0,0],
           [0,1,0,1,1,0,1,0,1,0,0],
           [0,0,1,0,0,1,1,1,0,0,0],
           [1,1,1,1,0,0,0,0,1,1,1],
           [1,0,0,1,0,0,1,0,0,0,0],
           [0,0,1,1,0,1,0,1,1,0,1],
           [1,1,0,1,0,0,1,0,0,1,0],
           [0,1,1,0,1,0,1,0,0,1,1],
           [1,0,0,0,1,0,0,1,1,0,0],
           [1,0,0,0,1,0,1,0,1,0,0]]

graph_6 = [[0,1,0,0,1,1,0,1,0,1,1,0],
           [1,0,1,0,1,0,0,1,1,0,0,1],
           [0,1,0,1,1,0,1,0,1,0,0,1],
           [0,0,1,0,0,1,1,1,0,0,0,1],
           [1,1,1,1,0,0,0,0,1,1,1,1],
           [1,0,0,1,0,0,1,0,0,0,0,0],
           [0,0,1,1,0,1,0,1,1,0,1,1],
           [1,1,0,1,0,0,1,0,0,1,0,0],
           [0,1,1,0,1,0,1,0,0,1,1,0],
           [1,0,0,0,1,0,0,1,1,0,0,1],
           [1,0,0,0,1,0,1,0,1,0,0,0],
           [0,1,1,1,1,0,1,0,0,1,0,0]]

graph_7 = [[0,1,0,0,1,1,0,1,0,1,1,0,1],
           [1,0,1,0,1,0,0,1,1,0,0,1,0],
           [0,1,0,1,1,0,1,0,1,0,0,1,0],
           [0,0,1,0,0,1,1,1,0,0,0,1,1],
           [1,1,1,1,0,0,0,0,1,1,1,1,0],
           [1,0,0,1,0,0,1,0,0,0,0,0,1],
           [0,0,1,1,0,1,0,1,1,0,1,1,0],
           [1,1,0,1,0,0,1,0,0,1,0,0,0],
           [0,1,1,0,1,0,1,0,0,1,1,0,1],
           [1,0,0,0,1,0,0,1,1,0,0,1,1],
           [1,0,0,0,1,0,1,0,1,0,0,0,0],
           [0,1,1,1,1,0,1,0,0,1,0,0,1],
           [1,0,0,1,0,1,0,0,1,1,0,1,0]]

graph_8 = [[0,1,0,0,1,1,0,1,0,1,1,0,1,1],
           [1,0,1,0,1,0,0,1,1,0,0,1,0,0],
           [0,1,0,1,1,0,1,0,1,0,0,1,0,1],
           [0,0,1,0,0,1,1,1,0,0,0,1,1,0],
           [1,1,1,1,0,0,0,0,1,1,1,1,0,0],
           [1,0,0,1,0,0,1,0,0,0,0,0,1,0],
           [0,0,1,1,0,1,0,1,1,0,1,1,0,1],
           [1,1,0,1,0,0,1,0,0,1,0,0,0,0],
           [0,1,1,0,1,0,1,0,0,1,1,0,1,1],
           [1,0,0,0,1,0,0,1,1,0,0,1,1,0],
           [1,0,0,0,1,0,1,0,1,0,0,0,0,1],
           [0,1,1,1,1,0,1,0,0,1,0,0,1,0],
           [1,0,0,1,0,1,0,0,1,1,0,1,0,1],
           [1,0,1,0,0,0,1,0,1,0,1,0,1,0]]

graph = [graph_1, graph_2,graph_3, graph_4, graph_5, graph_6,graph_7,graph_8]

v_cover = VertexCover()
i = 4
for x in graph:
    print("\n\n")
    print("Number of vertices: ", i)
    starttime_naive = datetime.datetime.now()
    cover, operations = v_cover.min_vertex_cover(x)
    print("Cover Naive: ", cover)
    print("Operations Naive: ", operations)
    print("Running Time Naive: ", datetime.datetime.now()-starttime_naive)
    if i < 10:
        i += 2
    else:
        i += 1

model = ExpFit()        
x = np.array([4,6,8,10,11,12,13,14])
y = np.array([0.000230,0.000541,0.005217,0.009482,0.015446,0.030069,0.034510,0.069203])
x_predict = np.array([16,18,20,22])
parameters, covariance = model.fit(x,y)
y_predicted = model.predict(x_predict, parameters)
model.plot(x,y,x_predict,y_predicted)
