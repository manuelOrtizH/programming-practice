// Manuel Ortiz at 2023
// Extracted from: https://leetcode.com/problems/merge-sorted-array/

const merge = (nums1, m, nums2, n) => {
    if (!nums2){ return nums1 };
    let i = m - 1; //Pivot from nums1
    let j = n - 1; //End from nums2
    let k = m + n - 1; // Pointer starting from the end of the nums1

    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]){
            nums1[k] = nums1[i];
            i--;
        }else{
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }

    while (j >= 0){
        nums1[k] = nums2[j];
        j--;
        k--;
    }
    
};

const nums1 = [0,0,3,0,0,0,0,0,0];
const nums2 = [-1,1,1,1,2,3];
const n = 6;
const m = 3;

// const nums1 = [1,5,6,4,0,0];
// const nums2 = [2,3];
// const n = 2;
// const m = 4;

// const nums1 = [1,2,3,0,0,0];
// const nums2 = [2,5,6];
// const n = 3;
// const m = 3;

// const nums1 = [1,2,4,5,6,0];
// const nums2 = [3];
// const n = 1;
// const m = 5;

merge(nums1,m,nums2,n);
console.log('Result: ', nums1);