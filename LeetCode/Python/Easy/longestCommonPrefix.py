# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def comparingStrings(self, s1: str, s2: str):
        prefix = ''
        for c1,c2 in zip(s1,s2):
            if c1 != c2:
                break
            prefix += c1
        return prefix

    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs) == 1:
            return prefix
        
        for i in range(1,len(strs)):
            if not prefix:
                break
            prefix = self.comparingStrings(prefix, strs[i])    
        return prefix