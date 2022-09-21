// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/unique-paths/

const uniquePaths = (m,n) => {
    const memo = [];
    for (let i = 0; i < m; i++){
        memo.push([]);
        for (let j = 0; j < n; j++){
            memo[i][j] = 0;
        }
    }

    return uniquePathsHelper(0, 0, memo);
};  

const uniquePathsHelper = (m,n,memo) => {
    const M = memo.length - 1;
    const N = memo[0].length - 1;
    if (m == M && n == N){
        //Reach destination
        return 1;
    } else if (m > M || n > N){
        return 0;
    } else if (memo[m][n] > 0){
        return memo[m][n];
    } else { 
        memo[m][n] = uniquePathsHelper(m+1,n,memo) + uniquePathsHelper(m, n+1, memo);
        return memo[m][n];
    }


}
