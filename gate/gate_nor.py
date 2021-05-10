from .gate_not import NOT
from .gate_or import OR


def NOR(x1, x2):
    return NOT( OR(x1, x2) )