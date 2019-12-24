#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:45:47 2019

@author: gabriel
"""
from random import randint

class StreamGenerator(object):
    def __init__(self,name):
        self.string_name = name
        
    def get_character(self):
        return self.string_name[randint(0,len(self.string_name)-1)]
    
