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
        G[v2].append(v1)
    
    return G

def dfs(graph, start):
    queue = deque()
    queue.extend(start)
    res = []
    while queue:
        current = queue.popleft()
        if current not in res:
            res.append(current)
        for next in graph[current]:
            if next not in res:
                queue.extend(next)
    output = ''
    for i in next:
        output = output + str(res) + ''
    return output

def write_vertex(output_file, output_string):
    with open(output_file, 'w') as f:
        f.write(output_string, '\n')


import random as rd
G = read_graph('orient.txt')
write_vertex('output.txt', dfs(G, list(G.keys())[rd.randint(0, len(G)-1)]))

