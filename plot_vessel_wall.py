# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 17:09:38 2025

@author: ychuang
"""

from shapely.geometry import MultiPoint
from shapely.geometry.polygon import Polygon
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np


# Suppose x and y are your unordered boundary points
points = np.loadtxt('vvfile.ogr')  # or wherever you load data
x = points[:, 0]
y = points[:, 1]



# Plot
plt.figure()

plt.plot(x, y, color = 'black', linewidth = 2)
plt.gca().set_aspect('equal')
plt.title("MAST-U vessel")
plt.show()
