# Класс для хранения узла бинарного дерева.
class Node:
    def __init__(self, root=None, l=None, r=None):
        self.root = root
        self.l = l
        self.r = r


# Рекурсивная функция для проверки идентичности двух заданных бинарных деревьев.
def is_Identical(x, y):
    # , если оба дерева пусты, вернуть true
    if x is None and y is None:
        return True

    # , если оба дерева непусты и значение их корневого узла совпадает,
    # повторяются для их левого и правого поддерева
    return (x is not None and y is not None) and (x.root == y.root) and \
           is_Identical(x.l, y.l) and is_Identical(x.r, y.r)

def is_sum(x, y):
    if x is None and y is None:
        return True
    return (x is not None and y is not None) and (x.root == y.root) and \
           is_sum(x.l, y.r) and is_sum(x.r, y.l)

def if_self_sum(x):
    return (is_sum_sum(x.r, x.l))

def Node_sum(x):
    if x == None:
        return 0
    else:
        return (x.root + Node_sum(x.l) + Node_sum(x.r))

def _make_sum(x):
    y = Node(Node_sum(x.l)+Node_sum(x.r))
    if x.l != None:
        y.l = _make_sum(x.l)
    if x.r != None:
        y.r = _make_sum(x.r)
    return (y)

def make_sum(x):
    if (x.r == None and x.l == None):
        y = x
    else:
        y = Node(make_sum(x.l).root+make_sum(x.r).root)
        y.l = make_sum(x.l)
        y.r = make_sum(x.r)
    return(y)

def is_sum_sum(x):
    if (x.r == None and x.l == None):
        return True
    return (x.root == x.r.root + x.l.root and is_sum_sum(x.l) and is_sum_sum(x.r))

def print3Node(x):
    y = x
    print(y.root)
    print(y.l.root, y.r.root)
    print(y.l.l.root, y.l.r.root, y.r.l.root, y.r.r.root)

def make_sum_(x):
    if x == None:
        return None
    y = Node(x.root)
    y.l = make_sum_(x.r)
    y.r = make_sum_(x.l)
    return(y)


# построить первое дерево
x = Node(1)
x.l = Node(1)
x.r = Node(1)
x.l.l = Node(3)
x.l.r = Node(1)
x.r.l = Node(4)
x.r.r = Node(2)

# построить второе дерево
y = Node(0)
y.l = Node(1.2)
y.r = Node(1.1)
y.l.l = Node(2.4)
y.l.r = Node(2.3)
y.r.l = Node(2.2)
y.r.r = Node(2.1)

z = make_sum_(x)
print3Node(x)
print3Node(z)
print(is_sum(x, z))