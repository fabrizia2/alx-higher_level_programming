#!/usr/bin/python3
"""
The inheritance from class Rectangle process.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square"""

    def __init__(self, size):
        """Initialise an instance of the class Square"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
