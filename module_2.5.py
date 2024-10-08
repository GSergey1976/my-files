def get_matrix (n,m,value):
# n-строки
# m-столбцы
# value-значения
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)

n = int(input('Задайте количество строк матрицы   : '))
m = int(input('Задайте количество столбцов матрицы: '))
value = input(f'Задайте значение матрицы: ')
get_matrix (2,4,3)








