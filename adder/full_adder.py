import gate


def full_adder(x: int, y: int, carry_in: int):
    sumation = gate.XOR(x, y, carry_in)
    carry_out = gate.OR( gate.AND(x, y), gate.AND(x, carry_in), gate.AND(y, carry_in) )
    return sumation, carry_out