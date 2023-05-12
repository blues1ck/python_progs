from collections import deque

def find_comp(g):
        gkeys = g.keys()
        visited = [] # просто все пройденные вершины
        result = [] # список списков связности
        queue = deque()
        while len(visited)!=len(gkeys):
            for i in gkeys:
                if i not in visited:
                    queue.extend(i)
                    break
            cur_visited = []
            cur_visited.append(i)
            while queue:
                i = queue.pop()
                for j in g[i]:
                    if j not in cur_visited: 
                        cur_visited.append(j)
                        queue.extend(j)
            
            for i in cur_visited:
                visited.append(i)
            result.append(cur_visited)
        return(result)

n, s = input().split()
n = int(n)
g = {str(i):{} for i in range(n)}
for i in range(n):
    l = list(map(int, input().split()))
    g[str(i)] = {str(j):l[j] for j in range(len(l))}
gkeys = list(g.keys())
G = {str(i):{} for i in range(n)}
for i in gkeys:
    cur_keys = list(g[i].keys())
    for j in cur_keys:
        if g[i][j] == 1:
            G[i][j] = 1
            G[j][i] = 1

components = find_comp(G)
for i in components:
    if s in i:
        print(len(i)-1)