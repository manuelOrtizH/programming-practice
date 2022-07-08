#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 1
        j = 0
        if not s:
            return 0
        for i in range(1,len(s)+1):
            w = s[j:i]
            if len({*w}) == len(w): l = max(l,i-j)
            else: j+=1
        return l
               
sol = Solution()
sol.lengthOfLongestSubstring("pwwkew")