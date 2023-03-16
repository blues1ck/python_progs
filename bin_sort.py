from random import randint
def BinTree():
    return{'root': None}

def Node(value):
    return{'left': None,
           'right': None,
           'value': value}

def insert_into_tree(t, value):
    if t['root'] is None:
        t['root'] = Node(value)
    else:
        insert_into_node(t['root'], value)

def insert_into_node(node, value):
    if value == node['value']:
        return
    if value > node['value']:
        if node['right'] is None:
            node['right'] = Node(value)
        else:
            insert_into_node(node['right'], value)
    else:
        if node['left'] is None:
            node['left'] = Node(value)
        else:
            insert_into_node(node['left'], value)

def print_tree(t):
    print_node(t['root'])
    print()

def print_node(node):
    if node is None:
        return
    print_node(node['left'])
    print(node['value'], end = ' ')
    print_node(node['right'])


t = BinTree()
for _ in range(15):
    x = randint(100, 999)
    print(x, end= ' ')
    insert_into_tree(t, x)

print()
print(t)
print_tree(t)