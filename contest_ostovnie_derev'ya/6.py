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

l = list(map(int, input().split()))
n, m = l[0], l[1]
centers = l[2:] # города центры
centers = [str(i) for i in centers]
g = {str(i): {} for i in range(n)}
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    g[a][b] = weight
    g[b][a] = weight
components = find_comp(g) # компонены связности городов
tops = g.keys() # все города
vilages = [] # города не являющиеся центрами
for i in tops:
    if i not in centers:
        vilages.append(i)
graphs = [] # список связных графов
for i in range(len(components)):
    cur_g = {j:{} for j in components[i]}
    for j in components[i]:
        cur_g[j] = g[j]
    graphs.append(cur_g)
min_paths = 0
for i in vilages:
    for j in components:
        if i in j:
            break
    # i - перебор по деревням
    # j - компонента связонсти, где содержится i
    key = False
    cur_centers = []
    for k in j:
        if k in centers:
            key = True
            cur_centers.append(k)
    if key == False:
        continue
    cur_min_path = []
    for k in cur_centers:
        cur_min_path.append(dijkstra(graphs[components.index(j)], i)[k])
    min_paths += min(cur_min_path)

print(min_paths)
        


'''
5 3 0 1
0 1 34
2 1 7
3 2 85
'''