# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 12:34:05 2025

@author: ychuang
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

# Grid size (based on your image)
nx, ny = 98, 38
x = np.arange(nx + 1)
y = np.arange(ny + 1)

# Create meshgrid for vertices
X, Y = np.meshgrid(x, y)

# Dummy region label map (replace with your actual mapping)
region_map = np.full((ny, nx), 'core')  # default
region_map[ny//2:, :] = 'SOL'
# region_map[3*ny//4:, :] = 'divertor'

# Define colors
region_colors = {
    "core": "lavender",
    "SOL": "deepskyblue",
    "divertor": "orange"
}

# Build polygons
polys = []
colors = []

for j in range(ny):
    for i in range(nx):
        verts = [
            (X[j, i], Y[j, i]),
            (X[j+1, i], Y[j+1, i]),
            (X[j+1, i+1], Y[j+1, i+1]),
            (X[j, i+1], Y[j, i+1])
        ]
        polys.append(verts)
        colors.append(region_colors[region_map[j, i]])

# Plot it
fig, ax = plt.subplots()
collection = PolyCollection(polys, facecolors=colors, edgecolors='gray', linewidths=0.1)
ax.add_collection(collection)

ax.set_xlim(0, nx)
ax.set_ylim(0, ny)
ax.set_aspect('equal')
ax.axis('off')
plt.show()
