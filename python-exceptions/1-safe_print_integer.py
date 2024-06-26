#!/usr/bin/python3
# 1-safe_print_integer.py


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
