import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv


data = np.genfromtxt('landscape.txt')

xdim, ydim = data.shape
xx = range(xdim)
yy = range(ydim)
xx, yy = np.meshgrid(xx,yy)
print(xx.shape)
grid = pv.StructuredGrid(xx,yy,data.T)
pv.set_plot_theme('paraview')
grid.plot(eye_dome_lighting=True)




#path1 = np.genfromtxt('path1.txt')
#path2 = np.genfromtxt('path2.txt')
