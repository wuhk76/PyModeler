import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def parseobj(objpath):
    points = []
    with open(objpath) as obj:
        obj = obj.readlines()
    for line in obj:
        line = line.strip()
        if line.startswith('v '):
            line = line.split()
            del line[0]
            line = [float(value.strip()) for value in line]
            point = tuple(line)
            points.append(point)
    return points
mesh = parseobj(input('Enter path of OBJ:'))
x, y, z = zip(*mesh)
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_box_aspect([1, 1, 1])
ax.scatter(x, y, z, s = 1, color = 'blue')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show(block = True)