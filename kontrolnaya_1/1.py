from collections import deque
a_chet = deque()
a_nechet = deque()
a = list(map(int, input().split()))
for i in a:
    if i % 2 == 0:
        a_chet.append(i)
    else:
        a_nechet.append(i)

while (len(a_chet) > 0) and (len(a_nechet) > 0):
    print(a_chet.pop(), a_nechet.pop(), end = ' ')
if len(a_chet) == 0:
    while (len(a_nechet) > 0):
        print(a_nechet.pop(), end = ' ')
if len(a_nechet) == 0:
    while (len(a_chet) > 0):
        print(a_chet.pop(), end = ' ')
print()