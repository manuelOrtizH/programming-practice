// Manuel Ortiz at 2022
// Extratcted from: https://leetcode.com/problems/subarray-sum-equals-k/

const subarraySum = (nums,k) => {
    const mapSums = new Map();
    let sum = 0;
    mapSums.set(sum, 1);
    let counter = 0;
    for (const n of nums){
        sum+=n;
        if (mapSums.has(sum - k)){
            counter+=mapSums.get(sum - k);
        }
        mapSums.set(sum, mapSums.has(sum) ? mapSums.get(sum)+1 : 1);
    }
    return counter;
};

const numsA = [3,4,7,2,-3,1,4,2];
const res = subarraySum(numsA, 7);
console.log(res);