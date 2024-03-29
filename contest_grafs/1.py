from collections import deque

start = input()  # Клетка, в которой находится конь
finish = input()  # Клетка, в которую необходимо попасть

letters = 'abcdefgh'  # Названия столбцов
numbers = '12345678'  # Названия строк

graph = dict()  # Создаем пустой словарь из 64 ключей.
for l in letters:  # Каждому ключу соответствует пустое множество.
    for n in numbers:
        graph[l+n] = set()  # Вершины будут иметь названия, состоящие из строки "буква+цифра".


def add_edge(v1, v2):
    """Функция добавляет ребра в словарь по ключу."""
    graph[v1].add(v2)
    graph[v2].add(v1)


for j in range(8):  # Заполняем словарь значениями в соответствии
    for i in range(8):  # с разрешенными ходами коня.
        v1 = letters[i] + numbers[j]
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i+2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i-2] + numbers[j+1]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i-1] + numbers[j+2]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i+1] + numbers[j+2]
            add_edge(v1, v2)

distances = {v: None for v in graph}  # Массив расстояний от стартовой вершины до всех пройденных.
parents = {v: None for v in graph}  # Список предшествующих вершин для каждой вершины.

distances[start] = 0  # Присваиваем стартовой вершине значение 0 в списке distances.
queue = deque([start])  # Создаем очередь для перебора вершин.

while queue:  # Как только queue станет пустой, выполнение цикла прекратится.
    cur_v = queue.popleft()  # Добываем из очереди первый элемент.
    for neigh_v in graph[cur_v]:  # Перебираем его соседей.
        if distances[neigh_v] is None:  # Если соседнюю вершину не посещали,
            # она имеет значение None в списке distances.
            distances[neigh_v] = distances[cur_v] + 1  # Тогда присваиваем ей
            # значение ее предшествующей вершины + 1.
            parents[neigh_v] = cur_v  # Вершина cur_v является предком
            # текущей рассматриваемой вершины neigh_v.
            if neigh_v == finish:  # Если дошли до искомой клетки,
                break  # прерываем цикл.
            queue.append(neigh_v)  # Добавляем эту вершину в конец очереди.


path = [finish]  # Список, содержащий путь от конечной до начальной клетки.
parent = parents[finish]  # Предшествующая вершина для конечной клетки.

while not parent is None:  # Когда предшествующая вершина приобретет значение None, цикл завершится.
    path.append(parent)  # Добавляем предшественника в путь.
    parent = parents[parent]  # Обновляем значение parent.

for i in range(len(path) - 1, -1, -1):
    print(path[i])  # Выводим путь в обратной последовательности.
