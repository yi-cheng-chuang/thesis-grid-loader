# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:03:33 2025

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


for aa, fname in enumerate(fname_list):
    
    
    b2fgeo = lbm.read_b2fgmtry(fname = fname)


    X, Y = lbm.calcgrid_method(geo = b2fgeo)

        
    if aa == 0:
        
        axs[aa].plot(X[0, 25: 73], Y[0, 25: 73], 'cyan', linewidth=3)

        axs[aa].plot(X[-1, :], Y[-1, :], 'blue', linewidth=3)
        
        axs[aa].plot(X[0, :24], Y[0, :24], 'green', linewidth=3)
        axs[aa].plot(X[0, 73:], Y[0, 73:], 'orange', linewidth=3)
        
        axs[aa].plot(X[18, 24: 73], Y[18, 24: 73], 'red', linewidth=1, linestyle= '--')
        
        axs[aa].plot(X[18, :24], Y[18, :24], 'red', linewidth=1, linestyle= '--')
        axs[aa].plot(X[18, 72:], Y[18, 72:], 'red', linewidth=1, linestyle= '--')
        
    
    elif aa == 1:
        
        axs[aa].plot(X[0, 1:13], Y[0, 1:13], 'green', linewidth=3)                
        #inner upper PFR
        axs[aa].plot(X[0, 36:48], Y[0, 36:48], 'orange', linewidth=3)
        axs[aa].plot(X[0, 13:36], Y[0, 13:36], 'cyan', linewidth=3)
                
        #outer upper PFR
        axs[aa].plot(X[0, 49:62], Y[0, 49:62], 'tan', linewidth=3)
        axs[aa].plot(X[0, 62:85], Y[0, 62:85], 'teal', linewidth=3)


        #outer lower PFR
        axs[aa].plot(X[0, 85:], Y[0, 85:], 'lightgreen', linewidth=3)
        
        
        axs[aa].plot(X[-1, 1:13], Y[-1, 1:13], 'blue', linewidth=3)
        axs[aa].plot(X[-1, 13:36], Y[-1, 13:36], 'blue', linewidth=3)
        axs[aa].plot(X[-1, 36:48], Y[-1, 36:48], 'blue', linewidth=3)

        #outer SOL
        axs[aa].plot(X[-1, 49:62], Y[-1, 49:62], 'purple', linewidth=3)
        axs[aa].plot(X[-1, 62:85], Y[-1, 62:85], 'purple', linewidth=3)
        axs[aa].plot(X[-1, 85:], Y[-1, 85:], 'purple', linewidth=3)
        

            
        
        axs[aa].plot(X[18, 1:13], Y[18, 1:13], 'red', linewidth=1, linestyle='--')
        axs[aa].plot(X[18, 12:36], Y[18, 12:36], 'red', linewidth=1, linestyle='--')
        axs[aa].plot(X[18, 35:48], Y[18, 35:48], 'red', linewidth=1, linestyle='--')

        #outer SOL
        axs[aa].plot(X[18, 49:62], Y[18, 49:62], 'red', linewidth=1, linestyle='--')
        axs[aa].plot(X[18, 61:85], Y[18, 61:85], 'red', linewidth=1, linestyle='--')
        axs[aa].plot(X[18, 84:], Y[18, 84:], 'red', linewidth=1, linestyle='--')
        
    



   
        
        

    if plot_vessel:
        
        axs[aa].plot(vessel[:,0]/1000, vessel[:,1]/1000, color = 'black', linewidth = 2)

    else:
        pass

    axs[aa].set_xlabel("R: [m]")
    axs[aa].set_ylabel("Z: [m]")
    axs[aa].set_aspect('equal')
    

   