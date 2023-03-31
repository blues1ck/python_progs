N = int(input()) # количество вершин
M = int(input()) # кол-во ребер

graph = {}
for i in range(N):
    graph[i] = set()
for j in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

from collections import deque

queue = deque()
queue.append(0)
svyazn = 0
for i in range(len(graph)):
    if len(graph[i]) == 0:
        svyazn += 1
        graph.pop(i) 
while len(graph) != 0:
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
                graph[j].discard(i)
                queue.append(j)
            graph.pop(i)

    svyazn += 1

print(svyazn)