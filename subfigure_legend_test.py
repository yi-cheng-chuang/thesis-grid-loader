# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 16:19:55 2025

@author: ychuang
"""


import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import matplotlib.gridspec as gridspec

# Set up GridSpec layout
fig = plt.figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[1.5, 3])  # Slightly wider for legend

# Create subplots
ax1 = fig.add_subplot(gs[0])
legend_ax = fig.add_subplot(gs[1])

# Turn off axes for legend box
legend_ax.axis('off')

# Define color mapping
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


