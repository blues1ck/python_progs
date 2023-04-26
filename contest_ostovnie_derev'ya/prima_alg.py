from collections import deque

def alg_prima(g):
    gkeys = list(g.keys())
    result = {}
    i = gkeys[0]
    result[i] = {}
    if not g[i]:
        return 'error'
    minpath = g[i][list(g[i].keys())[0]]
    for j in g[i]:
        if minpath >= g[i][j]:
            minpath = g[i][j]
            j_min = j
    j = j_min
    result[j] = {}
    result[i][j] = g[i][j]
    result[j][i] = g[j][i]
    min_path = g[i][j]
    while sum(len(result[i]) for i in list(result.keys()))<2*(len(g)-1):
        minpath = -1
        for i in list(result.keys()):
            for j in g[i]:
                if j not in result:
                    if minpath == -1:
                        minpath = g[i][j]
                        i_min = i
                        j_min = j
                    if minpath > g[i][j]:
                        minpath = g[i][j]
                        i_min = i
                        j_min = j
        min_path += g[i_min][j_min]
        result[j_min] = {}
        result[j_min][i_min] = g[i_min][j_min]
        result[i_min][j_min] = result[j_min][i_min]
    return [result, min_path]

n, m = map(int, input().split())
g = {str(i):{} for i in range(1, n+1)}
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    g[a][b] = weight
    g[b][a] = weight

t = alg_prima(g)
print(t[1])

'''
5 7
1 2 3
1 3 1
1 4 5
2 3 2
2 5 3
3 4 2
4 5 4
'''