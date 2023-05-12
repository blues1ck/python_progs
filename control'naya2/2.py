from collections import deque

def dfs_dijkstra(G, start):
    # алгортим Дейкстры для маршрута
    Q = deque()
    p = {}
    # кратчайший маршрут до каждой вершины
    p[start] = [-1]
    s = {}
    # кратчайший маршрут до каждой точки
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            # идем по вершинам графа, в которые можно добраться напрямую из текущей
            if (u not in s) or ((s[v]+G[v][u])<s[u]):
                # условие обновления кратчайшего пути
                s[u] = s[v] + G[v][u]
                p[u] = p[v] + [v]
                Q.append(u)
    return [p, s]

N = int(input())
M = int(input())
S = input()
F = input()
g = {str(i):{} for i in range(N)}
for i in range(M):
    a, b, w = input().split()
    g[a][b] = int(w)
    g[b][a] = int(w)
d = dfs_dijkstra(g, S)
print(d[1][F]+1)
print(*d[0], sep = ' ')

'''
5
7
0
4
0 1 2
0 2 5
1 2 1
1 3 6
2 3 2
2 4 4
3 4 1
'''