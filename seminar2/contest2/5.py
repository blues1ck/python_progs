def smallest_range(lists):
    indices = {}
    for i, lst in enumerate(lists):
        for elem in lst:
            if elem not in indices:
                indices[elem] = []
            indices[elem].append(i)
    all_indices = sorted(idx for lst in lists for idx in range(len(lst)))
    left = 0
    right = 0
    counts = [0] * len(lists)
    best_range = None
    while right < len(all_indices):
        idx = all_indices[right]
        for lst_idx in indices.get(lists[idx[0]][idx[1]]):
            counts[lst_idx] += 1
        while all(counts):
            if best_range is None or all_indices[right][0] - all_indices[left][0] < best_range[1] - best_range[0]:
                best_range = (all_indices[left][0], all_indices[right][0])
            idx = all_indices[left]
            for lst_idx in indices.get(lists[idx[0]][idx[1]]):
                counts[lst_idx] -= 1
            left += 1
        right += 1
    return best_range

# Пример использования
lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print(smallest_range(lists)) # (20, 24)

