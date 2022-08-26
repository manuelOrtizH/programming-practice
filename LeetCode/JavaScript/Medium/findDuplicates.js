// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/find-all-duplicates-in-an-array/

const findDuplicates = nums => {
    const result = [];
    let i = 0;
    // []
    while (i < nums.length) {
        const index = Math.abs(nums[i]) - 1;
        if (nums[index] < 0) {
            result.push(index + 1);
        }else{
            nums[index] *= -1;
        }
        i++;
    }
    
    return result;
    
};

const nums = [4,3,2,7,8,2,3,1];
findDuplicates(nums);