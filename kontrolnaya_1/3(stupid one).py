def bin_tree_height(a):
    i = 0
    while len(a)>(2**i):
        i += 1

    return i+1


a = list(map(str, input().split()))
print(bin_tree_height(a))

