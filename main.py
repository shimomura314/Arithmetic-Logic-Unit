import gate
import adder


def gate_checker():
    for x in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        y = gate.AND(*x)
        print("AND : " + str(x) + " -> " + str(y))
    for x in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        y = gate.NAND(*x)
        print("NAND : " + str(x) + " -> " + str(y))
    for x in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        y = gate.OR(*x)
        print("OR : " + str(x) + " -> " + str(y))
    for x in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        y = gate.XOR(*x)
        print("XOR : " + str(x) + " -> " + str(y))


def adder_checker():
    for x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = adder.half_adder(*x)
        print("%s + %s = %s carry %s" %(x[0], x[1], y[0], y[1]))
    for x in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        y = adder.full_adder(*x)
        print("%s + %s + %s = %s carry %s" %(x[0], x[1], x[2], y[0], y[1]))


if __name__ == "__main__":
    adder_checker()