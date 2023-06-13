def hash_string(s, M):
    p = 31
    hash_value = 0
    for c in s:
        hash_value = (hash_value + ord(c)) % M
    return hash_value

s = input()
M = int(input())
print(hash_string(s, M))