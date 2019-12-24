#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:38:36 2019

@author: gabriel
"""

from StreamGenerator import StreamGenerator
from Counters import Counters
from collections import defaultdict

letter_generator = StreamGenerator("gabrieldarochasilva")
n_iters = [100,1000,10000,100000,1000000]
for n_iter in n_iters:
    dict_list = []
    for i in range(0,10):
        counters = Counters()
        for i in range(0,n_iter):
            counters.update_counters( letter_generator.get_character() )
        dict_list.append( counters.get_dicts() )
    
    max_values = defaultdict()
    min_values = defaultdict()
    average_values_prob = defaultdict()
    average_values_full = defaultdict()
    for result in dict_list:
        for key,value in result[0].items():
            if key not in average_values_full:
                average_values_full[key] = value
            else:
                average_values_full[key] += value
        
        for key,value in result[1].items():
            if key not in max_values:
                max_values[key] = value
            elif key in max_values and max_values[key] < value:
                max_values[key] = value
                
                
            if key not in min_values:
                min_values[key] = value
            elif key in max_values and min_values[key] > value:
                min_values[key] = value
                
            if key not in average_values_prob:
                average_values_prob[key] = value
            else:
                average_values_prob[key] += value
                
    average_values_prob = counters.get_average_dict(average_values_prob, 10)
    average_values_full = counters.get_average_dict(average_values_full, 10)
    
    file = open("contagens_prob.txt", 'a+')
    file_2 = open("contagens_full.txt", 'a+')
    file.write("\n")
    file_2.write("\n")
    string_to_write = "N_Iteracoes = " + str(n_iter) + "\n"
    file.write(string_to_write)
    for key,value in average_values_prob.items():
        string_to_write = "Key: " + key + "\n"
        file.write(string_to_write)
        file_2.write(string_to_write)
        string_to_write = "Average: " + str(value) + "\n"
        string_to_write_2 = "Average: " + str(average_values_full[key]) + "\n"
        file_2.write(string_to_write_2)
        file.write(string_to_write)
        string_to_write = "Min: " + str(min_values[key])+ "\n"
        file.write(string_to_write)
        string_to_write = "Max: " + str(max_values[key])+ "\n"
        file.write(string_to_write)
        string_to_write = "Expected value: " + str(value*8) + "\n"
        file.write(string_to_write)
        
    file.close()
    file_2.close()