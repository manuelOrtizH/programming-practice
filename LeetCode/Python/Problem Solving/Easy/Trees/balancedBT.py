#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/balanced-binary-tree/

from node import Node

def findHeight(root):
    if not root:
        return -1

    l = 1 + findHeight(root.left)
    r = 1 + findHeight(root.right)           

    return max(l,r)

def isBalanced(root):
    if not root:
        return True
    l = findHeight(root.left)
    r = findHeight(root.right)
    
    return abs(l-r)<=1 and isBalanced(root.left) and isBalanced(root.right)

rootA = Node(3, 
        left=Node(9), 
        right=Node(20, 
            left=Node(15), right=Node(7)))

rootB = Node(1,
        left=Node(2,
            left=Node(3, 
                left=Node(4), 
                right=Node(4)),
            right=Node(3)),
        right=Node(2))

isBalanced(rootA)
    