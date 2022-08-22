#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import math
from node import Node
def sortedArrayToBST(nums):
    nodes, center_node = len(nums), 0
    if not nums: 
        return
    center_node = nodes//2
    root = Node(nums[center_node])
    root.left = sortedArrayToBST(nums[0:center_node])
    root.right = sortedArrayToBST(nums[center_node+1:])
    return root


nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)