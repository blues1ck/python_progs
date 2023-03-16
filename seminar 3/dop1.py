lst = list(map(int, input().split()))

def dop_sort(m):
    i = 0
    while i < len(m)-2:
        if m[i]==m[i+1]:
            m.pop(i+1)
        else:
            i = i + 1
    return m

m = dop_sort(sorted(lst))

a = [0]*len(lst)
for i in range(len(m)):
    for j in range(len(lst)):
        if lst[j] == m[i]:
            a[j] = i + 1
print(*a)