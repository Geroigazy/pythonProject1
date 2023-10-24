
def sorting(a, b, c):
    """
    задача 6
    :param a:
    :param b:
    :param c:
    :return:
    """
    arr = [a, b, c]

    arr = sorted(arr)

    return f'{arr[0]} {arr[1]} {arr[2]}'


if __name__ == '__main__':
    print(sorting(1, 2, 1))
