# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:41:33 2019

@author: gabriel, 100451
"""
import datetime
import itertools

def validity_check(cover, graph):
    is_valid = True
    for i in range(len(graph)):
        for j in range(i+1, len(graph[i])):
            if graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1':
                return False
    return is_valid


def min_vertex_cover_naive(graph):
    n = len(graph)
    minimum_cover = n
    num_edge = list(itertools.product(*["01"] * n))
    for i in num_edge:
        if validity_check(i, graph):
            counter = 0
            for value in i:
                if value == '1':
                    counter += 1
            print(counter)
            minimum_cover = min(counter, minimum_cover)
    return minimum_cover

def min_vertex_cover_greedy(graph):
    cover = []
    valid, num_edge = valid_cover(graph, cover)
    
    while not valid:
        for x in range(0, len(num_edge)):
            if num_edge[x] == max(num_edge):
                cover.append(x)
                break
        valid, num_edge = valid_cover(graph, cover)
    return cover

def valid_cover(graph, cover):
    valid = True
    num_edge = [0] * len(graph)
    for i in range(0, len(graph)):
        for j in range(i, len(graph)):
            if graph[i][j] == 1:
                if (i not in cover) and (j not in cover):
                    valid = False
                    num_edge[i] += 1
                    num_edge[j] += 1
    return valid, num_edge

graph_1 = [[0, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0]]

graph_2 = [[0,1,1,0,0,0,0,0],
           [1,0,0,1,0,1,0,0],
           [1,0,0,1,1,0,1,0],
           [0,1,1,0,1,0,0,0],
           [0,0,1,1,0,0,1,0],
           [0,1,0,0,0,0,0,1],
           [0,0,1,0,1,0,0,0],
           [0,0,0,0,0,1,0,0]]

graph_3 = [[0,1,1,0,0,0,0,0,1,1,1],
           [1,0,0,1,0,1,0,0,0,0,0],
           [1,0,0,1,1,0,1,0,0,0,1],
           [0,1,1,0,1,0,0,0,0,0,0],
           [0,0,1,1,0,0,1,0,0,0,0],
           [0,1,0,0,0,0,0,1,0,0,0],
           [0,0,1,0,1,0,0,0,0,0,0],
           [0,0,0,0,0,1,0,0,0,1,0],
           [1,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,1,0,0,0],
           [1,0,1,0,0,0,0,0,0,0,0]]

graph_4 = [[0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

graph = [graph_1, graph_2,graph_3]#, graph_4]
i = 1
for x in graph:
    starttime_naive = datetime.datetime.now()
    cover = min_vertex_cover_naive(x)
    print(cover)
    print("Running Time Naive: ", datetime.datetime.now()-starttime_naive)
    starttime_greedy = datetime.datetime.now()
    cover = min_vertex_cover_greedy(x)
    print(cover)
    print("Running Time Greedy: ", datetime.datetime.now()-starttime_greedy)
    i += 1