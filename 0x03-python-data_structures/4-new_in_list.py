#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        buff = my_list.copy()
        buff[idx] = element
        return buff