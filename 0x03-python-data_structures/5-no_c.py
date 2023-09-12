#!/usr/bin/python3
def no_c(my_string):
    buff = list(my_string)
    for character in buff:
        if character == 'c' or character == 'C':
            buff.remove(character)
    return "".join(buff)
