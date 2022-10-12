#!/usr/bin/python3

""" Square representor """


class Square:
    """ Defines the class of square """

    def __init__(self, size=0):
        self.size = size

    @property
    """ to retrieve it """
    def size(self):
        return self.__size

    @property.setter
    """ to set it """
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
