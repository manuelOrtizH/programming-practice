#Manuel Ortiz at 2023
#Extracted from: https://leetcode.com/problems/symmetric-tree/

from node import Tree,Node

class Solution:
    def helperIsSymmetric(self, nodeA, nodeB):
        if not nodeA or not nodeB:
            return nodeA == nodeB
        
        if nodeA.val == nodeB.val:
            return self.helperIsSymmetric(nodeA.left, nodeB.right) and self.helperIsSymmetric(nodeA.right, nodeB.left)
        
        return False

    def isSymmetric(self, root: Node) -> bool:
        return self.helperIsSymmetric(root.left, root.right)
        
rootA =  Node(1 
            ,left = Node(2
                        ,left=  Node(3)
                        ,right= Node(4)
                    )       
            ,right = Node(2
                        ,left=  Node(4)
                        ,right= Node(3)   
                    )
        )

rootB = Node(1
            ,left = Node(2 
                        ,left=None
                        ,right=Node(3))
            ,right = Node(2
                        ,left=None
                        ,right=Node(3))
)

rootC = Node(1, left=Node(2))


tree = Tree(rootB)
sol = Solution()
res = sol.isSymmetric(tree.root)
print(res)

