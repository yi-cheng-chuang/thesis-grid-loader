# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:05:44 2025

@author: ychuang
"""

import load_B2grid_method as lbm
import numpy as np
import matplotlib.pyplot as plt


b2fgeo = lbm.read_b2fgmtry(fname = 'b2fgmtry')


X, Y = lbm.calcgrid_method(geo = b2fgeo)
    
vessel = np.loadtxt('vvfile.ogr')

# Plot the curvilinear grid


cut_filter = True
plot_vessel = True

plt.figure()

if cut_filter:

    for k in range(X.shape[0]):  # horizontal lines
        plt.plot(X[k, :13], Y[k, :13], 'b', linewidth=1)
        plt.plot(X[k, 13:36], Y[k, 13:36], 'b', linewidth=1)
        plt.plot(X[k, 36:47], Y[k, 36:47], 'b', linewidth=1)
        plt.plot(X[k, 49:62], Y[k, 49:62], 'b', linewidth=1)
        plt.plot(X[k, 62:85], Y[k, 62:85], 'b', linewidth=1)
        plt.plot(X[k, 85:], Y[k, 85:], 'b', linewidth=1)
else:

    for k in range(X.shape[0]):  # horizontal lines
        plt.plot(X[k, :], Y[k, :], 'b', linewidth=1)



for k in range(X.shape[1]):  # vertical lines
    plt.plot(X[:, k], Y[:, k], 'r', linewidth=1)

if plot_vessel:
    
    plt.plot(vessel[:,0]/1000, vessel[:,1]/1000, color = 'black', linewidth = 2)

else:
    pass


plt.gca().set_aspect('equal')
plt.title("B2.5 Curvilinear Grid")
plt.xlabel("R: [m]")
plt.ylabel("Z: [m]")
plt.show()



    
    
    
    
    
