#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/search-in-a-binary-search-tree/ 

from node import Node, in_order_traversal

def rec_find_node(node, val):
    if not node:
        return None
    if node.data == val:
        return node
    if val < node.data:
        return rec_find_node(node.left, val)
    return rec_find_node(node.right,val)
    

def find_node(node,val):
    while node:
        if val < node.data:
            node = node.left
        elif val > node.data:
            node = node.right
        else:
            return node
        
    return None

root = Node(2, Node(7, Node(12), Node(6)), Node(5, Node(8), Node(9)))
node_rec = rec_find_node(root, 5)
node = find_node(root, 5)
print(in_order_traversal(node_rec, []))
print('----')
print(in_order_traversal(node, []))
