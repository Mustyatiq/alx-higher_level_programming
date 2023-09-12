#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for number in range(len(new_list)):
        if new_list[number] % 2 == 0:
            new_list[number] = True
        else:
            new_list[number] = False
    return new_list
