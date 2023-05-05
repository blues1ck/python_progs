def infinte(lst, tries):
    try:
        for i in range(len(lst)):
            lst[i] = lst[i].replace('[', '')
            lst[i] = lst[i].replace(']', '')
            lst[i] = int(lst[i])
    except:
        print(-1)
        return
    i = 0
    while i < (tries-1):
        print(lst[i%len(lst)], end = '-')
        i+=1
    print(lst[(i)%len(lst)])

lst = list(input().split())
tries = int(input())
infinte(lst, tries)