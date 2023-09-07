#!/usr/bin/python3
def pow(a, b):
    "a function that computes a to the power of b and return the value."
    if b == 0:
        return 1
    elif b > 0:
        return a * pow(a, b - 1)
    else:
        return (1 / a) * pow(a, b + 1)
