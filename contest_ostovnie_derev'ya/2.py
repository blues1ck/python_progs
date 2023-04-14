'''
6
1 3 0 5 8 5
2 4 6 7 9 9
'''
from collections import deque

def dijkstra(G, start):
    Q = deque()
    s = {}
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if (u not in s) or ((s[v]+G[v][u])>s[u]):
                s[u] = s[v] + G[v][u]
                Q.append(u)
    return(s)

n = int(input())
s1 = list(map(int, input().split()))
s2_bezform = list(map(int, input().split()))
s2 = [s2_bezform[i]+1 for i in range(len(s2_bezform))]
s = sorted(s1 + s2)
G = {(i):{0:0} for i in s}
'''
6
10 20 60 120 200 300
15 45 100 190 250 330
'''
Gkeys = G.keys()
for i in Gkeys:
     for j in Gkeys:
          if j<i:
               G[i][j] = 0
for i in range(n):
     G[s2[i]][s1[i]] = 1
if 0 not in G.keys():
     G[min(s1)][0] = 0
     G[0] = {}
     G[0][min(s1)] = 0
print(dijkstra(G, max(s2))[0])

