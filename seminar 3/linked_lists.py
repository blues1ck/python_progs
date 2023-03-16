from  random import randint

def LinkedList():
    return {'first': None}

# создание узла
def Node(value):
    return {'value': value, 'next': None}

def addtolist(value, l_list):
    new_node = Node(value)
    new_node['next'] = l_list['first']
    l_list['first'] = new_node

def pop_from_list(l_list):
    res = l_list['first']['value']
    l_list['first'] = l_list['first']['next']
    return res

def printlist(l_list):
    current_node = l_list['first']
    while current_node is not None:
        print(current_node['value'], end=' ')
        current_node = current_node['next']
    print()

def insert_value(node, value):
    new_node = Node(value)
    new_node['next'] = node['next']
    node['next'] = new_node
    return node


l = LinkedList()
for _ in range(10):
    addtolist(randint(1, 1000), l)
printlist(l)
print(l)