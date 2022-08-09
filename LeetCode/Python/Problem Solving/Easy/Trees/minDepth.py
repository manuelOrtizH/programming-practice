#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/minimum-depth-of-binary-tree/
from node import Node
def minimum_depth(root):
    if not root:
        return 0

    l = 1 + minimum_depth(root.left)
    r = 1 + minimum_depth(root.right)

    return min(l,r) if min(l,r)>1 else max(l,r)

rootA = Node(3, Node(9), Node(20, Node(15), Node(7)))
rootB = Node(4, Node(2, Node(4), Node(5)), Node(3))
minimum_depth(rootB)