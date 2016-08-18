from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math


def fact(x):
    if x <= 1:
        return 1;
    return x * fact(x - 1)


class function():
    def __init__(self, fun, x, a=0, i=0, der=0):
        if der:
            self.x = x
            self.f = fun
            self.y = (fun(a) * ((x - a) ** (i)) )/ fact(i)
        else:
            self.x = x
            self.y = fun(x)
            self.f = fun


class AproxSerie():
    def __init__(self, xmin, xmax, funs, a):
        self.x = np.linspace(xmin, xmax)
        self.fns = [function(funs[0], self.x)]
        for i in range(len(funs)-1):
            self.fns.append(function(funs[i + 1], self.x, a, i+1, 1))



    def draw(self, i, txt="fun",gen=0):
        if gen:
            plt.figure()
        plt.plot(self.x, self.fns[i].y, label=txt)



