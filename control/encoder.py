__all__ = ["encoder"]


def bit_length(*x: list):
    MAX_LENGTH = 0
    for e in x:
        MAX_LENGTH = max(MAX_LENGTH, len(e))
    corrected = []
    for e in x:
        e.extend([0]*(MAX_LENGTH-len(e))) 
        corrected.append(e)
    return corrected


def int_to_bit(x: int) -> list:
    return list(map(int, reversed(list(bin(x))[2:])))


def encoder(*x: int):
    encoded = []
    for e in x:
        encoded.append(int_to_bit(e))
    return bit_length(*encoded)