#!/usr/bin/python3
def max_integer(my_list=[]):
    greatest = 0
    if len(my_list) == 0:
        return None
    for number in my_list:
        if greatest < number:
            greatest = number
    return greatest
