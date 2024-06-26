#!/usr/bin/python3


"""Write a function that writes a string to a text file (UTF8)
   and returns the number of characters written"""


def write_file(filename="", text=""):
    """open the text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        """write or create the file"""
        return f.write(text)
