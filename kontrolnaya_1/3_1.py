import re
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.children = []

def build_tree(nodes):
    root_val = nodes.pop(0)
    root = TreeNode(int(root_val))

    queue = [root]
    while queue and nodes:
        node = queue.pop(0)
        children = nodes.pop(0)
        child_vals = [int(val) if val.isdigit() else val for val in re.split(r'\s|-', children)]

        for val in child_vals:
            if val is not None:
                child = TreeNode(val)
                node.children.append(child)
                queue.append(child)

    return root

def get_node_level(root, node_val):
    queue = [(root, 1)]
    while queue:
        node, level = queue.pop(0)
        if node.val == node_val:
            return level
        for child in node.children:
            queue.append((child, level+1))
    return 0

root_val = input()
nodes = input().split()
node_val = int(input())

tree = build_tree([root_val] + nodes)
print(get_node_level(tree, node_val))
