# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:22:03 2025

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

length = len(fname_list)

fig, axs = plt.subplots(1, 2)

b2fgeo = lbm.read_b2fgmtry(fname = 'b2fgmtry_mastu')


X, Y = lbm.calcgrid_method(geo = b2fgeo)

inner_r = np.arange(1, 19)
outer_r = np.arange(19, 37)

inner_p = np.arange(1, 48)
outer_p = np.arange(49, 97)


in_top_p = np.arange(36, 48)
in_core_p = np.arange(13, 36)
in_bottom_p = np.arange(1, 13)
 

out_top_p = np.arange(49, 62)
out_core_p = np.arange(62, 85)
out_bottom_p = np.arange(85, 97)



print('x range is:')
print(X.shape[0])


for k in inner_r:
    
    #inner lower PFR
    axs[0].plot(X[k, 1:13], Y[k, 1:13], 'green', linewidth=1)


            
    #inner upper PFR
    axs[0].plot(X[k, 36:48], Y[k, 36:48], 'orange', linewidth=1)
    axs[0].plot(X[k, 13:36], Y[k, 13:36], 'cyan', linewidth=1)
            
    #outer upper PFR
    axs[0].plot(X[k, 49:62], Y[k, 49:62], 'tan', linewidth=1)
    axs[0].plot(X[k, 62:85], Y[k, 62:85], 'teal', linewidth=1)


    #outer lower PFR
    axs[0].plot(X[k, 85:], Y[k, 85:], 'lightgreen', linewidth=1)


for k in outer_r:
    
    #inner SOL
    axs[0].plot(X[k, 1:13], Y[k, 1:13], 'blue', linewidth=1)
    axs[0].plot(X[k, 13:36], Y[k, 13:36], 'blue', linewidth=1)
    axs[0].plot(X[k, 36:48], Y[k, 36:48], 'blue', linewidth=1)
    
    #outer SOL
    axs[0].plot(X[k, 49:62], Y[k, 49:62], 'purple', linewidth=1)
    axs[0].plot(X[k, 62:85], Y[k, 62:85], 'purple', linewidth=1)
    axs[0].plot(X[k, 85:], Y[k, 85:], 'purple', linewidth=1)


for k in in_top_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'orange', linewidth=1)  
    

for k in out_top_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'tan', linewidth=1) 


for k in in_core_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'cyan', linewidth=1) 


for k in out_core_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'teal', linewidth=1) 


for k in in_bottom_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'green', linewidth=1)
    

for k in out_bottom_p:  # vertical lines

    axs[0].plot(X[:18, k], Y[:18, k], 'lightgreen', linewidth=1) 


for k in outer_p:  # vertical lines

    # axs[0].plot(X[:18, k], Y[:18, k], 'cyan', linewidth=1)   
    axs[0].plot(X[18:, k], Y[18:, k], 'purple', linewidth=1)
    
    
for k in inner_p:  # vertical lines

    # axs[0].plot(X[:18, k], Y[:18, k], 'cyan', linewidth=1)    
    axs[0].plot(X[18:, k], Y[18:, k], 'blue', linewidth=1)

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

half_width = 47

half_height = 19
bottom_PFR_width = 12
core_width = 23
top_PFR_width = 12



# Define colors for each section
colors = {
    'Inner bottom PFR':'green',
    'Inner core': 'cyan',
    'Inner SOL': 'blue',
    'Inner top PFR': 'orange',
    'Outer SOL': 'purple',
    'Outer core': 'teal',
    'Outer top PFR': 'tan',
    'Outer bottom PFR': 'lightgreen'
}

# Draw vertical lines
for x in range(width + 1):
    axs[1].axvline(x, color='gray', linewidth=0.3)

# Draw horizontal lines
for y in range(height + 1):
    axs[1].axhline(y, color='gray', linewidth=0.3)


axs[1].axvline(x= 50, color='black', linewidth=2, linestyle= '--')
axs[1].axvline(x = 48, color='black', linewidth=2, linestyle= '--')

axs[1].vlines(x=13, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=36, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=62, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=85, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')

# Add patches (rectangles) for each labeled region
# Lower half
axs[1].add_patch(patches.Rectangle((1, 1), bottom_PFR_width, half_height -1, facecolor=colors['Inner bottom PFR'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((13, 1), core_width, half_height -1, facecolor=colors['Inner core'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((36, 1), top_PFR_width, half_height -1, facecolor=colors['Inner top PFR'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((50, 1), top_PFR_width, half_height -1, facecolor=colors['Outer top PFR'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((62, 1), core_width, half_height -1, facecolor=colors['Outer core'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((85, 1), bottom_PFR_width, half_height -1, facecolor=colors['Outer bottom PFR'], edgecolor='none'))

# Upper half
axs[1].add_patch(patches.Rectangle((1, half_height), half_width, half_height -1, facecolor=colors['Inner SOL'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((50, half_height), half_width, half_height -1, facecolor=colors['Outer SOL'], edgecolor='none'))

# Add text labels
# axs[1].text(1.5, 0.5, 'Core', ha='center', va='center', fontsize=12)
# axs[1].text(1.5, 1.5, 'SOL', ha='center', va='center', fontsize=12)
# axs[1].text(0.5, 0.5, 'Inner divertor', ha='center', va='center', rotation='vertical', fontsize=12)
# axs[1].text(2.5, 0.5, 'Outer divertor', ha='center', va='center', rotation='vertical', fontsize=12)



# Set limits and remove axes
axs[1].set_xlim(0, width)
axs[1].set_ylim(0, height)
axs[1].set_aspect('equal')
axs[1].axis('off')












    
    



