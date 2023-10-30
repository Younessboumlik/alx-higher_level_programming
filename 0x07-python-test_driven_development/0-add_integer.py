#!/usr/bin/env python3


def add_integer(a, b=98):
    """
    Adds two integers.

    >>> add_integer(1, 1)
    2

    >>> add_integer(5, 5)
    10
    """
    if type(a) != int and  type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and  type(b) != float:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
