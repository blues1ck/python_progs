N, M = map(int, input().split()) # количество вершин, кол-во ребер

graph = {}
for i in range(1, N+1):
    graph[i] = set()
for j in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


from collections import deque

def dfs(graph, start, visited = set()):
    if len(visited) == 0:
        visited.add(start)
    for i in graph[start]:
        if i in visited:
            continue
        visited.add(i)
        if (len(graph[i])!=0):
            dfs(graph, i, visited)        
    return visited


'''graph = {
    1: set(),
    2: set(),
    3: set(),
    4: set()
}
graph[1].add(2)
graph[2].add(1)
graph[2].add(3)
graph[3].add(2)
graph[3].add(4)
N = 4'''
k = 0
k_1 = 1
a = set()
while k != 1:
    for i in range(1, N+1):
        if len(graph[i]) != 0:
            if len(dfs(graph, i)) != len(graph) - len(a):
                k = 1
                break
    if k == 1:
        break
    max_con = 0
    for i in range(1, N+1):
        max_con = max(max_con, len(graph[i]))
    for i in range(1, N + 1):
        if len(graph[i]) == max_con:
            graph[i] = set()
            a.add(i)
            break
    k_1 = 0
    for i in range(1, N+1):
        if len(graph[i]) != 0:
            k_1 += 1
    if k_1 <= 1:
        break

if k_1 > 1:
    print(*a)
else:
    print('-1')