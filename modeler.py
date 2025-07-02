import numpy as np
from collections import defaultdict
from scipy.spatial import Delaunay
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
        if self.xval[0] <= x <= self.xval[1] and self.yval[0] <= y <= self.yval[1] and self.zval[0] <= z <= self.zval[1]:
            x = round(x * self.res)
            y = round(y * self.res)
            z = round(z * self.res)
            self.points.append((x, y, z))
    def addf(self, f0, f1, error = 0.0):
        function = []
        x = np.linspace(self.xval[0], self.xval[1], int(self.xrange * self.res))
        y = np.linspace(self.yval[0], self.yval[1], int(self.yrange * self.res))
        z = np.linspace(self.zval[0], self.zval[1], int(self.zrange * self.res))
        try:
            f0 = eval('lambda x, y, z:' + f0)
            f1 = eval('lambda x, y, z:' + f1)
        except:
            pass
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
        try:
            del self.points[point]
        except:
            pass
    def delf(self, function = 0):
        try:
            del self.functions[function]
        except:
            pass
    def cla(self):
        self.points = []
        self.functions = []
        self.model = []
    def compose(self):
        functions = [item for sublist in self.functions for item in sublist]
        self.model = self.points + functions
        self.model = set(self.model)
        self.model = list(self.model)
        self.model = [(x / self.res, y / self.res, z /self.res) for (x, y, z ) in self.model]
        return self.model
    def obj(self, model):
        model = np.array(model)
        tri = Delaunay(model)
        facecount = defaultdict(int)
        for simplex in tri.simplices:
            faces = [
                tuple(sorted((simplex[0], simplex[1], simplex[2]))),
                tuple(sorted((simplex[0], simplex[1], simplex[3]))),
                tuple(sorted((simplex[0], simplex[2], simplex[3]))),
                tuple(sorted((simplex[1], simplex[2], simplex[3]))),
            ]
            for face in faces:
                facecount[face] += 1
        surfaces = [face for face, count in facecount.items() if count == 1]
        obj = ''
        for x, y, z in model:
            obj += f'v {x} {y} {z}\n'
        for face in surfaces:
            obj += f'f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n'
        return obj
modeler = Modeler()