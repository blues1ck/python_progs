
def LinkedList():
    return {'first': None}

# создание узла
def Node(value):
    return {'value': value, 'next': None}

def addtolist(value, l_list):
    new_node = Node(value)
    new_node['next'] = l_list['first']
    l_list['first'] = new_node

def search(l_list, item):
    current_node = l_list['first']
    while current_node['next'] is not None:
        if current_node['value'] == item:
            return True
        current_node = current_node['next']
    return False

l = list(map(int, input().split()))
l_list = LinkedList()
for i in l:
    addtolist(i, l_list)
print(search(l_list, int(input())))
