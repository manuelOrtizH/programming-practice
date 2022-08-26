// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/maximum-subarray/

const maxSubArray = nums => {
    let firstElement = nums[0];
    let minSum = firstElement;    
    let currSum = firstElement;
    let result = firstElement;
    
    for (let i = 1; i < nums.length; i++) {
        currSum += nums[i];
        result = Math.max(result, Math.max((currSum - minSum), currSum));
        minSum = Math.min(minSum, currSum);
    }
    
    return result;
 
};

const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
maxSubArray(nums);