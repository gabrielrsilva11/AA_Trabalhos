# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:41:33 2019

@author: gabriel, 100451
"""
import datetime
import itertools
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def validity_check(cover, graph, operations):
    is_valid = True
    for i in range(len(graph)):
        operations += 1
        for j in range(i+1, len(graph[i])):
            operations += 1
            if graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1':
                operations += 1
                return False, operations
    return is_valid, operations


def min_vertex_cover_naive(graph):
    n = len(graph)
    minimum_cover = n
    num_edge = list(itertools.product(*["01"] * n))
    operations = 0
    for i in num_edge:
        operations += 1
        valid, operations = validity_check(i,graph,operations)
        if valid:
            counter = 0
            for value in i:
                operations += 1
                if value == '1':
                    operations += 1
                    counter += 1
            minimum_cover = min(counter, minimum_cover)
    return minimum_cover, operations

def min_vertex_cover_greedy(graph):
    cover = []
    operations = 0
    valid, num_edge, operations = valid_cover(graph, cover, operations = 0)

    while not valid:
        operations += 1
        for x in range(0, len(num_edge)):
            operations += 1
            if num_edge[x] == max(num_edge):
                cover.append(x)
                break
        valid, num_edge, operations = valid_cover(graph, cover, operations)
    return len(cover), operations

def valid_cover(graph, cover, operations):
    valid = True
    num_edge = [0] * len(graph)
    for i in range(0, len(graph)):
        operations += 1
        for j in range(i, len(graph)):
            operations += 1
            if graph[i][j] == 1:
                operations += 1
                if (i not in cover) and (j not in cover):
                    operations += 1
                    valid = False
                    num_edge[i] += 1
                    num_edge[j] += 1
    return valid, num_edge, operations

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
i = 4
for x in graph:
    print("\n\n")
    print("Number of vertices: ", i)
    starttime_naive = datetime.datetime.now()
    cover, operations = min_vertex_cover_naive(x)
    print("Cover Naive: ", cover)
    print("Operations Naive: ", operations)
    print("Running Time Naive: ", datetime.datetime.now()-starttime_naive)
    starttime_greedy = datetime.datetime.now()
    cover, operations = min_vertex_cover_greedy(x)
    print("Cover Greedy: ", cover)
    print("Operations Greedy: ", operations)
    print("Running Time Greedy: ", datetime.datetime.now()-starttime_greedy)
    i += 2

x = np.array([4,6,8,10,11,12,13,14]).reshape(-1,1)
y = np.array([0.000230,0.000541,0.005217,0.009482,0.015446,0.030069,0.034510,0.069203])
x_2 = np.array([16,18,20]).reshape(-1,1)

poly = PolynomialFeatures(degree = 1)
X_ = poly.fit_transform(x)
predict_ = poly.fit_transform(x_2)

model = LinearRegression()
model.fit(X_,np.log(y))
predict = model.predict(predict_)
