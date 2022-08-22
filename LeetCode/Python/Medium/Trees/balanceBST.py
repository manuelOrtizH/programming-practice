#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/balance-a-binary-search-tree/

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

def add_num(data, nums):
    nums.append(data)

def tree_to_list(root, nums):
    if root:
        tree_to_list(root.left, nums)
        add_num(root.data, nums)
        tree_to_list(root.right, nums)
    return nums


def balanceBST(root):
    nums = tree_to_list(root,[])
    return sortedArrayToBST(nums)
    

root = Node(1, left=None, right=Node(2, left=None, right=Node(3, left=None, right=Node(4))))