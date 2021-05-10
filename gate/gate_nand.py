import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([-1, -1])
    bias = 1.5
    temporary = np.sum( x*weight ) + bias
    if temporary <= 0:
        return 0
    return 1