"""
Firn depth models
Author: Cyril Grima <cyril.grima@gmail.com>
"""

import pandas as pd
from numpy.polynomial.polynomial import polyval
import scipy.constants as ct
import numpy as np



def density_kovacs82(d0, z):
    """Convert depth into firn density from Kovacs [1982]
    measurements over the brine of McMurdo Ice Shelf

    Arguments
    ---------
    d0 : float
        first polynom equals the surface density [kg^m{-3}]
    z : array of floats
        Depth [m]
    """ 

    p = {'B': [d0, 2.79e1, 0, 0, 0, 0, 0],
         'C': [d0, 2.21e1, -3.09e-1, 0, 0, 0, 0],
         'D': [d0, 2.38e1, -5.11e-1, 4.62e-3, 0, 0, 0],
         'E': [d0, 3.36e1, -1.89e00, 7.83e-2, -1.85e-3, 2.24e-5, -1.07e-7],
         'F': [d0, 3.57e1, -2.15e00, 8.77e-2, -1.94e-3, 2.15e-5, -9.54e-8]}
    p = pd.DataFrame(p)

    # Density caclcuation
    dns = {'B': z*0, 'C': z*0, 'D': z*0, 'E': z*0, 'F': z*0}
    dns = pd.DataFrame(dns)

    for i, val in enumerate(z):
        dns.ix[i] = polyval(val,p.ix[:])
    dns[dns > 917] = 917.
    return dns


def density_sorgelaw(d0, z, zt):
    """Convert depth into firn density from Sorge's law
    as reported by [Cuffey and Patterson, 2010, eq.2.2]

    Arguments
    ---------
    d0 : float
        surface density [kg^m{-3}]
    z : array of floats
        Depth [m]
    zp : float
        characteristic depth of firn
    """
    di = 917. # Density of ice    
    return di-(di-d0)*np.exp(-1.9*z/zt)
    
