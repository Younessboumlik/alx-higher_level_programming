#!/usr/bin/python3
"""Represent a square."""

class Square:
    """Represent a square."""
    def __init__(self, size=0):
       """Initialize a new Square.
       Args:
       size (int): The size of the new square.
       """
       if not  isinstance(size, int):
        raise TypeError("size must be an integer")
       elif size < 0:
        raise ValueError("size must be >= 0")
       else :
         self.__size = size 
    
    def area(self):
      """Return the current area of the square."""
      return (self.__size * self.__size)
    
    @property
    def size(self):
      """
      Getter method for the size property.
      Returns:
      int: The current size of the object.
      """
      return self.__size  
    @size.setter
    def size(self, value):
      """
      Setter method for the size property.
      Args:
      value (int): The new size value.
      Raises:
      ValueError: If the value is not a non-negative integer."""
      if not  isinstance(value, int):
        raise TypeError("size must be an integer")
      elif value < 0:
        raise ValueError("size must be >= 0")
      else :
         self.__size = value