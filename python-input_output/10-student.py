#!/usr/bin/python3
"""Define the Student class."""


class Student:
    """class student."""

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict rep of a Student.

        Args:
            attrs (list): A list of strings specifying the
            attributes to retrieve.
            If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary containing the
            specified attributes of the Student instance.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
