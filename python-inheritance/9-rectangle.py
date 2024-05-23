#!/usr/bin/python3
"""
Module that defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represent a rectangle using BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
