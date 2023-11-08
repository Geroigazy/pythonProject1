import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def power(a, b):
    return a ** b


def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


def main():
    while True:
        print("Available options:")
        print("1. a + b")
        print("2. a - b")
        print("3. a * b")
        print("4. a / b")
        print("5. a ** b")
        print("6. Fibonacci number")
        print("7. Exit")
        try:
            choice = input("Enter option: ")

            if choice == '7':
                print("Exiting the calculator. Goodbye!")
                return False

            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid option. Please choose a valid option (1-7).")
                continue

            if choice == '1':
                a = float(input("insert a: "))
                b = float(input("insert b: "))
                result = add(a, b)
            elif choice == '2':
                a = float(input("insert a: "))
                b = float(input("insert b: "))
                result = subtract(a, b)
            elif choice == '3':
                a = float(input("insert a: "))
                b = float(input("insert b: "))
                result = multiply(a, b)
            elif choice == '4':
                a = float(input("insert a: "))
                b = float(input("insert b: "))
                result = divide(a, b)
            elif choice == '5':
                a = float(input("insert a: "))
                b = float(input("insert b: "))
                result = power(a, b)
            elif choice == '6':
                a = int(input("insert a: "))
                result = fibonacci(int(a))

            print("Result:", result)
        except ValueError:
            print("Invalid input. Please write integer, not string!")
            continue


if __name__ == '__main__':
    main()
