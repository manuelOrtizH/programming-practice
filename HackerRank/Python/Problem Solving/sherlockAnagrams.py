#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def sherlockAndAnagrams(s): 
    pairs, cache, anagrams =  0, set(), {}


    for i in range(1,len(s)):
        for j in range(len(s)):
            w = ''.join(sorted(s[j:i+j]))
            if len(w) == i:
                if w not in cache:
                    cache.add(w)
                else:
                    if w not in anagrams:
                        anagrams[w] = 2
                    else:
                        anagrams[w] += 1
    return sum(map(lambda c: ((c-1) * c)//2, anagrams.values()))

if __name__ == '__main__':
#     s = 'abba'
#     s = 'mom'
#     s = 'abba'
#     s = 'ifailuhkqq'
    s = 'kkkk'
#     s = 'cdcd'
    result = sherlockAndAnagrams(s)
    print(result)