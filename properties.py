"""
Snow/Firn/Ice properties
Author: Cyril Grima <cyril.grima@gmail.com>
"""

import numpy as np

def perm_kovacs95(val, density=False):
    """Convert permittivity to/from density for dry snow
    from [Kovacs et al., 1995] 

    Arguments
    ---------
    val : float
        relative permittivity or density [kg.m^{-3}]

    Keywords
    --------
    density : bool
        wether or not the 'val' is a density 
    """
    if density is False:
        out = (np.sqrt(val)-1)/845e-6
    else:
        out = (1+845e-6*val)**2
    return out
