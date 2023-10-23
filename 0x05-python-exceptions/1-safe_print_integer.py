#!/usr/bin/python3
def safe_print_integer(value):
    """function that print a value."""
    try:
        print("{:d}".format(value))
        return(True)
    except Exception:
        return(False)