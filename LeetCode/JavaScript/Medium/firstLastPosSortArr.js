//Manuel Ortiz at 2022
//Extracted from: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

const leftBinarySearch = (nums, left, right, target) => {
    
    let i = -1;
    
    while (left <= right) {
        const middle = Math.floor((left + right)/2);
        if (nums[middle] == target ){
            i = middle;
        }
        
        if (target <= nums[middle]){
            right = middle-1;
        } else {
            left = middle+1;
        }

    }
   
    return i;

};

const rightBinarySearch = (nums, left, right, target) => {
    let i = -1;
    
    while (left <= right) {
        const middle = Math.floor((left + right)/2);
        if (nums[middle] == target ){
            i = middle;
        }
        
        if (target >= nums[middle]){
            left = middle+1;
        } else {
            right = middle-1;
        }

    }
   
    
    return i;

};


const searchRange = (nums, target) => {
    const result = [leftBinarySearch(nums,0,nums.length, target), rightBinarySearch(nums,0,nums.length, target)];
    
    return result;
    

};