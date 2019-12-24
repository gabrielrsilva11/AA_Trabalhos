# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:41:33 2019

@author: Gabriel Silva, 100451

Vertex cover algorithm:
    
    Initialize all possible solutions
    while there are solutions
        Check if current solution is valid:
            if valid:
                count the number of vertices used
    return the lowest count value
"""

import itertools

class VertexCover():
    
    def validity_check(self,cover, graph, operations):
        is_valid = True
        for i in range(len(graph)):
            operations += 1
            for j in range(i+1, len(graph[i])):
                operations += 1
                if graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1': #check if the given solution is valid according to the graph
                    operations += 1
                    return False, operations
        return is_valid, operations
    
    def min_vertex_cover(self,graph):
        n = len(graph)
        minimum_cover = n
        num_edge = list(itertools.product(*["01"] * n)) #initialize every possible solution
        print(len(num_edge))
        operations = 0
        for i in num_edge: #go through every solution and check if they're valid.
            operations += 1
            valid, operations = self.validity_check(i,graph,operations)
            if valid:
                counter = 0
                for value in i:
                    operations += 1
                    if value == '1':
                        operations += 1
                        counter += 1
                minimum_cover = min(counter, minimum_cover) #check if the solution is better than the current solution
        return minimum_cover, operations




