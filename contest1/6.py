def hash_string(s, M):
    p = 31
    hash_value = 0
    for c in s:
        hash_value = (hash_value * p + ord(c)) % M
    return hash_value

def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash_string(pattern, M)
    t_hash = hash_string(text[:p_len], M)
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                print(i, end=' ')
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(31, p_len-1, M)) % M
            t_hash = (t_hash * 31 + ord(text[i+p_len])) % M
    if i == 0:
        print(-1)

pattern = input()
text = input()
M = 10**9+9
if pattern not in text:
    print(-1)
else:
    rabin_karp(pattern, text)
