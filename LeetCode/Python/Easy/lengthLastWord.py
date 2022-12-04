# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        WHITE_SPACE = " "
        # Look for no blank spaces
        while (s[i] == WHITE_SPACE):
            i-=1
            
        while (i>=0 and s[i]!= WHITE_SPACE):
            length+=1
            i-=1
        
        return length
        # if (len(s) == 0):
        #     return 0
        # s = s.strip() # remove the extra spaces at the end, which are unnecessary
        # l = s.split(" ") # then split it so that we get a list of all the words in the string
        # return len(l[-1])   

