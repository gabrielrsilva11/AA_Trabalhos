# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:41:33 2019

@author: Gabriel Silva, 100451

"""

import itertools

class VertexCover():

    def validity_check(self,cover, graph, operations):
        is_valid = True
        for i in range(len(graph)):
            operations += 1
            for j in range(i+1, len(graph[i])):
                operations += 1
                if graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1':
                    operations += 1
                    return False, operations
        return is_valid, operations
    
    def min_vertex_cover(self,graph):
        n = len(graph)
        minimum_cover = n
        num_edge = list(itertools.product(*["01"] * n)) #inicializar todas as possiveis solucoes
        operations = 0
        for i in num_edge: #ciclo para percorrer todas as solucoes e verificar se sao validas
            operations += 1
            valid, operations = self.validity_check(i,graph,operations)
            if valid:
                counter = 0
                for value in i:
                    operations += 1
                    if value == '1':
                        operations += 1
                        counter += 1
                minimum_cover = min(counter, minimum_cover)
        return minimum_cover, operations




