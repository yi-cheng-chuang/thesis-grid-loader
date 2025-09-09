# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 21:06:32 2025

@author: ychuang
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


fig, axs = plt.subplots(1, 2)



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
    'Inner target':'darkred',
    'Core boundary': 'cyan',
    'SOL boundary': 'blue',
    'Outer target': 'rosybrown',
    'Inner PFR boundary': 'green',
    'Outer PFR boundary': 'orange'
}

# Draw vertical lines
for x in range(width + 1):
    axs[0].axvline(x, color='gray', linewidth=0.3)

# Draw horizontal lines
for y in range(height + 1):
    axs[0].axhline(y, color='gray', linewidth=0.3)




axs[0].vlines(x=25, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[0].vlines(x=73, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[0].hlines(y=19, xmin=1, xmax=97, colors='red', linewidth=1, linestyle= '--')

# Add patches (rectangles) for each labeled region
# Lower half
axs[0].add_patch(patches.Rectangle((1, 0), inner_PFR_width, 1, 
                                   facecolor=colors['Inner PFR boundary'], edgecolor='none'))
axs[0].add_patch(patches.Rectangle((73, 0), outer_PFR_width, 1, 
                                   facecolor=colors['Outer PFR boundary'], edgecolor='none'))
axs[0].add_patch(patches.Rectangle((25, 0), core_width, 1, 
                                   facecolor=colors['Core boundary'], edgecolor='none'))
axs[0].add_patch(patches.Rectangle((0, 1), 1, height -2, facecolor=colors['Inner target'], edgecolor='none'))
axs[0].add_patch(patches.Rectangle((width -1, 1), 1, height -2, facecolor=colors['Outer target'], edgecolor='none'))


# Upper half
axs[0].add_patch(patches.Rectangle((1, height -1), simu_width, 1, facecolor=colors['SOL boundary'], edgecolor='none'))




# Set limits and remove axes
axs[0].set_xlim(0, width)
axs[0].set_ylim(0, height)
axs[0].set_aspect('equal')
axs[0].axis('off')





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
    'Inner bottom PFR boundary':'green',
    'Inner core boundary': 'cyan',
    'Inner SOL boundary': 'blue',
    'Inner top PFR boundary': 'orange',
    'Outer SOL boundary': 'purple',
    'Outer core boundary': 'teal',
    'Outer top PFR boundary': 'tan',
    'Outer bottom PFR boundary': 'lightgreen',
    'Inner bottom target': 'darkred',
    'Inner top target': 'rosybrown',
    'Outer top target': 'magenta',
    'Outer bottom target': 'slategray'
}

# Draw vertical lines
for x in range(width + 1):
    axs[1].axvline(x, color='gray', linewidth=0.3)

# Draw horizontal lines
for y in range(height + 1):
    axs[1].axhline(y, color='gray', linewidth=0.3)


axs[1].axvline(x= 49, color='black', linewidth=2, linestyle= '--')
axs[1].hlines(y=19, xmin=1, xmax=48, colors='red', linewidth=1, linestyle= '--')
axs[1].hlines(y=19, xmin=50, xmax=97, colors='red', linewidth=1, linestyle= '--')

axs[1].vlines(x=13, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=36, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=62, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')
axs[1].vlines(x=85, ymin=1, ymax=19, colors='black', linewidth=2, linestyle= '--')


# Add patches (rectangles) for each labeled region
# Lower half
axs[1].add_patch(patches.Rectangle((1, 0), bottom_PFR_width, 1, facecolor=colors['Inner bottom PFR boundary'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((13, 0), core_width, 1, facecolor=colors['Inner core boundary'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((36, 0), top_PFR_width, 1, facecolor=colors['Inner top PFR boundary'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((50, 0), top_PFR_width, 1, facecolor=colors['Outer top PFR boundary'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((62, 0), core_width, 1, facecolor=colors['Outer core boundary'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((85, 0), bottom_PFR_width, 1, facecolor=colors['Outer bottom PFR boundary'], edgecolor='none'))

# Upper half
axs[1].add_patch(patches.Rectangle((1, height -1), half_width, 1, facecolor=colors['Inner SOL boundary'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((50, height -1), half_width, 1, facecolor=colors['Outer SOL boundary'], edgecolor='none'))


#targets
axs[1].add_patch(patches.Rectangle((0, 1), 1, height -2, facecolor=colors['Inner bottom target'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((width -1, 1), 1, height -2, facecolor=colors['Outer bottom target'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((48, 1), 1, height -2, facecolor=colors['Inner top target'], edgecolor='none'))
axs[1].add_patch(patches.Rectangle((49, 1), 1, height -2, facecolor=colors['Outer top target'], edgecolor='none'))


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











