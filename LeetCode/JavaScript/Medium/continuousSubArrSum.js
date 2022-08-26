// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/continuous-subarray-sum/

const checkSubarraySum = (nums, k) => {
    const mapSums = new Map();
    mapSums.set(0,-1);
    let sum = 0;
    for (let i = 0; i < nums.length; i++){
        sum += nums[i];
        const modSum = sum%k;
        if (!mapSums.has(modSum)){
            mapSums.set(modSum, i);
        } else {
            if ((i - mapSums.get(modSum)) > 1){
                return true;
            }
        }
    };
    return false;
};

const nums = [23, 2, 4, 6, 7];
const k = 6;
checkSubarraySum(nums,k);