# Проверить, все ли строки матрицы содержат хотя бы один положительный элемент.
# Если да, то изменить знаки всех элементов матрицы на обратные.

def positive_element(row):
    for element in row:
        if element > 0:
            return True
    return False


def modify_row(row):
    modified_row = [-element for element in row]
    return modified_row


def matrix(matrix):
    for row in matrix:
        if positive_element(row):
            row[:] = modify_row(row)


created_matrix = [
    [1, -2, 3],
    [-4, -5, -6],
    [7, -8, -9]
]

matrix(created_matrix)

for row in (created_matrix):
    print(row)
