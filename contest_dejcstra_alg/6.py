from collections import deque

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
tsifri = '123456789'
G = {i+j+k+m:{} for i in tsifri for j in tsifri for k in tsifri for m in tsifri}
chisla = G.keys()
for i in chisla:
    if i[0] != '9':
        j = i
        j = chr(ord(i[0]) + 1) + j[1:]
        G[i][j] = 1

    if i[3] != '1':
        j = i
        j = j[:3] + chr(ord(i[3]) - 1)
        G[i][j] = 1
    
    j = str(i[3]+i[0]+i[1]+i[2])
    G[i][j] = 1
    j = str(i[1]+i[2]+i[3]+i[0])
    G[i][j] = 1

a = input()
b = input()
mar = dfs(G, a, b)[1:]
for i in mar:
    print(i)
print(b)