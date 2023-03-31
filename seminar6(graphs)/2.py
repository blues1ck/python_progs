N = int(input())
inc = {}
for i in range(N):
    inc[str(i)] = []
links = list(input().split(' '))
for x in range(len(links)):
    links[x] = links[x].replace('[', '')
    links[x] = links[x].replace(']', '')
    links[x] = links[x].replace(')', '')
    links[x] = links[x].replace('(', '')
    links[x] = links[x].replace(',', '')
i = 0
while i+1 < len(links):
    if int(links[i]) < N and int(links[i+1]) < N:
        inc[str(links[i])].append(links[i+1])
        i = i + 2
a, b = map(int, input().split())

def dfs(v):
    global visited
    if v in visited:  # Если вершина уже посещена, выходим
        return
    visited.add(v)  # Посетили вершину v
    for i in inc[str(v)]:  # Все смежные с v вершины
        if not i in visited:
            dfs(i)

visited = set()
dfs(str(a))
if str(b) in visited:
    print(True)
else:
    print(False)