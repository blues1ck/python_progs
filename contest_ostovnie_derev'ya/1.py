
v, e = map(int, input().split())
g = input()
g = g [2:-2]
g = list((g.split('}, {')))
for i in range(len(g)):
    if g[i] == '':
        g[i] = []
    else:
        g[i] = list(map(int, g[i].split(', ')))
G = {i:[] for i in range(v)}
for i in range(len(g)):
    G[i] = g[i]
def dfs(g, start, visited = set(), parent = -1):
    # print(start, parent, visited)
    if g[start] is None:
        return True
    m = True
    if parent!=-1:
        visited.add(parent)
    for i in g[start]:
        if i!=parent:
            if i in visited:
                return False
            m = dfs(g, i, visited, start)
            if m==False:
                break
    visited.clear()
    return m

k = True
for i in range(len(G)):
    k = dfs(G, i)
    if k == False:
        break
if k:
    print('NO')
else:
    print('YES')
'''
5 5
{{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}}
'''
'''
5 5
{{1}, {0, 2}, {1, 3}, {2, 4}, {3}}
'''
'''
6 5
{{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}, {}}
'''
'''
7 5
{{}, {2}, {1, 3}, {2, 4}, {3, 5}, {4}, {}}
'''