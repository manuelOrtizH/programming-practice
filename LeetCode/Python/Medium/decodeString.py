#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/decode-string/

def decodeString(s):
    def dfs(s,times,index):
        if not s:
            return s

        newString = ""
        t = ''
        i = index
        while i<len(s):
            if s[i].isnumeric():
                t+=s[i]
            elif s[i] == ']':
                newString += times * newString
                return newString, i
            elif s[i] == '[':
                times = int(t)
                to_concat, index = dfs(s, times, i+1)
                newString+=to_concat
                i = index
                t = ''
            else:
                newString+=s[i]
            i+=1
        return newString,i
    return dfs(s,1,0)[0]

s1 = "3[a2[c]]"
s2 = "2[abc]3[cd]ef"
decodeString(s2)