string = input().split()
if len(string) == 0:
    print(0)
elif len(string) == 1:
    print(1)
else:
    dictionary = dict()
    all = []
    for comb in string[1:]:
        num = comb.split("-")
        if len(dictionary) == 0:
            dictionary[string[0]] = num
        else:
            stop = False
            for key in dictionary.keys():
                if len(dictionary[key]) != 1:
                    for j in dictionary[key]:
                        if j not in all:
                            dictionary[j] = num
                            all.append(j)
                            stop = True
                            break
                if stop:
                    break
    keys = dictionary.keys()
    roads = []

    def rd(road, a):
        if a not in keys:
            roads.append(road + 1)
        else:
            for i in dictionary[a]:
                rd(road + 1, i)

    rd(0, str(string[0]))
    print(max(roads))