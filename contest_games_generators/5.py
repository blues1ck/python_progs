'''
Наташа и Петя любят играть в следующую игру на лекциях по теории сложности. Они рисуют неориентированный двудольный граф G на листе бумаги
и ставят фишку в одну из его вершин. После этого они делают ходы по очереди, Наташа ходит первой.
Ход в игре заключается в том, что фишка перемещается по графу вдоль одного из ребер.
После хода вершина, в которой фишка находилась перед ходом, а также все инцидентные ей ребра, удаляются из графа. 
Игрок, который не может сделать ход, проигрывает.
Вам задан граф, который нарисовали Наташа и Петя. Для каждой вершины графа определите, кто выиграет при оптимальной игре обоих игроков,
если фишка будет исходно размещена в этой вершине.

Входные данные

Первая строка входного файла INPUT.TXT содержит три целых числа: n1, n2 и m – количество вершин в первой и второй доле, соответственно,
а также количество ребер в графе (1 ≤ n1, n2 ≤ 500, 0 ≤ m ≤ 50 000). Следующие m строк описывают ребра – каждая строка содержит
по два числа – номера вершин, соединенных соответствующим ребром. Вершины в каждой доле независимо пронумерованы, начиная с 1.

Выходные данные

В выходной файл OUTPUT.TXT выведите две строки.
Первая строка должна содержать n1 символов, i-й символ должен быть 'N',
если при исходном расположении фишки в i-й вершине первой доли, выигрывает Наташа
и 'P', если выигрывает Петя. Вторая строка должна описывать вершины второй доли аналогичным образом.
'''

graph = {}
with open('INPUT.TXT', 'r') as f:
    n, m = map(int, f.readline().split())
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for j in range(m):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)



# Функция минимакса
def minimax(node, depth, is_max):
    if not graph[node]:
        return 1 if is_max else -1
    if depth == 10:
        return 1 if is_max else -1
    if is_max:
        max_val = float('-inf')
        for adj_node in graph[node]:
            val = minimax(adj_node, depth+1, False)
            max_val = max(max_val, val)
        return max_val
    else:
        min_val = float('inf')
        for adj_node in graph[node]:
            val = minimax(adj_node, depth+1, True)
            min_val = min(min_val, val)
        return min_val

# Определение победителя в каждой вершине первой доли
winners = {}
for node in graph.keys():
    winners[node] = minimax(node, 0, True) > 0

# Определение победителя в каждой вершине второй доли
for node in graph.keys():
    if not winners[node]:
        continue
    for adj_node in graph[node]:
        if winners[adj_node]:
            winners[node] = False
            break

# Вывод результатов
with open('output.txt', 'w') as f:
    for node in graph.keys():
        f.write('1\n' if winners[node] else '0\n')