from collections import deque

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

def dijkstra(G, start):
    Q = deque()
    s = {}
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if (u not in s) or ((s[v]+G[v][u])<s[u]):
                s[u] = s[v] + G[v][u]
                Q.append(u)
    return(s)

def dfs(G, start, finish):
    Q = deque()
    p = {}
    p[start] = [-1]
    s = {}
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if (u not in s) or ((s[v]+G[v][u])<s[u]):
                s[u] = s[v] + G[v][u]
                p[u] = p[v] + [v]
                Q.append(u)
    return(p)

n, m, s, f = map(int, input().split())
G = {i:{} for i in range(n)}
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    a = int(a)
    b = int(b)
    add_edge(G, a, b, weight)
    add_edge(G, b, a, weight)
shortest_distance = dfs(G, s, f)
print(len(shortest_distance[f]))


