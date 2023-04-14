a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def _round(x):
    if x<0:
        if abs(x-int(x))<0.5:
            x = int(x)
        else:
            x = int(x-1)
    else:
        if abs(x-int(x)) < 0.5:
            x = int(x)
        else:
            x = int(x+1)
    return x

if b2 != 0 and a1 - b1*a2/b2 != 0:
    x = ((-c1+c2*b1/b2)/(a1 - b1*a2/b2))
    y = ((-c2 - a2*x)/b2)
    print(_round(x), _round(y))
else:
    print('NO')