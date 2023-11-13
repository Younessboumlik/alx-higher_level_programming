#!/usr/bin/python3
"""the base of our project."""


class Base:
    """the base class in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """the init method."""
        if id is not in None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
