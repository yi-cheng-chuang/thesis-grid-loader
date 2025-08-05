# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 16:40:06 2025

@author: ychuang
"""



import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots()

# Define rectangle width and height
width = 98
height = 38

half_width = 49

half_height = 19
bottom_PFR_width = 13
core_width = 24
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
    ax.axvline(x, color='gray', linewidth=0.3)

# Draw horizontal lines
for y in range(height + 1):
    ax.axhline(y, color='gray', linewidth=0.3)


ax.axvline(49, color='black', linewidth=2, linestyle= '--')

ax.vlines(x=13, ymin=0, ymax=19, colors='black', linewidth=2, linestyle= '--')
ax.vlines(x=37, ymin=0, ymax=19, colors='black', linewidth=2, linestyle= '--')
ax.vlines(x=61, ymin=0, ymax=19, colors='black', linewidth=2, linestyle= '--')
ax.vlines(x=85, ymin=0, ymax=19, colors='black', linewidth=2, linestyle= '--')

# Add patches (rectangles) for each labeled region
# Lower half
ax.add_patch(patches.Rectangle((0, 0), bottom_PFR_width, half_height, facecolor=colors['Inner bottom PFR'], edgecolor='none'))
ax.add_patch(patches.Rectangle((13, 0), core_width, half_height, facecolor=colors['Inner core'], edgecolor='none'))
ax.add_patch(patches.Rectangle((37, 0), top_PFR_width, half_height, facecolor=colors['Inner top PFR'], edgecolor='none'))
ax.add_patch(patches.Rectangle((49, 0), top_PFR_width, half_height, facecolor=colors['Outer top PFR'], edgecolor='none'))
ax.add_patch(patches.Rectangle((61, 0), core_width, half_height, facecolor=colors['Outer core'], edgecolor='none'))
ax.add_patch(patches.Rectangle((85, 0), bottom_PFR_width, half_height, facecolor=colors['Outer bottom PFR'], edgecolor='none'))

# Upper half
ax.add_patch(patches.Rectangle((0, half_height), half_width, half_height, facecolor=colors['Inner SOL'], edgecolor='none'))
ax.add_patch(patches.Rectangle((49, half_height), half_width, half_height, facecolor=colors['Outer SOL'], edgecolor='none'))

# Add text labels
# ax.text(1.5, 0.5, 'Core', ha='center', va='center', fontsize=12)
# ax.text(1.5, 1.5, 'SOL', ha='center', va='center', fontsize=12)
# ax.text(0.5, 0.5, 'Inner divertor', ha='center', va='center', rotation='vertical', fontsize=12)
# ax.text(2.5, 0.5, 'Outer divertor', ha='center', va='center', rotation='vertical', fontsize=12)





# Set limits and remove axes
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')
ax.axis('off')

# Show plot
plt.show()