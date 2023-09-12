#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for number in my_list:
        print("{}".format(number))

print_reversed_list_integer([2, 6, 7, 8, 10])