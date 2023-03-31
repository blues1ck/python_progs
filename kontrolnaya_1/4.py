n = int(input())
a = input()
b = input()

# создадим словари хэшей всех возможных подстрок каждой из строк
hashes_a_string = {a[i:j]:hash(a[i:j]) for i in range(n) for j in range(i+1, n+1)}
hashes_b_string = {b[i:j]:hash(b[i:j]) for i in range(n) for j in range(i+1, n+1)}

# с помощью множества пересечем все возможные ключи словарей

substr = set(hashes_a_string.keys()) & set(hashes_b_string.keys())

max_len = 0
max_substr = ''
for sub in substr:
    if (len(sub) > max_len) and (hashes_a_string[sub] == hashes_b_string[sub]):
        max_len = len(sub)
        max_substr = sub

print(max_substr)