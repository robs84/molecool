'''
This module is for functions that perform measurements.
'''


import numpy as np



def calculate_distance(rA, rB):

    '''
    Calculate the distance between two points.

    Parameters
    -----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    ------------
    distance : float
        The distance between the two points.

    Examples
    ------------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r1 = np.array([0.0, 0.0, 1.0])
    >>> calculate_distance(r1, r2)
    1.0

    '''


    # This function calculates the distance between two points given as numpy arrays.

    #if isinstance(rA, np.ndarray) is False or isinstance(rB, ndarray) is False:
        #raise TypeError("rA and rB must be numpy arrays")

    dist_vec=(rA-rB)
    distance=np.linalg.norm(dist_vec)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
