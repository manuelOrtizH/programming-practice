# Manuel Ortiz at 2023
# Extracted from: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from node import Node
from collections import defaultdict, deque

def tree_to_graph(root, graph_dict):
    stack = []
    stack.append(root)
    while stack:
        curr_node = stack.pop()
        if curr_node.left: 
            stack.append(curr_node.left)
            graph_dict[curr_node].append(curr_node.left)
            graph_dict[curr_node.left].append(curr_node)
        if curr_node.right: 
            stack.append(curr_node.right)
            graph_dict[curr_node].append(curr_node.right)
            graph_dict[curr_node.right].append(curr_node)

def distanceK(root, target, k):
    if not root: return None

    graph_dict, visited = defaultdict(list), set()
    stack, distance_stack, result = [], [], []
    stack.append(target)
    distance_stack.append(0)

    tree_to_graph(root, graph_dict)
    
    while stack:
        
        curr, curr_distance = stack.pop(), distance_stack.pop()
        if curr_distance == k:
            result.append(curr.data)
        else:
            visited.add(curr)
            for children in graph_dict[curr]:
                if children not in visited:
                    stack.append(children)
                    distance_stack.append(curr_distance +1)
    return result     



root = Node()
root = Node(3, 
                left= Node(5,
                    left=Node(6),
                    right=Node(2, 
                        left= Node(7),
                        right=Node(4))),
                right=Node(1,
                    left=Node(0),
                    right=Node(8)))

print(distanceK(root, target=root.left, k=2))
