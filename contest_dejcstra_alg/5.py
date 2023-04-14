from collections import deque

fout = open('abc.txt', 'w')  # 'w' - это режим "запись" ("write")

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

def dfs(G, start, finish = 0):
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
    return(p[finish])

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

v, e, start, end = input().split()
v, e = int(v), int(e)
G = {}
for i in range(e):
    a, b, weight = input().split()
    weight = int(weight)
    add_edge(G, a, b, weight)
    add_edge(G, b, a, weight)
mar = dfs(G, start, end)[1:]
outstr = ''
for i in range(len(mar)):
    outstr += (mar[i] + ' -> ' )
outstr += str(end)

fout.write(f"Your trip from {start} to {end} will be {dijkstra(G, start)[end]} minutes.\n")
fout.write(outstr)
fout.close()

'''
6 5 mendeleevskaya serpukhovskaya
mendeleevskaya tsvetnoy_bulvar 4
tsvetnoy_bulvar chekhovskaya 3
chekhovskaya borovitskaya 4
borovitskaya polyanka 3
polyanka serpukhovskaya 3
'''
