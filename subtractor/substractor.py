import adder
import gate


def substractor(x: list, y: list):
    y = gate.NOT(y)
    return adder.n_bit_adder(x, y, 1)[0]