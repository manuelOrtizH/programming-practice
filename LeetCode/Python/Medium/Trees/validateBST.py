#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/validate-binary-search-tree/
from cmath import inf
from node import Node
def isValidBST(root):
    stack = []
    left_most = float(-inf)
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
    
        root = stack.pop()    
        if root.data <= left_most:
            return False

        left_most, root = root.data, root.right
        
    return True


rootA = Node(2, Node(1), Node(3))
rootB = Node(5, Node(1), Node(4, Node(3), Node(6)))
rootC = Node(1, left= Node(1))
rootD = Node(5, Node(4), Node(6, Node(3), Node(7)))
rootE = Node(8, 
            left=Node(2, 
                left=Node(1), 
                right=Node(9)), 
            right=Node(12, 
                left=Node(11), 
                right=Node(13)))

print(isValidBST(rootA))
