#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:27:42 2019

@author: gabriel
"""


from random import random
from collections import defaultdict
import math

class Counters(object):
    def __init__(self):
        self.full_counter = defaultdict()
        self.prob_counter = defaultdict()
        self.log_counter = defaultdict()

    def get_dicts(self):
        return self.full_counter, self.prob_counter

    def get_prob(self):
        return random()
    
    def update_counters(self, letter):
        #update the full counter
        if letter in self.full_counter:
            self.full_counter[letter] += 1
        else:
            self.full_counter[letter] = 1
        
        #get prob to update the prob_counter
        prob = self.get_prob()
        if prob < (1/8):
            if letter in self.prob_counter:
                self.prob_counter[letter] += 1
            else:
                self.prob_counter[letter] = 1
    
    def get_average_dict(self,dictio, n_rep):
        for key,value in dictio.items():
            dictio[key] = math.floor(value/n_rep)
        return dictio
        
    def print_values(self):
        print(self.full_counter)
        print(self.prob_counter)
        