# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 15:28:23 2025

@author: ychuang
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri



filename_list_mastu =['fort_mastu.33', 'fort_mastu.34']
filename_list_mast =['fort.33', 'fort.34']


list_list = [filename_list_mast, filename_list_mastu]

length = len(list_list)

fig, axs = plt.subplots(1, length, sharey = True)

for ii, index in enumerate(list_list):
    
    ft33 = index[0]
    ft34 = index[1]
    
    Nodes=np.fromfile(ft33, sep=' ')
    NN=int(Nodes[0])
    XNodes=Nodes[1:NN+1]/100
    YNodes=Nodes[NN+1:]/100

    vessel = np.loadtxt('vvfile.ogr')

    Triangles = np.loadtxt(ft34, skiprows=1, usecols=(1,2,3)) #Alternatively use fort.34


    triang = tri.Triangulation(XNodes, YNodes, triangles= (Triangles -1))


    plot_vessel = False

    # Plot the triangulation
    axs[ii].triplot(triang, color='blue', linewidth = 0.5)
    # plt.plot(XNodes, YNodes, 'o', color='red', markersize= 1)  # plot the points

    if plot_vessel:
        
        axs[ii].plot(vessel[:,0]/1000, vessel[:,1]/1000, color = 'black', linewidth = 2)

    else:
        pass
    
    # plt.title("Triangular Grid")
    
    axs[ii].set_xlabel("R: [m]")
    axs[ii].set_aspect('equal')

fig.supylabel("Z: [m]")
plt.tight_layout()





 