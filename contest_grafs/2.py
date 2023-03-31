from collections import deque

n, m = map(int, input().split())
grafs = dict()
for i in range(n):
    grafs[i] = set()

def add_connection(v1, v2):
    grafs[v1].add(v2)
    grafs[v2].add(v1)

for j in range(m):
    v1, v2 = map(int, input().split())
    add_connection(v1, v2)


way_len = [-1]*n
way_len[0] = 0

queue = deque()
queue.append(0)
while len(queue)!=0:
    i = queue.popleft()
    for j in grafs[i]:
        if way_len[j] == -1:
            way_len[j] = way_len[i] + 1
            queue.append(j)
        elif way_len[i] + 1 < way_len[j]:
            way_len[j] = way_len[i] + 1
            queue.append(j)

for i in range(n):
    print(way_len[i])