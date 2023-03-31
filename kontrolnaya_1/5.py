a = list(input().split())
b = list(input().split())
d = {a[i]: b[i] for i in range(len(a))}
print(d)