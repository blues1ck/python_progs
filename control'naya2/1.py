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

N = int(input())
M = int(input())
if M == 0:
    print('NO')
else:
    g = {str(i):{} for i in range(N)}

    for i in range(M):
        a, b = input().split()
        if a not in g:
            g[a] = {}
        g[a][b] = 1
        if b not in g:
            g[b] = {}
        g[b][a] = 1

    components = find_comp(g)
    if len(components[0]) == len(g):
        print('YES')
    else:
        print('NO')