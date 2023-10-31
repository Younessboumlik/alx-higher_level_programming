#!/usr/bin/python3


def add_integer(a, b=98):
    if type(a) != int and  type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and  type(b) != float:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))                                                    
