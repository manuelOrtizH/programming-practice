#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/delete-node-in-a-bst/

from node import Node

def right_most_node(root): 
    if not root.right:
        return root
    return right_most_node(root.right)
    
def deleteNode(root, key):
    if not root:
        return root
    
    if root.val == key:
        if not root.left and not root.right: return None 
        elif not root.left or not root.right: return root.right or root.left 
        else:
            right_most = right_most_node(root.left)
            right_most.right = root.right
            return root.left    
        
    elif key<root.val:
        root.left = deleteNode(root.left, key)
    else:
        root.right = deleteNode(root.right, key)
    return root


rootA = Node(5, 
        left=Node(3, 
            left=Node(2),
            right=Node(4)),
        right=Node(6, 
            left=None, 
            right=Node(7)))

rootB = Node(0)

rootC = Node(5, 
        left=Node(3,
            left=Node(2),
            right=Node(4)),
        right=Node(6, 
            left=None,
            right=Node(7)))

deleteNode(rootB, 0)