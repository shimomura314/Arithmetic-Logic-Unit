__all__ = ["decoder"]


def decoder(x: list) -> int:
    x = int(str("0b" + "".join(reversed(list(map(str, x))))), 2)
    return x