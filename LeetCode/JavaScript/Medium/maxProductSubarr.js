// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/maximum-product-subarray/

const maxProduct = nums => {
    // [3,-1,4]
    // [3,-3,-12]
    let maxProduct = nums[0];
    let currProduct = 1;
    let i = 0;
    let j = nums.length - 1;
    while (i < nums.length) {
        if (currProduct == 0){
            currProduct = 1;
        }
        currProduct *= nums[i];
        maxProduct = Math.max(currProduct, maxProduct);
        i++;
    }
    currProduct = 1;
    while (j >= 0){
        if (currProduct == 0){
            currProduct = 1;
        }
        currProduct *= nums[j];
        maxProduct = Math.max(currProduct, maxProduct);
        j--;
    }
    
    return maxProduct;
    
};