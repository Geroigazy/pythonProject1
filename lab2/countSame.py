

def counting(a, b, c):
    """
    задача 5
    :param a:
    :param b:
    :param c:
    :return:
    """
    if a == b and b == c:
        return 3
    elif a != b and b != c:
        return 0
    else:
        return 1


if __name__ == '__main__':
    print(counting(4, 4, 4))