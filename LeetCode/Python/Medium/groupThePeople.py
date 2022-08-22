#Manuel Ortiz at 2022
#Extracted from:  https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {i: [] for i in groupSizes}
        result = []
        
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]])==groupSizes[i]:
                result.append(d[groupSizes[i]])
                d[groupSizes[i]] = []

        return sorted(result)