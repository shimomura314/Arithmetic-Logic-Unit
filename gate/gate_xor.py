from .gate_and import AND
from .gate_nand import NAND
from .gate_or import OR


def XOR(*x):
    if sum(x)%2 == 1:
        return 1
    return 0