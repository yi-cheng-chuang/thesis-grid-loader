# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:22:03 2025

@author: ychuang
"""


import load_B2grid_method as lbm
import numpy as np
import matplotlib.pyplot as plt



    
vessel = np.loadtxt('vvfile.ogr')

# Plot the curvilinear grid


cut_filter = True
plot_vessel = True


fname_list = ['b2fgmtry', 'b2fgmtry_mastu']

length = len(fname_list)

fig, axs = plt.subplots(1, 2)

b2fgeo = lbm.read_b2fgmtry(fname = 'b2fgmtry_mastu')


X, Y = lbm.calcgrid_method(geo = b2fgeo)

inner_r = np.arange(0, 18)
outer_r = np.arange(18, 37)

inner_p = np.arange(0, 49)
outer_p = np.arange(49, 97)


in_top_p = np.arange(36, 47)
in_core_p = np.arange(13, 36)
in_bottom_p = np.arange(0, 13)
 

out_top_p = np.arange(48, 62)
out_core_p = np.arange(62, 85)
out_bottom_p = np.arange(85, 97)



print('x range is:')
print(X.shape[0])


for k in inner_r:
    
    #inner lower PFR
    axs[0].plot(X[k, :13], Y[k, :13], 'green', linewidth=1)


            
    #inner upper PFR
    axs[0].plot(X[k, 36:47], Y[k, 36:47], 'orange', linewidth=1)
    axs[0].plot(X[k, 13:36], Y[k, 13:36], 'cyan', linewidth=1)
            
    #outer upper PFR
    axs[0].plot(X[k, 49:62], Y[k, 49:62], 'tan', linewidth=1)
    axs[0].plot(X[k, 62:85], Y[k, 62:85], 'teal', linewidth=1)


    #outer lower PFR
    axs[0].plot(X[k, 85:], Y[k, 85:], 'lightgreen', linewidth=1)


for k in outer_r:
    
    #inner SOL
    axs[0].plot(X[k, :13], Y[k, :13], 'blue', linewidth=1)
    axs[0].plot(X[k, 13:36], Y[k, 13:36], 'blue', linewidth=1)
    axs[0].plot(X[k, 36:47], Y[k, 36:47], 'blue', linewidth=1)
    
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
    



# Set grid size
cols = 96
rows = 36



# Draw vertical lines
for x in range(cols + 1):
    axs[1].axvline(x, color='lightgray', linewidth=0.5)

# Draw horizontal lines
for y in range(rows + 1):
    axs[1].axhline(y, color='lightgray', linewidth=0.5)

# Set axis limits
axs[1].set_xlim(0, cols)
axs[1].set_ylim(0, rows)

# Set equal aspect ratio
axs[1].set_aspect('equal')

# Optional: remove ticks
# ax.set_xticks([])
# ax.set_yticks([])

# plt.title("96x36 Grid")
# plt.show()



plt.tight_layout()




    
    



