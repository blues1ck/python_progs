'''N = 3
a = [[3,5,7], [2,14,15], [1, 7, 10]]'''
N = int(input())
a = []
for i in range(N):
    a.append(sorted(list(map(int, input().split()))))

s = [a[i][0] for i in range(N)] #список минимальных в каждом списке
ind = N*[0]
minint = max(s) - min(s)
min1= min(s)
min2 = max(s)
while True:
    try:
        minind = s.index(min(s)) # из какого списка нужно брать
        ind[minind] += 1 
        s[minind] = a[minind][ind[minind]] # добавляем в s след элемент из списка откуда был минимальный
        if abs(max(s)-min(s))< minint:
            minint = max(s)-min(s)
            min1 = min(s)
            min2 = max(s)
    except:
        print(f'{min1}-{min2}')
        break

    



    
