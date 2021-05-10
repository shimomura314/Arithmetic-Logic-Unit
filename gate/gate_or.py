import numpy as np


def OR(*x):
    x = np.array(x)
    weight = np.ones(len(x))
    bias = -0.5
    temporary = np.sum( x*weight ) + bias
    if temporary <= 0:
        return 0
    return 1