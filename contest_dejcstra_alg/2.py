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

n, m = map(int, input().split())
G = {str(i):{} for i in range(n)}
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    add_edge(G, a, b, weight)
    add_edge(G, b, a, weight)

'''G = {'0':{'2': 3},
     '1':{'3':8, '4':3, '5':2, '6':3},
     '2':{'0':2, '3':1},
     '3':{'2':1, '1': 8, '6':4},
     '4':{'1':3},
     '5':{'1':2},
     '6':{'3':4, '1':3}}'''
g = {}
for i in range(len(G)):
    g[str(i)+'A']={}
    g[str(i)+'B']={}

dop_keys = g.keys()

for i in dop_keys:
    if 'A' in i:
        j = 'B'
    else:
        j = 'A'
    cur_keys = G[i[:-1]].keys()
    for k in cur_keys:
        g[i][str(k+j)] = G[i[:-1]][k]

k = int(input())
vivod = []
for i in range(k):
    a, b = map(str, input().split())
    f_a = dijkstra(g, a + "A")
    fa_keys = f_a.keys()
    if b + "A" in fa_keys:
        cur_way = dfs(g, a + "A", b + "A")[1:]+[b+ "A"]
        for i in range(len(cur_way)):
            cur_way[i] = int(cur_way[i][:-1])
        vivod.append(cur_way)
    else:
        vivod.append([-1])
    
for i in range(len(vivod)):
    print(*vivod[i])