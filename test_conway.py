"""
test conway.py.
"""

import conway as cw
import numpy as np


def test_conway():
    """
        Test conway
    """
    nsteps = 10
    oscillator_init = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
    game = cw.conway(array=oscillator_init,t=nsteps)
    oscillator_state1 = game[0::2,:,:]
    oscillator_state2 = game[1::2,:,:]
    if len(oscillator_state1) != len(oscillator_state2):
        start=1
    else:
        start=0
    print(oscillator_state1.shape,oscillator_state2.shape)
    comparisson = oscillator_state1[start::,:,:] == oscillator_state2.transpose(0,2,1)
    assert(comparisson.all())

