#!/usr/bin/python3
# 4-only_diff_elements.py


def only_diff_elements(set_1, set_2):
    valuediff = [value for value in set_1 if value not in set_2] + \
                [value for value in set_2 if value not in set_1]
    return valuediff
