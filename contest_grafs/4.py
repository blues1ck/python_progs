N, M = map(int,input().split()) # количество вершин, кол-во ребер

graph = {}
for i in range(N):
    graph[i] = {}
for j in range(M):
    a, b, weight = map(int, input().split())
    graph[a][b] = weight
    graph[b][a] = weight

from collections import deque

queue = deque()
queue.append(0)
svyazn = []
for i in range(len(graph)):
    if len(graph[i]) == 0:
        svyazn.append(0)
        graph.pop(i) 
while len(graph) != 0:
    cur_w = 0
    for t in range(N):
        if (t in graph) and (len(graph[t])!=0):
            queue = deque()
            queue.append(t)
    while len(queue) != 0:
        i = queue.popleft()
        if len(graph[i]) == 0:
            graph.pop(i)
            queue = deque()
        else:
            for j in graph[i]:
                cur_w += graph[i][j]
                graph[j].pop(i)
                queue.append(j)
            graph.pop(i)

    svyazn.append(cur_w)

svyazn = sorted(svyazn)
for i in svyazn:
    print(i)