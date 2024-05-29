#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Iniciamos el triángulo con la primera fila

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Cada nueva fila comienza con 1
        # Construimos los elementos de la nueva fila
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Cada nueva fila termina con 1
        triangle.append(new_row)

    return triangle
