def heapqsort(lst):

    def heapqmin(lst):
        nlst = []
        for i in range(len(lst)):
            nlst.append(lst[i])
            for j in range(len(nlst)-1,-1,-1):
                if nlst[j]<nlst[j//2]:
                    nlst[j], nlst[j//2] = nlst[j//2], nlst[j]
        return nlst
    nlst = []
    for i in range(len(lst)):
        a = (heapqmin(lst))[0]
        nlst.append(a)
        lst.remove(a)
    return nlst

french = list(map(int, input().split()))
swimmers = list(map(int, input().split()))
piano = list(map(int, input().split()))
a = []
for i in piano:
    if i in swimmers and i not in french:
        a.append(i)
print(*heapqsort(a))

