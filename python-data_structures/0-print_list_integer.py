#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print all integers as strings"""
    for num in my_list:
        print(str.format("{}", num))
