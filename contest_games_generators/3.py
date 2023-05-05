from collections import deque

def dfs_for_directed(graph, start):
    
    def vis(visited):
        res = []
        for i in visited:
            res.append(i[0])
        return res

    queue = deque()
    queue.append([start, 1])
    visited = []
    final_points = set()
    while queue:
        current = queue.popleft()
        cur_path = current[1]
        current = current[0]
        if [current,cur_path] not in visited:
            visited.append([current, cur_path])
        if len(graph[current]) == 0:
            final_points.add(current)
        for i in graph[current]:
            if i in vis(visited):
                return -1
            queue.append([i, cur_path + 1])
            
    return [visited, final_points]

def maxi(f):
    max_g_path = 0
    for j in f:
        max_g_path = max(max_g_path, j[1])
    return max_g_path


n1, m1 = map(int, input().split())
g1 = {str(i):set() for i in range(1, n1+1)}

for i in range(m1):
    a, b = input().split()
    g1[a].add(b)

n2, m2 = map(int, input().split())
g2 = {str(i):set() for i in range(1, n2 + 1)}

for i in range(m2):
    a, b = input().split()
    g2[a].add(b)

start_pos_count = int(input())
start_positions = []
for i in range(start_pos_count):
    v1, v2 = input().split()
    start_positions.append([v1, v2])

for i in start_positions:
    paths1 = dfs_for_directed(g1, i[0])
    paths2 = dfs_for_directed(g2, i[1])
    if paths1 == -1 and paths2 == -1:
        print('draw')
    elif paths1 == -1:
        print('firsrt')
    elif paths2 == -1:
        print('second')
    else:
        max1 = maxi(paths1[0])
        max2 = maxi(paths2[0])
        if max1 > max2:
            print('first')
        else:
            print('second')

'''
3 2
1 2
2 3
2 1
1 2
2
1 1
3 2
'''