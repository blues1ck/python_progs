from collections import deque
from time import perf_counter as pc
import random
from collections import defaultdict

# самописный
def alg_prima(g):

    gkeys = list(g.keys())
    result = {}
    i = gkeys[0]
    result[i] = {}
    if not g[i]:
        return 'error'
    minpath = g[i][list(g[i].keys())[0]]
    for j in g[i]:
        if minpath >= g[i][j]:
            minpath = g[i][j]
            j_min = j
    result[j] = {}
    result[i][j] = g[i][j]
    result[j][i] = g[j][i]
    while sum(len(result[i]) for i in list(result.keys()))<2*(len(g)-1):
        minpath = -1
        for i in list(result.keys()):
            for j in g[i]:
                if j not in result:
                    if minpath == -1:
                        minpath = g[i][j]
                        i_min = i
                        j_min = j
                    if minpath > g[i][j]:
                        minpath = g[i][j]
                        i_min = i
                        j_min = j
        result[j_min] = {}
        result[j_min][i_min] = g[i_min][j_min]
        result[i_min][j_min] = result[j_min][i_min]
    return result
# самописный
def alg_kruskal(g):

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

    def is_not_cycle(g):
        components = find_comp(g)
        for k in range(len(components)):
            queue = deque()
            queue.extend(components[k][0])
            visited = [components[k][0]]
            k = True
            parent = {}
            parent[visited[0]] = '-1'
            while queue:
                i = queue.pop()
                for j in g[i]:
                    if j not in visited:
                        parent[j] = i
                        queue.append(j)
                        visited.append(j)
                    else:
                        if j != parent[i]:
                            k = False
                            return k
        return k

    tree = {}
    gkeys = list(g.keys())
    curcled = []
    longest = 0
    for j in gkeys:
        if j not in tree:
            for i in g[j]:
                longest = max(longest, g[j][i])
    k = 0
    while (2*(len(g)-1))!=sum(len(tree[i]) for i in list(tree.keys())):
        k = 1
        tree_keys = list(tree.keys())
        cur_tree = {i:{j:tree[i][j] for j in list(tree[i].keys())} for i in tree_keys}
        shortest = longest
        i_min, j_min = gkeys[0], gkeys[1]                     
        for i in gkeys:
            for j in g[i]:
                if i in tree:
                    if j not in tree[i]:
                        if [i, j] not in curcled:
                            shortest = min(shortest, g[i][j])
                            if shortest == g[i][j]:
                                i_min = i
                                j_min = j
                else:
                    if [i, j] not in curcled:
                        shortest = min(shortest, g[i][j])
                        if shortest == g[i][j]:
                            i_min = i
                            j_min = j
        if i_min not in tree:
            cur_tree[i_min] = {}
        if j_min not in tree:
            cur_tree[j_min] = {}
        cur_tree[i_min][j_min] = g[i_min][j_min]
        cur_tree[j_min][i_min] = g[j_min][i_min]
        if is_not_cycle(cur_tree):
            tree = cur_tree
        else:
            curcled.append([i_min, j_min])
            curcled.append([j_min, i_min])
    return tree
# из интернета
def kruskal(graph):
    mst = defaultdict(set)
    edges = [(cost, frm, to) for frm, edges in graph.items() for to, cost in edges.items()]
    edges.sort()
    parent = {i: i for i in range(len(graph))}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        parent[xroot] = yroot

    for edge in edges:
        weight, frm, to = edge
        if find(frm) != find(to):
            union(frm, to)
            mst[frm].add(to)

    return mst

def generate_random_graph(n, max_weight):
    graph = defaultdict(dict)
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph

prima_time = []
kruskal_time = []
k = 1
graph_list = []
for i in range(2, 100):
    graph_list.append(generate_random_graph(i, 15))
for i in graph_list:
    k+=1
    t1 = pc()
    alg_prima(i)
    t2 = pc()
    dt = t2 - t1
    prima_time.append(dt)
    t3 = pc()
    kruskal(i)
    t4 = pc()
    kruskal_time.append((t4-t3))

graph_len = [len(g) for g in graph_list]

import matplotlib.pyplot as plt
plt.plot(graph_len, prima_time, label = 'prim', color = 'green')
plt.plot(graph_len, kruskal_time, label = 'kraskal', color = 'red')
plt.legend()
plt.grid()
plt.show()
# видимо моя реализация алгоритма краскала далека до идеала, но я старался :)
