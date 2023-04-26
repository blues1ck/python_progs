from collections import deque

def alg_kraskalka(g):

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

n, m = map(int, input().split()) # кол-во вершин и ребер
g = {}
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = weight
    g[b][a] = weight
t = alg_kraskalka(g)
print(t)

'''
g = {   
    '3': {'0': 3, '4': 3}, 
    '0': {'3': 3, '2': 4, '1': 2}, 
    '4': {'3': 3, '2': 6, '1': 2, '5': 1, '6': 8, '8': 7}, 
    '2': {'0': 4, '4': 6},
    '1': {'0': 2, '5': 5, '4': 2},
    '5': {'1': 5, '4': 1, '6': 6, '7': 12}, 
    '6': {'5': 6, '4': 8, '9': 4}, 
    '7': {'5': 12, '8': 6, '9': 11}, 
    '8': {'4': 7, '9': 3, '7': 6}, 
    '9': {'8': 3, '7': 11, '6': 4}
    }
'''

'''
10 16
3 0 3
3 4 3
0 2 4
0 1 2
2 4 6
1 5 5
1 4 2
4 5 1
5 6 6
5 7 12
4 6 8
4 8 7
8 9 3
8 7 6
7 9 11
6 9 4
'''
