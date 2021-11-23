"""
conway game of life.
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp

def conway(array,t):
    if array is None:
        grid_dim = (25,25)
        grid = np.random.randint(low=0, high=2,size=(grid_dim[0],grid_dim[1]))
    else:
        if isinstance(array,list):
            print('')
            grid = np.array(array)
        else:
            grid = array
        
        grid_dim = grid.shape
        
    filt = np.ones(shape=(3,3))
    filt[1,1] = 0

    nsteps = t
    grid_history = np.empty(shape=(nsteps+1,grid_dim[0],grid_dim[1]))
    grid_history[0,:,:] = grid
    
    for i in range(nsteps):
        neighbors = scp.convolve2d(grid, filt, mode='same', boundary='symm', fillvalue=0)

        overpop = np.where(neighbors>3)
        underpop = np.where(neighbors<2)
        reprod = np.where(neighbors==3)

        grid[overpop] = 0
        grid[underpop] = 1 
        grid[reprod] = 1

        grid_history[i+1,:,:] = grid
    return grid_history
