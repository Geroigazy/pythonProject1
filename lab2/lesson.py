

def endOfLesson(a: int):
    """
    задача 2
    :param a:
    :return:
    """
    short = a // 2
    long = (a-1) // 2

    total = a * 45 + short*5 + long*15

    hours = total // 60
    minutes = total % 60

    return f'{9 + hours:02d} {minutes:02d}'


if __name__ == '__main__':
    print(endOfLesson(2))
