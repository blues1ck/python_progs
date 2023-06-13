from collections import deque

arr = list(map(float, input().split()))
stack = deque()
for i in arr:
    stack.appendleft(i)
rev_arr3 = deque()
rev_arr5 = deque()
rev_arr2 = deque()

while stack:
    i = stack.popleft()
    if i%3 == 0:
        rev_arr3.appendleft(i)
    elif i%2 == 0:
        rev_arr2.appendleft(i)
    elif i%5 == 0:
        rev_arr5.appendleft(i)

while rev_arr2 or rev_arr3 or rev_arr5:
    if rev_arr3:
        i = rev_arr3.pop()
        print(i, end = ' ')
    if rev_arr2:
        i = rev_arr2.pop()
        print(i, end= ' ')
    if rev_arr5:
        i = rev_arr5.pop()
        print(i, end = ' ')
print()
