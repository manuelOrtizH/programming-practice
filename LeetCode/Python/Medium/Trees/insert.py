#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/insert-into-a-binary-search-tree/

from node import Node

def insertIntoBST(root,val):
    if not root:
        return Node(val)

    if val>root.data:
        root.right = insertIntoBST(root.right, val)
    elif val<root.data:
        root.left = insertIntoBST(root.left, val)
    return root

root = Node(4, 
        left=Node(2,
            left=Node(1),
            right=Node(3)),
        right=Node(7))

result = insertIntoBST(root, 5)