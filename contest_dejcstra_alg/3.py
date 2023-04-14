from collections import deque

n, m = map(int, input().split())

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

def sum_of_dict(d):
    dkeys = d.keys()
    s = 0
    for i in dkeys:
        s += d[i]
    return s

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

G = {i:{} for i in range(n)}
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    a = int(a)
    b = int(b)
    add_edge(G, a, b, weight)
    add_edge(G, b, a, weight)

a = [sum_of_dict(dijkstra(G, i)) for i in range(n)]
print(a.index(min(a)))

