def read_graph(filename):
    m = n = None
    G = {}
    f = open('/home/ilya/Рабочий стол/python_progs/polina/' + filename, 'r')
    a = f.readline()
    m = int(a)
    for _ in range(m):
        a = f.readline()
        v1, v2 = a.split()
        for v in (v1, v2):
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    
    return G

def graph_matrix(G):
    keys = list(G.keys())
    matrix = ['0']*len(keys)
    for key in keys:
        key_index = keys.index(key)
        matrix[key_index] = ['0']*(len(keys)+1)
        for i in range(len(keys)):
            if keys[i] in G[key]:
                matrix[key_index][i] = '1'
            else:
                matrix[key_index][i] = '0'
        matrix[key_index][len(keys)] = key

    matrix.extend([keys])
    return matrix
    
def write_matrix(filename, matrix):
    with open(filename, 'w') as f:
        for i in range(len(matrix)-1):
            string = ''
            for j in matrix[i]:
                try:
                    j = int(j)
                    string = string + str(j) + ' '
                except:
                    string = string + '|' + str(j)
            f.write(f'{str(string)}\n')

        f.write('_'*(len(string)-3))
        f.write('\n')
        string = ''
        for j in matrix[-1]:
            string = string + j + ' '
        f.write(string)
        f.write('\n')
        f.write('\n')
        f.write('1 - path, 0 - no path')


G = read_graph('orient.txt')
matrix = graph_matrix(G)
write_matrix('output_matrix.txt', matrix)