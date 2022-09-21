// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/decode-ways/

const map = new Map([
    ['1', 'A'],['2', 'B'],['3', 'C'],['4', 'D'],['5', 'E'],['6', 'F'],
    ['7', 'G'],['8', 'H'],['9', 'I'],['10', 'J'],['11', 'K'],['12', 'L'],
    ['13', 'M'],['14', 'N'],['15', 'O'],['16', 'P'],['17', 'Q'],['18', 'R'],
    ['19', 'S'],['20', 'T'],['21', 'U'],['22', 'V'],['23', 'W'],['24', 'X'],
    ['25', 'Y'],['26', 'Z']
]);

const numDecodings = s => {

    const dp = [1];
    
    
    if (s[0] == '0') {
        return 0;
    } else {
        dp[1] = 1;
    }

                 
    for (let i = 2; i <= s.length; i++){
        if (s[i-1] != '0') {
            dp[i] = dp[i-1];
        }else {
            dp[i] = 0;
        }
        
        const value = s[i-2] + s[i-1];
        
        if (map.has(value)){
            dp[i] += dp[i-2];
        }
        
    }
    
    
    
    return dp[s.length];
    
};