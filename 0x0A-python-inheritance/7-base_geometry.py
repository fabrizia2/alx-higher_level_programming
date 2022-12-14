#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """public instance method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
