

def compare(a, b):
    """
    задача 3
    :param a:
    :param b:
    :return:
    """
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return 2


if __name__ == '__main__':
    a = input()
    b = input()

    print(compare(a, b))


