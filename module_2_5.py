def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return  matrix
n = int(input('Задайте количество строк: '))
m = int(input('Задайте количество столбцов: '))
value = int(input('Задайте значение: '))
print(get_matrix(n,m,value))