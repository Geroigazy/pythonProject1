

def maxx(a, b, c):
    """
    задача 4
    :param a:
    :param b:
    :param c:
    :return:
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return c


if __name__ == '__main__':
    a = input()
    b = input()
    c = input()
    print(maxx(a, b, c))
