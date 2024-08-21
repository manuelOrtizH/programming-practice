# Manuel Ortiz at 2024
# Extracted from: https://leetcode.com/problems/leaf-similar-trees/
from node import Tree, Node

class Solution:
    def leafSimilarHelper(self, root, stack):
        if not root:
            return stack

        if not root.left and not root.right:
            stack.append(root.val)
            return stack

        stack = self.leafSimilarHelper(root.left, stack)
        stack = self.leafSimilarHelper(root.right, stack)
        
        return stack

        

    def leafSimilar(self, root1: Node, root2: Node) -> bool:
        stack1 = self.leafSimilarHelper(root1, [])
        stack2 = self.leafSimilarHelper(root2, [])

        if len(stack1) != len(stack2):
            return False
        
        i = 0
        
        while i < len(stack1):
            if stack1[i] != stack2[i]:
                return False
            i+=1

        return True 
    
# Case 1
rootA = Node(3 
            ,left=Node(5 
                    ,left=Node(6) #end
                    ,right=Node(7) #end
                    )
            ,right= Node(1 
                        ,left=Node(4) #end
                        ,right=Node(2 
                                    ,left=Node(9) #end
                                    ,right=Node(8) #end
                                )
                        )
            )

rootB = Node(3 
            ,left= Node(5 
                        ,left=Node(6) #end
                        ,right=Node(7) #end
                    )
            ,right= Node(1 
                        ,left= Node(4) #end
                        ,right= Node(2 
                                    ,left=Node(9) #end
                                    ,right=Node(8) #end
                                )
                    )
        )

#Case 2
rootC = Node(1 
                ,left=Node(2) #end
                ,right= Node(3) #end
            )

rootD = Node(1 
                ,left=Node(3) #end
                ,right= Node(2) #end
            )  



treeA, treeB = Tree(rootA), Tree(rootB)
# treeA, treeB = Tree(rootC), Tree(rootD)
sol = Solution()
res = sol.isSymmetric(treeA.root, treeB.root)
print(res)

    