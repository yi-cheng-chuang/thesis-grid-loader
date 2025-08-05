# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 12:05:47 2025

@author: ychuang
"""

import matplotlib.pyplot as plt
import numpy as np



# Set grid size
cols = 98
rows = 38

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






fig, ax = plt.subplots()

# Draw vertical lines
for x in range(cols + 1):
    ax.axvline(x, color='lightgray', linewidth= 0.5)

for y in inner_r:
    
    for x in in_top_p:
        ax.axvline(x, color='orange', linewidth= 0.5)
        ax.axhline(y, color='orange', linewidth= 0.5)

for y in inner_r:
    
    for x in in_core_p:
        ax.axvline(x, color='cyan', linewidth= 0.5)
        ax.axhline(y, color='cyan', linewidth= 0.5)

for y in inner_r:
    
    for x in in_bottom_p:
        ax.axvline(x, color='green', linewidth= 0.5)
        ax.axhline(y, color='green', linewidth= 0.5)

for y in inner_r:
    
    for x in out_top_p:
        ax.axvline(x, color='tan', linewidth= 0.5)
        ax.axhline(y, color='tan', linewidth= 0.5)


for y in inner_r:
    
    for x in out_core_p:
        ax.axvline(x, color='teal', linewidth= 0.5)
        ax.axhline(y, color='teal', linewidth= 0.5)

for y in inner_r:
    
    for x in out_bottom_p:
        ax.axvline(x, color='lightgreen', linewidth= 0.5)
        ax.axhline(y, color='lightgreen', linewidth= 0.5)




# Draw horizontal lines
for y in outer_r:
    
    for x in inner_p:
        ax.axvline(x, color='blue', linewidth= 0.5)
        ax.axhline(y, color='blue', linewidth= 0.5)


for y in outer_r:
    
    for x in outer_p:
        ax.axvline(x, color='purple', linewidth= 0.5)
        ax.axhline(y, color='purple', linewidth= 0.5)   
    
    
# Set axis limits
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)

# Set equal aspect ratio
ax.set_aspect('equal')

# Optional: remove ticks
# ax.set_xticks([])
# ax.set_yticks([])

# plt.title("96x36 Grid")
# plt.show()