import numpy as np
from math import *
class Modeler:
    def __init__(self):
        self.xval = []
        self.yval = []
        self.zval = []
        self.xrange = 0.0
        self.yrange = 0.0
        self.zrange = 0.0
        self.res = 1
        self.points = []
        self.functions = []
        self.model = []
    def setd(self, x, y, z, res):
        self.xval = x
        self.yval = y
        self.zval = z
        self.xrange = self.xval[1] - self.xval[0]
        self.yrange = self.yval[1] - self.yval[0]
        self.zrange = self.zval[1] - self.zval[0]
        self.res = res
    def addp(self, x, y, z):
        x = round(x * self.res)
        y = round(y * self.res)
        z = round(z * self.res)
        self.points.append((x, y, z))
    def addf(self, f0, f1, error = 0.0):
        function = []
        x = np.linspace(self.xval[0], self.xval[1], int(self.xrange * self.res))
        y = np.linspace(self.yval[0], self.yval[1], int(self.yrange * self.res))
        z = np.linspace(self.zval[0], self.zval[1], int(self.zrange * self.res))
        f0 = eval('lambda x, y, z:' + f0)
        f1 = eval('lambda x, y, z:' + f1)
        for j in z:
            for k in y:
                for l in x:
                    try:
                        if abs(f0(j, k, l) - f1(j, k, l)) <= error:
                            function.append((round(l * self.res), round(k * self.res), round(j * self.res)))
                    except:
                        pass
        self.functions.append(function)
    def delp(self, point = 0):
        del self.points[point]
    def delf(self, function = 0):
        del self.functions[function]
    def compose(self):
        functions = [item for sublist in self.functions for item in sublist]
        self.model = self.points + functions
        self.model = set(self.model)
        self.model = list(self.model)
        self.model = [(x / self.res, y / self.res, z /self.res) for (x, y, z ) in self.model]
        return self.model
modeler = Modeler()