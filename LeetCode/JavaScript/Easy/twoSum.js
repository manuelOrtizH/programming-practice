// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/two-sum/

const twoSum = (nums, target) => {
    const numsMap = new Map();
  
    for (let i=0; i<nums.length; i++){
        const diff = target - nums[i];
        if (numsMap.has(diff)){
            return [i,numsMap.get(diff)];
        }else {
            numsMap.set(nums[i], i);
        }
    }
    return [];
    
};