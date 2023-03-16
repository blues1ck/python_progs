class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isIdentical(x, y):
     
    #, если оба дерева пусты, вернуть true
    if x is None and y is None:
        return True
 
    #, если оба дерева непусты и значение их корневого узла совпадает,
    # повторяются для их левого и правого поддерева
    return (x is not None and y is not None) and (x.key == y.key) and \
        isIdentical(x.right, y.left) and isIdentical(x.left, y.right)

if __name__ == '__main__':
 
    # построить первое дерево
    x = Node(15)
    x.left = Node(10)
    x.right = Node(10)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(12)
    x.right.right = Node(8)


    
    if isIdentical(x.left, x.right):
        print('The given binary tree is simetrical')
    else:
        print('The given binary tree is not simetrical')