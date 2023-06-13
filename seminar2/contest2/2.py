french = set(input().split())
swimmers = set(input().split())
pianists = set(input().split())

result = sorted(list(map(int, swimmers.intersection(pianists).difference(french))))
print(*result)