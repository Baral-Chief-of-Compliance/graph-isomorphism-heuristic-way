from matrix_in_kv import kv_m


def change_row(n, matrix, row_n, row_n_1):
    for j in range(len(matrix)):
        matrix[j][n]=row_n_1[j]
        matrix[j][n+1]=row_n[j]
    print('\n\nматрица в change_row:')
    print(matrix)
    return matrix


def matrix_rebuild(matrix_v2):
    for i in range(len(matrix_v2)-1):
        if matrix_v2[i][i] < matrix_v2[i+1][i+1]:
            memory_list = matrix_v2[i]
            print('\n\nmemory list:')
            print(memory_list)
            matrix_v2[i] = matrix_v2[i+1]
            matrix_v2[i+1] = memory_list
            memory_list_row_i = [row[i] for row in matrix_v2]
            memory_list_row_i_1 = [row[i + 1] for row in matrix_v2]
            print('\n\nmemory_list_row_i')
            print(memory_list_row_i)
            print('\n\nmemory_list_row_i_1')
            print(memory_list_row_i_1)
            print('\n\nматрица до change row:')
            print(matrix_v2)
            matrix_v2 = change_row(i, matrix_v2, memory_list_row_i, memory_list_row_i_1)
    return matrix_v2


def make_diagonal(matrix):
    diag = [matrix[i][i] for i in range(len(matrix))]
    return diag


def check_diagonal(matrix1, matrix2, counter):
    diag_1 = make_diagonal(matrix1)
    print('\n\nдиагоноль первой матрицы')
    print(diag_1)

    diag_2 = make_diagonal(matrix2)
    print('\n\nдиагоноль второй матрицы')
    print(diag_2)

    if counter == 10:
        print('\n\nматрицы являются изоморфными')
    elif diag_2 == diag_1:
        counter += 1
        algorithm(matrix1, matrix2, counter)
    else:
        print('\n\nматрицы не являются изоморфными')


def algorithm(adj_m1, adj_m2, counter):

    adj_m1_v2 = kv_m(adj_m1)
    print('\n\nквадарат матрицы 1:')
    print(adj_m1_v2)

    adj_m2_v2 = kv_m(adj_m2)
    print('\n\nквадрат матрицы 2:')
    print(adj_m2_v2)

    adj_m1_v2 = matrix_rebuild(adj_m1_v2)

    print(f'\n\nматрица 1 на прогоне {counter} :')
    print(adj_m1_v2)

    adj_m2_v2 = matrix_rebuild(adj_m2_v2)

    print(f'\n\nматрица 2 на прогоне {counter}:')
    print (adj_m2_v2)

    check_diagonal(adj_m1_v2, adj_m2_v2, counter)