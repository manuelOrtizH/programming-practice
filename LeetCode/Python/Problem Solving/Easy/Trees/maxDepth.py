#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/maximum-depth-of-binary-tree/
from node import Node
def maximum_depth(root):
    if not root:
        return 0

    l = 1 + maximum_depth(root.left)
    r = 1 + maximum_depth(root.right)

    return l if l>r else r

rootA = Node(3, Node(9), Node(20, Node(15), Node(7)))
rootB = Node(4, Node(2, Node(4), Node(5)), Node(3))
maximum_depth(rootB)