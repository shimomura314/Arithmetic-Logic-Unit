from .gate_and import AND
from .gate_nand import NAND
from .gate_or import OR


def XOR(x1, x2):
    return AND(OR(x1, x2), NAND(x1, x2))