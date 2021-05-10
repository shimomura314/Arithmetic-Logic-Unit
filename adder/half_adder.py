import gate


def half_adder(x: int, y: int):
    sumation = gate.XOR(x, y)
    carry_out = gate.AND(x, y)
    return sumation, carry_out