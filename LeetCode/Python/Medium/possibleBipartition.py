# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/possible-bipartition/description/

from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        if not dislikes: return True

        graph = defaultdict(list)

        YELLOW, PURPLE = 1, -1

        color_dict = defaultdict(lambda: None)

        for (a,b) in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(person, color):
            if not color_dict[person]:
                color_dict[person] = color
            else:
                return color_dict[person] == color
            
            for disliked_person in graph[person]:
                if not dfs(disliked_person, PURPLE if color==YELLOW else YELLOW):
                    return False
                    
            return True

        for person in range(1, n+1):
            if not color_dict[person] and not dfs(person, YELLOW):
                return False

        return True
        


