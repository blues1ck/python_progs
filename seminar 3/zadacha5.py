class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
        newNode =  Node(data)

        if (self.head == None):
            self.head, self.tail = newNode, newNode
            self.head.previous = None
            self.tail.next = None
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
    def remove_from_list(self, data):
            to_del = Node(data)
            if self.head is None:
                return
            elif self.head.data == to_del.data:
                self.head = self.head.next
            else:
                current = self.head
                following = Node(0)
                precurrent = Node(0)
                while current.data != to_del.data:
                    if current.next is not None:
                        current = current.next
                    else:
                        return
                following = current.next
                precurrent = current.previous
                following.previous, precurrent.next = current.previous, current.next
                return
    
    def ai_ani(self):
        if self.head.next is None:
            print('List dont have enought items')
            return
        elif (self.tail.previous == self.head) or (self.tail.previous == self.head.next):
            print(self.head.data - self.tail.data)
            return
        else:
            current1 = self.head
            current2 = self.tail
            while (current1 != current2) and (current1.previous != current2):
                print(current1.data - current2.data, end = ', ')
                current1, current2 = current1.next, current2.previous

import random
dl_list = Double_Linked_List()
for _ in range(6):
    dl_list.add_node(random.randint(-2, 5))
dl_list.printlist()
dl_list.remove_from_list(0)
dl_list.printlist()
dl_list.ai_ani()