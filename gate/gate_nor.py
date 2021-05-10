from .gate_not import NOT
from .gate_or import OR


def NOR(*x):
    return NOT( OR(*x) )