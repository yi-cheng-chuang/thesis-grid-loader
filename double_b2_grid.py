# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:08:54 2025

@author: ychuang
"""


import load_B2grid_method as lbm
import numpy as np
import matplotlib.pyplot as plt



    
vessel = np.loadtxt('vvfile.ogr')

# Plot the curvilinear grid


cut_filter = False
plot_vessel = True


fname_list = ['b2fgmtry', 'b2fgmtry_mastu']

length = len(fname_list)

fig, axs = plt.subplots(1, length, sharey = True)



for ii, index in enumerate(fname_list):
    
    fgeo_name = fname_list[ii]
    
    
    b2fgeo = lbm.read_b2fgmtry(fname = fgeo_name)


    X, Y = lbm.calcgrid_method(geo = b2fgeo)



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
            axs[ii].plot(X[k, :], Y[k, :], 'b', linewidth=1)



    for k in range(X.shape[1]):  # vertical lines
        axs[ii].plot(X[:, k], Y[:, k], 'r', linewidth=1)

    if plot_vessel:
        
        axs[ii].plot(vessel[:,0]/1000, vessel[:,1]/1000, color = 'black', linewidth = 2)

    else:
        pass

    axs[ii].set_xlabel("R: [m]")
    axs[ii].set_aspect('equal')


fig.supylabel("Z: [m]")
plt.tight_layout()




    
    



