#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/summary-ranges/

def check_range(initial_range,final_range, res):
    if final_range > initial_range:
        res.append(str(initial_range) + '->' + str(final_range))
    else:
        res.append(str(initial_range))

def summaryRanges(nums):
    initial_range = 0
    final_range = 0
    if nums:
        final_range = initial_range = nums[0]
    else: return nums
    res = [] 
    
    for i in range(1, len(nums)):
        if (nums[i] - nums[i-1]) == 1:
            final_range = nums[i]
        else:
            check_range(initial_range, final_range, res)
            initial_range = final_range = nums[i]
    #Last elements of range
    check_range(initial_range, final_range, res)
    
    return res

numsA = [0,1,2,4,5,7]
numsB = [0,2,3,4,6,8,9]
summaryRanges(numsA)