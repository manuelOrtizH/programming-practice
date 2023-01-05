# Manuel Ortiz at 2023
# Extracted from: https://leetcode.com/problems/all-paths-from-source-to-target/description/ */

from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        graph_dict = defaultdict(list)
        for i,children in enumerate(graph):
            graph_dict[i] = children
        NODE_SOURCE = 0
        NODE_DESTINATION = len(graph_dict) - 1
        paths = []
        
        stack = [(NODE_SOURCE, [NODE_SOURCE])]
        while stack:
            node, path = stack.pop()
            if node == NODE_DESTINATION:
                paths.append(path)
            for children in graph_dict[node]:
                stack.append((children, path+[children]))

        return paths