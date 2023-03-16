def Is_sum_tree(t):
    if t.data is None:
        return None
    if (t.left is None) and (t.right is None):
        return True
    elif t.right is None:
        if t.left == t.data:
            return True
        else:
            return False
    elif t.left is None:
        if t.right.data == t.data:
            return True
        else:
            return False
    else:
        if t.left.data + t.right.data == t.data:
            if Is_sum_tree(t.left) and Is_sum_tree(t.right):
                return True
            else:
                return False                     
        else:
            return False