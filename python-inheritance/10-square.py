#!/usr/bin/python3
"""
Module that defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a square using Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Calculate the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return super().area()
