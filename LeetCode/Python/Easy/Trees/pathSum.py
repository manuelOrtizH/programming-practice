# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        new_target_sum = targetSum - root.val
        if not root.right and not root.left:
            return (new_target_sum) == 0
        
        
        left_path = self.hasPathSum(root.left, new_target_sum)
        right_path = self.hasPathSum(root.right, new_target_sum)
    
    
        return left_path or right_path or False