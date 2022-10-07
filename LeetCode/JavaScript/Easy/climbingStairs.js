// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/climbing-stairs/

const climbStairs = (n) => {
    if (n <= 2) return n;
    const memo = [];
    memo[0] = 1 
    memo[1] = 2 
    
    for (let i = 2; i < n; i++) memo[i] = memo[i-1] + memo[i-2];

    return memo[n-1];
        
};