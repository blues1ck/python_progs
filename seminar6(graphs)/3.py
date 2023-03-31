inc = {'LED':'VN', 'FR':'NN', 'VN':'FR'}
# led -> vn -> fr -> nn


def dfs(v):
    global visited
    if v in visited:  # Если вершина уже посещена, выходим
        return
    visited.add(v)  # Посетили вершину v
    for i in inc[str(v)]:  # Все смежные с v вершины
        if not i in visited:
            dfs(i)

print(inc)
lst = []

while inc is not None:
    for i in inc:
        if inc[i] not in inc:
            lst.extend(inc[i])
            break
    inc.pop(i)
    print(lst)
