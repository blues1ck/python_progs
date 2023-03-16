class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        # getting tree root
        return self.root

    def add(self, val):
        # adding value to tree
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            # adding into left
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            # into right
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        # finding value in the tree
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
        print()

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v), end = ' ')
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
from random import randint
for _ in range(10):
    tree.add(randint(1, 5))

tree.printTree()
tree.find(5)