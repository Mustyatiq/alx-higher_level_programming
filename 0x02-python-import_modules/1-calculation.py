#!/usr/bin/python3
import calculator_1 as calc


def main():
    a = 10
    b = 5
    print(a, " + ", b, " = ", calc.add(a, b))
    print(a, " - ", b, " = ", calc.sub(a, b))
    print(a, " * ", b, " = ", calc.mul(a, b))
    print(a, " / ", b, " = ", calc.div(a, b))


if __name__ == "__main__":
    main()
