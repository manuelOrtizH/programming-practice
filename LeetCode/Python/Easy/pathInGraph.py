# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from collections import deque


class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        
        graph = dict()
        
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]
            
        stack, visited = deque(), set()
        stack.append(start)
        visited.add(start)

        return self.validPathHelper(start, end, graph, stack, visited)
        

    def validPathHelper(self, start, end, graph, stack, visited):
        
        if not stack: return False

        node = stack.pop()

        if node == end: return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                
            
        return self.validPathHelper(start,end,graph,stack,visited)


