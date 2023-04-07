N, M = map(int, input().split())
graph = {i:set() for i in range(N)}
for i in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)


from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = deque()
        visited.append(start)
    if len(graph[start]) == 0:
        # visited.append(start)
        return visited
    else:
        for i in graph[start]:
            visited.append(i)
            dfs(graph, i, visited)
        return visited
    
try:
    top = {i: list(dfs(graph, i))[:-1] for i in range(N)}
    a = list(top.keys())
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if len(top[a[i]]) < len(top[a[j]]):
                a[i], a[j] = a[j], a[i]
    print(a, top, sep='\n')
except:
    print('NO')
