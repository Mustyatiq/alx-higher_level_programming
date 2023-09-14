#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        largest = [None, 0]
        for x, y in a_dictionary.items():
            if largest[1] < y:
                largest = [x, y]
        return largest[0]
    else:
        return None
