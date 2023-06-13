from collections import deque

def read_graph(filename):
    m = n = None
    G = {}
    f = open('/home/ilya/Рабочий стол/python_progs/polina/' + filename, 'r')
    a = f.readline()
    m = int(a)
    for _ in range(m):
        a = f.readline()
        v1, v2 = a.split()
        for v in (v1, v2):
            if v not in G:
                G[v] = []
        G[v1].append(v2)
    
    return G

def dfs(graph,start,finish):
    queue = deque()
    queue.extend(start)
    flag = False
    visited = []
    while queue:
        i = queue.popleft()
        visited.append(i)
        if finish == i:
            return True
        for j in graph[i]:
            if j not in visited:
                queue.extend(j)
    return flag

G = read_graph('newgraph.txt')
print(dfs(G, input('enter start position '), input('enter finish position ')))