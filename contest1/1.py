def to_dict(l):
    global n
    a = {i: str(i)*n for i in l}
    return a

n = int(input())
l = list(map(int, input().split()))
print(to_dict(l))