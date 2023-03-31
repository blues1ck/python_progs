# Поиск в глубину - ПВГ (Depth First Search - DFS)
def dfs(v):
    global visited
    if v in visited:  # Если вершина уже посещена, выходим
        return
    visited.add(v)  # Посетили вершину v
    for i in inc[str(v)]:  # Все смежные с v вершины
        if not i in visited:
            dfs(i)

N = int(input())
inc = {}
for i in range(N):
    inc[str(i)] = []
a, b = map(int, input().split())
try:
    while a!='#':
        if (int(a)<=N-1) and (int(b)<=N-1): 
            inc[str(a)].append(b)
            inc[str(b)].append(a)
            a, b = map(int, input().split())
        else:
            print("Недопустимое ребро")
            a, b = map(int, input().split())
except:
    pass
visited = set()
start = 0
dfs(start)
if len(visited) == N:
    print(True)
else:
    print(False)
