def heap_reverse(h):
    a = []
    for i in range(len(h)):
        a.append(h[i])
        shift_up(a, i)
    return a

def shift_up(h, i):
    if i == 0:
        return
    parent_i = (i-1) // 2
    if h[i] < h[parent_i]:
        h[i], h[parent_i] = h[parent_i], h[i]
        shift_up(h, parent_i)

a = list(map(int, input().split()))
print(*heap_reverse(a))