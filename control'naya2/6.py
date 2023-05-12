n, m = map(int, input().split()) # Считываем количество гостей и пар, которые не могут сидеть рядом
adj_list = [[] for _ in range(n)] # Создаем пустой список смежности для графа

for _ in range(m):
  a, b = map(int, input().split())
  adj_list[a-1].append(b-1) # Добавляем b в список смежности для a
  adj_list[b-1].append(a-1) # Добавляем a в список смежности для b

def dfs(v, color):
  colors[v] = color # Красим вершину в цвет color
  for u in adj_list[v]:
    if colors[u] == color: # Если соседняя вершина уже покрашена в тот же цвет, то это означает, что они не могут сидеть за одним столом
      return False
    if colors[u] == 0 and not dfs(u, -color): # Если соседняя вершина еще не покрашена и рекурсивный вызов dfs вернул False, то это означает, что комбинация рассадки невозможна
      return False
  return True

colors = [0] * n # Создаем список цветов для гостей (0 - не покрашен, 1 - первый стол, -1 - второй стол)
if dfs(0, 1): # Запускаем DFS из первой вершины с цветом 1
  print("YES")
  print(" ".join(str(i+1) for i in range(n) if colors[i] == 1)) # Выводим номера гостей, которых нужно посадить за первый стол
else:
  print("NO")
    