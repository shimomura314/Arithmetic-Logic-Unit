from .gate_nand import NAND


def NOT(x):
    return NAND(x, x)