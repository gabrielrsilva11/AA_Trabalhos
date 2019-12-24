# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:47:33 2019

@author: Gabriel Silva, 100451

<<<<<<< HEAD
Function to fit the naive algorithm, since it runs in exponential time and we want to see hw long it would take
to run graphs with more vertices we create a simple curve to fit our data and predict what we want.
=======

Function to fit the naive algorithm, since it runs in exponential time and we want to see how long it would take
to run examples with higher number of vertices
>>>>>>> cd3527bfc4b09882f28d6c055c42a5fcb0e4b759
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


class ExpFit():

    def exp_func(self,x, a, b, c):
        return a * np.exp(b * x) + c

    def fit(self,x,y):
        popt, pcov = curve_fit(self.exp_func,x,y)
        return popt,pcov

    def predict(self,x_predict, popt):
        return self.exp_func(x_predict, *popt)

    def plot(self,x,y,x_pred,y_pred):
        plt.figure()
        plt.plot(x,y,'ko', label ='Pontos originais')
        plt.plot(x_pred,y_pred,'bx', label = 'Pontos previstos')
        plt.ylabel('Tempo de execução (Minutos)')
        plt.xlabel('Número de vértices')
        plt.title('Tempo de execução para instâncias de maior dimensão')
        plt.legend()
        plt.show()