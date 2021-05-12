import adder
import control
import gate
import subtractor


def ALU74381(a: int, b: int, s1: int, s2: int, s3: int):
    a, b = control.encoder(a, b)
    if not s1 and not s2 and not s3:
        return [0] * max(len(a), len(b))
    if not s1 and not s2 and s3:
        return subtractor.substractor(b, a)
    if not s1 and s2 and not s3:
        return subtractor.substractor(a, b)
    if not s1 and s2 and s3:
        return adder.n_bit_adder(a,b)[0]
    if s1 and not s2 and not s3:
        result = [0] * len(a)
        for index in range(len(a)):
            result[index] = gate.XOR( a[index],b[index] )
        return result
    if s1 and not s2 and s3:
        result = [0] * len(a)
        for index in range(len(a)):
            result[index] = gate.OR( a[index],b[index] )
        return result
    if s1 and s2 and not s3:
        result = [0] * len(a)
        for index in range(len(a)):
            result[index] = gate.AND( a[index],b[index] )
        return result
    if s1 and s2 and s3:
        return [1] * max(len(a), len(b))