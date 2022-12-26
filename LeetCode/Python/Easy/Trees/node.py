class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
    
    

def visit(node, children):
    children.append(node.data)

def in_order_traversal(node, children):
    if node:
        in_order_traversal(node.left, children)
        visit(node, children)
        in_order_traversal(node.right, children)
    return children

def in_preorder_traversal(node):
    if node:
        visit(node)
        in_preorder_traversal(node.left)
        in_preorder_traversal(node.right)


