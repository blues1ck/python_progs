
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
print(*heapqsort(list(map(int, input().split()))))