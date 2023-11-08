#!/usr/bin/python3
"""writes a string to a text."""


def write_file(filename="", text=""):
    """write the content in the file."""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
