// Manuel Ortiz at 2023
// Extracted from: https://leetcode.com/problems/remove-element/

const removeElement = (nums, val) => {
    let i = 0;
    let swap = nums.length - 1;
    let k = 0;
    while (i < nums.length && nums[i] != '_') {
        if(nums[i] == val){
            [nums[i], nums[swap]] = [nums[swap], "_"];
            swap--;
            continue;
        }
        i++;
    };

    return i;

};