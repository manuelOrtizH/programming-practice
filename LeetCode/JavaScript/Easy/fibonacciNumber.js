// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/fibonacci-number/

// Bottom-up approach
const fibMemo = n => {
    if (n==0) return 0; 
    else if (n==1) return 1;

    const memo = [0,1];
    for (let i = 2; i <= n; i++){
        memo[i] = memo[i - 1] + memo[i-2];
    }

    console.log(memo);
    return memo[n];
};

const fibVars = n => {
    if (n == 0) return 0;
    else if (n==1) return 1;

    let a = 0;
    let b = 1;

    for (let i = 2; i<=n; i++){
        [b,a] = [a, a+b];
    }

    return a+b;

};

// Top-Down

function fibRec(i, memo){
    if (i <= 1) return i;
    console.log(memo);
    if (!memo.has(i)){
        memo.set(i,fibRec(i-1, memo) + fibRec(i-2, memo)); 
    }
    return memo.get(i);

    
}

function fibTop(n){
    const memoMap = new Map();
    memoMap.set(0,1);
    memoMap.set(1,1);
    return fibRec(n, memoMap);
}



const res = fibTop(8);
const res2 = fibTop(4);
console.log(res);
console.log('-----------');
console.log(res2);
