import adder
import gate


def substractor(x: list, y: list):
    x.extend([0]*(len(y)-len(x)))
    y.extend([0]*(len(x)-len(y)))
    y = gate.NOT(y)
    return adder.n_bit_adder(x, y, 1)[0]