#!/usr/bin/python3
# 0-read_file.py


"""function that print text file in utf-8 format"""


def read_file(filename=""):
    """func that print text from other file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
