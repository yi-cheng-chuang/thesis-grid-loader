# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 10:43:02 2025

@author: ychuang
"""

import load_B2grid_method as lbm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches



    
vessel = np.loadtxt('vvfile.ogr')

# Plot the curvilinear grid


cut_filter = True
plot_vessel = True


fname_list = ['b2fgmtry', 'b2fgmtry_mastu']



fig, axs = plt.subplots(1, 2)

b2fgeo = lbm.read_b2fgmtry(fname = 'b2fgmtry')


X, Y = lbm.calcgrid_method(geo = b2fgeo)

inner_r = np.arange(0, 18)
outer_r = np.arange(18, 37)

outer_p = np.arange(0, 97)




in_pfr_p = np.arange(0, 24)
core_p = np.arange(25, 73)
out_pfr_p = np.arange(73, 97)






print('x range is:')
print(X.shape[0])


for k in inner_r:
    
    #inner lower PFR
    axs[0].plot(X[k, :24], Y[k, :24], 'green', linewidth=1)


    #core
    axs[0].plot(X[k, 25: 73], Y[k, 25: 73], 'cyan', linewidth=1)


    #outer lower PFR
    axs[0].plot(X[k, 73:], Y[k, 73:], 'orange', linewidth=1)


for k in outer_r:
    
    #outer SOL
    axs[0].plot(X[k, :], Y[k, :], 'blue', linewidth=1)





for k in outer_p:  # vertical lines

    # axs[0].plot(X[:18, k], Y[:18, k], 'cyan', linewidth=1)   
    axs[0].plot(X[18:, k], Y[18:, k], 'blue', linewidth=1)
    
    
for k in core_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'cyan', linewidth=1) 


for k in in_pfr_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'green', linewidth=1) 


for k in out_pfr_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'orange', linewidth=1)
    
    

if plot_vessel:
    
    axs[0].plot(vessel[:,0]/1000, vessel[:,1]/1000, color = 'black', linewidth = 2)

else:
    pass

axs[0].set_xlabel("R: [m]")
axs[0].set_ylabel("Z: [m]")
axs[0].set_aspect('equal')   
    



# Define rectangle width and height
width = 98
height = 38

simu_width = 96
simu_height = 36
simu_half_height = 18

half_height = 19
inner_PFR_width = 24
core_width = 48
outer_PFR_width = 24



# Define colors for each section
colors = {
    'Inner PFR':'green',
    'Core': 'cyan',
    'SOL': 'blue',
    'Outer PFR': 'orange',
}

# Draw vertical lines
for x in range(width + 1):
    axs[1].axvline(x, color='gray', linewidth=0.3)

# Draw horizontal lines
for y in range(height + 1):
    axs[1].axhline(y, color='gray', linewidth=0.3)




axs[1].vlines(x=25, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=73, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')

# Add patches (rectangles) for each labeled region
# Lower half
axs[1].add_patch(patches.Rectangle((1, 1), inner_PFR_width, simu_half_height, facecolor=colors['Inner PFR'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((25, 1), core_width, simu_half_height, facecolor=colors['Core'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((73, 1), outer_PFR_width, simu_half_height, facecolor=colors['Outer PFR'], edgecolor='none'))


# Upper half
axs[1].add_patch(patches.Rectangle((1, half_height), simu_width, simu_half_height, facecolor=colors['SOL'], edgecolor='none'))




# Set limits and remove axes
axs[1].set_xlim(0, width)
axs[1].set_ylim(0, height)
axs[1].set_aspect('equal')
axs[1].axis('off')