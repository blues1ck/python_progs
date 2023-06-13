arr = list(map(int, input().split()))

is_max_heap = True
for i in range(len(arr)):
    left_child = 2*i + 1
    right_child = 2*i + 2
    if left_child < len(arr) and arr[left_child] > arr[i]:
        is_max_heap = False
        break
    if right_child < len(arr) and arr[right_child] > arr[i]:
        is_max_heap = False
        break

if is_max_heap:
    print(1)
else:
    print(0)