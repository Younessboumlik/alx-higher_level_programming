#!/usr/bin/python3
"""
reading a file.
"""
def read_file(filename=""):
    """print the content of filename."""
    with open(filename,encoding="utf-8") as f
        print(f.read())
    f.close()
