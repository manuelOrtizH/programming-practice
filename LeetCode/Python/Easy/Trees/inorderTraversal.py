# Manuel Ortiz at 2023
# Extracted from: https://leetcode.com/problems/binary-tree-inorder-traversal/
from node import Tree

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        if (not root): return result
        node = root
        stack = []
        while (stack or node):
            while (node):
                stack.append(node)
                node = node.left
            
            currNode = stack.pop()
            result.append(currNode.val)
            node = currNode.right
            
        return result