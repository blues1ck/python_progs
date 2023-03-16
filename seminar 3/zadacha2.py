class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
        newNode =  Node(data)

        if (self.head == None):
            self.head, self.tail = newNode, newNode
            self.head.previous = None
            self.tail.previous = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None

    def printlist(self):
        current = self.head
        if self.head == None:
            print('List is empty')
            return
        else:
            while current != None:
                print(current.data, end = ', ')
                current = current.next
        print()

    def printlist_reverse(self):
        current = self.tail
        if self.tail == None:
            print("List is empty")
            return
        else:
            while current != None:
                print(current.data, end = ', ')
                current = current.previous
        print()


import random


dl_list = Double_Linked_List()
for _ in range(10):
    dl_list.add_node(random.randint(-100, 100))
dl_list.printlist()
dl_list.printlist_reverse() 