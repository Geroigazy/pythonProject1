

def root(a, b, c):
    discrement = b**2 - 4 * a * c

    if discrement>0:
        x1 = (-b + discrement**0.5) / 2 * a
        x2 = (-b - discrement**0.5) / 2 * a
        return x1, x2
    elif discrement == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        pass


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())

    print(root(a, b, c))


