def generate_array(n):
    # создаем пустой массив нужного размера
    arr = [[0 for j in range(n)] for i in range(n)]
    # заполняем главную диагональ
    for i in range(n):
        arr[i][i] = i
    # заполняем диагонали выше главной
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j] = arr[i][j-1] + n - (j - i) + 1 
    # заполняем диагонали ниже главной
    for i in range(1, n):
        for j in range(i):
            arr[i][j] = 0
    return arr

# пример использования
n = int(input())
arr = generate_array(n)
for row in arr:
    print(row)
