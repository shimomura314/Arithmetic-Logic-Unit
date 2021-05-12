from .full_adder import full_adder


def n_bit_adder(x: list, y: list, carry_in=0):
    sumation = [0]*len(x)
    for index in range(len(x)):
        sumation[index], carry_in = full_adder(x[index], y[index], carry_in)
    return sumation, carry_in