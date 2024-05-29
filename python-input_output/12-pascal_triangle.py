#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """funtion that creat a pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]  # triangle initiation

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # new row
        # new row contruction
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # add to new lilne
        triangle.append(new_row)

    return triangle
