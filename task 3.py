def get_matrix(n, m, value):
    # n-строки
    # m-столбцы
    # value-значения
    matrix = []

    for i in range(n):

        if n == 0:

            continue
            print(input('Введите другое число', n))
        else:
            matrix.append([i])
    for j in range(m):
        if m == 0:
            m = input('Введите другое число', n)
        else:
            matrix[i].append(value)
    print(matrix)
    return matrix


result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)

# result3 = get_matrix(4, 2, 13)
