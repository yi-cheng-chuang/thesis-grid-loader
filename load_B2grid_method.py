# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 15:56:00 2025

@author: ychuang
"""

from os import path
import numpy as np

def read_b2fgmtry(fname):
    if not path.exists(fname):
        print('ERROR: b2fgmtry file not found:',fname)
        return None

    data = []
    with open(fname, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):

        # Special handling for first few lines
        if i == 0:
            version = line.split()[0][7:-1]
            geo = {'version':version}
            continue
        elif i == 1:
            continue
        elif i == 2:
            # Assume starts with nx,ny after version
            geo['nx'] = int(line.split()[0])
            geo['ny'] = int(line.split()[1])
            numcells = (geo['nx']+2)*(geo['ny']+2)
            continue

        if line.split()[0] == '*cf:':
            vartype = line.split()[1]
            varsize = int(line.split()[2])
            varname = line.split()[3]
            # Some variables have no entries depending on config
            if varsize == 0:
                geo[varname] = None
            data = []
        else:
            # Parse by type
            if vartype == "char":
                geo[varname] = line.strip()
            else:
                splitline = line.split()
                for value in splitline:
                    if vartype == "int":
                        data.append(int(value))
                    else:
                        data.append(float(value))

                if len(data) == varsize:
                    if varsize%numcells == 0:
                        geo[varname] = np.array(data).reshape([geo['nx']+2,geo['ny']+2,int(varsize/numcells)], order = 'F')
                    else:
                        geo[varname] = np.array(data)
                        

    return geo




def calcgrid_method(geo):
    
    pol_range = int(geo['nx'] + 2)
    rad_range = int(geo['ny'] + 2)
    psival = np.zeros((rad_range, pol_range))
    
    # Assuming you have four 98x38 matrices stored in variables

    # Replace these with your actual matrices or generate them as needed
    
    crLowerLeft = geo['crx'][:,:,0]
    crLowerRight = geo['crx'][:,:,1]
    crUpperLeft = geo['crx'][:,:,2]
    crUpperRight = geo['crx'][:,:,3]
    czLowerLeft = geo['cry'][:,:,0]
    czLowerRight = geo['cry'][:,:,1]
    czUpperLeft = geo['cry'][:,:,2]
    czUpperRight = geo['cry'][:,:,3]
    
    
    # Create a list of matrices
    crx_collect = [crLowerLeft, crLowerRight, crUpperLeft, crUpperRight]
    cry_collect = [czLowerLeft, czLowerRight, czUpperLeft, czUpperRight]
    
    # Convert the list of matrices to a NumPy array
    crx_array = np.array(crx_collect)
    cry_array = np.array(cry_collect)
    
    # Calculate the average along the first axis (axis=0) to get the desired matrix
    rad_mean = np.mean(crx_array, axis = 0)
    vert_mean = np.mean(cry_array, axis = 0)
    
    
    rad_loc = rad_mean.transpose()
    vert_loc = vert_mean.transpose()
    
            
    return rad_loc, vert_loc


def load_vessel_method(self, fdir):
    # try:
    #     WallFile = np.loadtxt('{}/mesh.extra'.format(self.data['dirdata']['tbase']))
    # except:
    #     print('mesh.extra file not found! Using vvfile.ogr instead')
    #     WallFile=None
    
    try:
        VVFILE = np.loadtxt('{}/baserun/vvfile.ogr'.format(fdir))
    except:
        print('load_vessel_method has a bug!')

    return VVFILE