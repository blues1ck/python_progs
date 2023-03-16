N = int(input())
d = {}
m = 0 
for i in range(N):
    a = input()
    if a in d:
        d[a] +=1
    else:
        d[a] = 1
    a = ''
print(d)

sorted_values = sorted(d.values())
dkeys = d.keys()

for i in range(len(sorted_values),-1, -1):
    for j in dkeys:
        if d[j] == i and i!=0:
            print(j,i)
            d[j] = 0