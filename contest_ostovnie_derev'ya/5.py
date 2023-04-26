def alg_prima(g, a, b):
    gkeys = list(g.keys())
    result = {}
    i = a
    result[i] = {}
    if not g[i]:
        return 'error'
    minpath = g[i][list(g[i].keys())[0]]
    j = b
    result[j] = {}
    result[i][j] = g[i][j]
    result[j][i] = g[j][i]
    path_len = g[i][j]
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
        path_len += g[i_min][j_min]
        result[j_min] = {}
        result[j_min][i_min] = g[i_min][j_min]
        result[i_min][j_min] = result[j_min][i_min]
    return path_len

n, m = map(int, input().split())
g = {str(i):{} for i in range(1, n+1)}
ab = []
for i in range(m):
    a, b, weight = input().split()
    weight = int(weight)
    ab.append([a, b])
    g[a][b] = weight
    g[b][a] = weight
for i in ab:
    print(alg_prima(g, i[0], i[1]))
