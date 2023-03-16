
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        
    def add_to_list(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        current = self.head
        if self.head == None:
            print("List is enmpty")
        else:
            while current.next is not None:
                print(current.data, end = ', ')
                current = current.next
            print(current.data, '\n')

    def insert_to_list(self, data, posision):
        if posision > 1:
            new_node = Node(data)
            current = self.head
            i = 1
            while (i < (posision-1)):
                if current.next is None:
                    print('posision error!')
                    break
                current = current.next
                i += 1
            following = current.next
            current.next = new_node 
            new_node.next = following
        else:
            self.addtolist(data)

    def remove_from_list(self, data):
        to_del = Node(data)
        if self.head is None:
            print('List is empty')
            return
        elif self.head.data == to_del.data:
            self.head = self.head.next
        else:
            current = self.head
            previous = self.head
            while (current.data != to_del.data) and current.next is not None:
                previous = current
                current = current.next
            if current.next is None:
                return
            previous.next = current.next
        
    


import random
l_list = Linked_list()
for _ in range(10):
    t = random.random()
    l_list.add_to_list(t)
l_list.print_list()
l_list.insert_to_list(11, 3)
l_list.remove_from_list(11)
l_list.print_list()
