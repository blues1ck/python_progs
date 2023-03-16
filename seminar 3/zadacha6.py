class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizel = 0
    
    def push(self, data):
        newNode =  Node(data)

        if (self.head == None):
            self.head, self.tail = newNode, newNode
            self.head.previous = None
            self.tail.next = None
            self.sizel += 1
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
            self.sizel += 1

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
                self.sizel -= 1
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
                self.sizel -= 1
                return
    
    def pop(self):
        if self.sizel > 0:
            t = self.head.data
            self.remove_from_list(self.head.data)
            return t
        else:
            return 'None, becouse list is empty'
    
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
        print()

    def size(self):
        return self.sizel

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def printstack(self):
        self.printlist()
import random
dl_list = Double_Linked_List()
for _ in range(5):
    dl_list.push(random.randint(-2, 5))
dl_list.printlist()
dl_list.printlist()
print('Длина списка' ,dl_list.size())
print('Вернул первый элемент',dl_list.pop())
dl_list.printlist()
print('Длина списка' ,dl_list.size())
print(dl_list.isEmpty())
dl_list.printstack()