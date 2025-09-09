# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 16:19:55 2025

@author: ychuang
"""


import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

# Set up GridSpec layout
fig = plt.figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[1.5, 3])  # Slightly wider for legend

# Create subplots
ax1 = fig.add_subplot(gs[0])
legend_ax = fig.add_subplot(gs[1])

# Turn off axes for legend box
legend_ax.axis('off')


DEV = 'mastu'
as_boundary = False

# Define color mapping

if DEV == 'mast':
    
    colors = {
        'Inner PFR':'green',
        'Core': 'cyan',
        'SOL': 'blue',
        'Outer PFR': 'orange',
    }
    

elif DEV == 'mastu':
    
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
    
    

        
    
# Create custom legend elements
legend_elements = [Patch(facecolor=c, label=l) for l, c in colors.items()]


# Make a dashed handle with an explicit dash pattern (on = 4pt, off = 2pt)
gridcut_handle = Line2D([0], [0],
                        color='black',
                        lw=1.5,
                        linestyle=(0, (4, 2)),   # ensures visible dashes
                        dash_capstyle='butt',     # cleaner gaps
                        label='Grid cut')
legend_elements.append(gridcut_handle)

# Red dashed line for Separatrix
separatrix_handle = Line2D([0], [0],
                           color='red',
                           lw=1.5,
                           linestyle=(0, (4, 2)),  # same dash pattern
                           dash_capstyle='butt',
                           label='Separatrix')
legend_elements.append(separatrix_handle)



# Add flat-style legend to dedicated subplot
legend_ax.legend(
    handles=legend_elements,
    loc='center',
    ncol=4,                     # Flatten horizontally
    fontsize=9,
    frameon=True,
    handlelength=1.2,
    handleheight=0.6,
    handletextpad=0.4,
    columnspacing=1.0
)


