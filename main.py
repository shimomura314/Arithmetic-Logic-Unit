import adder
import alu
import control
import gate
import subtractor

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
    print(adder.n_bit_adder([0,1,0,1,0,1], [0,1,1,1]))
    print(subtractor.substractor([0,1,0,1,0,1], [0,1,1,1,1,1]))


def ALU_checker():
    for x,y in ([15,31], [123, 642], [12, 543]):
        for s1, s2, s3 in (
            [0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0 ,0],
            [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1],
            ):
            if not s1 and not s2 and not s3:
                print("0000")
            if not s1 and not s2 and s3:
                print("%d - %d = %d" %(y, x, control.decoder(alu.ALU74381(x, y, s1, s2 ,s3))))
            if not s1 and s2 and not s3:
                print("%d - %d = %d" %(x, y, control.decoder(alu.ALU74381(x, y, s1, s2 ,s3))))
            if not s1 and s2 and s3:
                print("%d + %d = %d" %(x, y, control.decoder(alu.ALU74381(x, y, s1, s2 ,s3))))
            if s1 and not s2 and not s3:
                print("%d ^ %d = %d" %(x, y, control.decoder(alu.ALU74381(x, y, s1, s2 ,s3))))
            if s1 and not s2 and s3:
                print("%d | %d = %d" %(x, y, control.decoder(alu.ALU74381(x, y, s1, s2 ,s3))))
            if s1 and s2 and not s3:
                print("%d & %d = %d" %(x, y, control.decoder(alu.ALU74381(x, y, s1, s2 ,s3))))
            if s1 and s2 and s3:
                print("1111")
    return


def main():
    return


if __name__ == "__main__":
    # gate_checker()
    # adder_checker()
    ALU_checker()