import numpy as np

from .gate_nand import NAND


def NOT(*x):
    for index in range(len(x[0])):
        x[0][index] = NAND(x[0][index], x[0][index])
    return x[0]