import heapq

def nsmallest(n, iterable):
    heap = iterable[:n]
    heapq._heapify_max(heap)
    for i in iterable[n:]:
        if i < heap[0]:
            heapq._heapreplace_max(heap, i)
    return sorted(heap)
