# heaps 
def add_to_heap(h, item):
    h.append(item)
    shift_up(h, len(h) - 1)


def shift_up(h, i):
    if i == 0:
        return
    parent_i = (i-1) // 2
    if h[i] < h[parent_i]:
        h[i], h[parent_i] = h[parent_i], h[i]
        shift_up(h, parent_i)

def pop_from_heap(h):
    if len(h) == 0:
        raise ValueError('heap is empty can\'t pop item from it')
    result = h[0]
    if len(h) == 1:
        h.pop()
        return result
    h[0] = h.pop()
    shift_down(h, 0)
    return result

def shift_down(h, i):
    a = [h[i]]
    a.extend(h[2*i + 1:2*i + 3])
    m = min(a)
    if m == h[i]:
        return
    if m == h[2*i+1]:
        h[i], h[2*i+1] = h[2*i+1], h[i]
        shift_down(h, 2*i + 1)
    else:
        h[i], h[2 * i + 2] = h[2 * i + 2], h[i]
        shift_down(h, 2 * i + 2)

# creating heap from random list
def heapify(h):
    for i in range((len(h)-2) // 2, -1, -1):
        shift_down(h, i)

def heap_to_sorted(h):
    for i in range(len(h)-1, 0, -1):
        h[i] = h[0]



from random import randint

h = []
a = [randint(1, 1000) for _ in range(10)]
for x in a:
    add_to_heap(h, x)
c = [h[i] for i in range(len(h))]
print(a)
print(h)
heapify(a)
print(a)
for _ in range(10):
    print(pop_from_heap(h), end=', ')
print()
for _ in range(10):
    print(pop_from_heap(a), end=', ')
print()
print()
print(c, heap_to_sorted(c), sep='\n')