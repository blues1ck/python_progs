class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def Is_palindr(head):
    stck = []
    current = head
    while current:
        stck.append(current.value)
        current = current.next
    
    current = head
    while current:
        if current.value != stck.pop():
            return "No"
        current = current.next
    
    return "Yes"

lst = list(map(str, input().split()))
st = ''
for i in lst:
    st = st + i
head = None
tail = None
for val in st:
    if not head:
        head = Node(val)
        tail = head
    else:
        tail.next = Node(val)
        tail = tail.next

print(Is_palindr(head))
