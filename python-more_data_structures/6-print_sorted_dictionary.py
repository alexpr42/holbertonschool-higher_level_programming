#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    sorted_keys = (a_dictionary.keys())
    for key in sorted_keys:
        print("{}:, {}".format(key, a_dictionary[key]))
