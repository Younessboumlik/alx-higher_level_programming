#!/usr/bin/python3

def best_score(a_dictionary):
    if not (a_dictionary):
        return None
    max = 0
    name = ""
    for i in a_dictionary:
        if (a_dictionary[i] > max):
            name = i
            max = a_dictionary[i]
    return name
