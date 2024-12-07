import re

import numpy as np

def transform_to_matrix(string_input: str):
    matrix = np.array([list(row) for row in string_input.strip().split('\n')])
    return matrix

def search_xmas(matrix):
    for i in range(0, matrix.shape[1]):
        row_list = matrix[i, :]
        row_str = "".join(row_list)
        r = re.findall(r"XMAS", row_str)
        print(f"Row #{i}:{r}")


with open('test_input.txt', 'r') as file:
    inp = file.read()
# print(inp)
m = transform_to_matrix(inp)

# print(m)
# print(m[0, :])
# print(m.shape)
search_xmas(m)
