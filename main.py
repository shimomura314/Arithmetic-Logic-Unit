import gate


for x in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = gate.AND(*x)
    print("AND : " + str(x) + " -> " + str(y))
for x in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = gate.NAND(*x)
    print("NAND : " + str(x) + " -> " + str(y))
for x in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = gate.OR(*x)
    print("OR : " + str(x) + " -> " + str(y))
for x in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = gate.XOR(*x)
    print("XOR : " + str(x) + " -> " + str(y))