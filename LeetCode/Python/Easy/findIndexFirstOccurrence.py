# Manuel Ortiz at 2024
# Extracted from: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        i = 0
        while i < len(haystack):
            j = 0
            while (i+j)<len(haystack) and (j < len(needle) and haystack[i+j] == needle[j]):
                j+=1
            if j == len(needle): return i #where the first_occ was
            
            i+=1
        return -1