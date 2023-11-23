class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.children = []
    
    def visit(self, node):
        self.children.append(node.data)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            self.visit(root)
            self.in_order_traversal(root.right)

    def in_preorder_traversal(self, root):
        if root:
            self.visit(root)
            self.in_preorder_traversal(root.left)
            self.in_preorder_traversal(root.right)
        
    def in_post_order_traversal(self, root):
        if root:
            self.in_post_order_traversal(root.left)
            self.in_post_order_traversal(root.right)
            self.visit(root)

