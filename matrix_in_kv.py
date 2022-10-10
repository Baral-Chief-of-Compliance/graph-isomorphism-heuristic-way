def kv_m(matrix):

    length = len(matrix)
    result_matrix = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result_matrix[i][j] += matrix[i][k] * matrix[k][j]

    return result_matrix