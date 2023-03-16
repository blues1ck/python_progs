a = list(map(int, input().split()))
k = 1
for i in range(len(a)//2):
    if 2*i+2<len(a):
        if a[i] >= a[2*i+1]:
            k = 0
            break

    elif 2*i+2<len(a):
        if  a[i] >= a[2*i+1] or a[i]>=a[2*i+2]:
            k = 0
            break
print(k)