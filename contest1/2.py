def number_count(s):
    a = {}
    for i in s:
        if int(i) not in a:
            a[int(i)] = 1
        else:
            a[int(i)] += 1
    return a

s = input()
print(number_count(s))