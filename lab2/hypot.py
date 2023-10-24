from math import sqrt


def pifogor(a: int, b: int) -> float:
    """
    задача 1
    :param a:
    :param b:
    :return:
    """
    return sqrt(float(a**2 + b**2))


if __name__ == '__main__':
    print(pifogor(6, 8))
