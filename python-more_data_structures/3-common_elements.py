#!/usr/bin/python3
# 3-common_elements.py


def common_elements(set_1, set_2):
    common = (value for value in set_1 if value in set_2)
    return common
