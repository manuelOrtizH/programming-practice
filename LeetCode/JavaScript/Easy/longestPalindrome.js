//Manuel Ortiz at 2022
//Extracted from: https://leetcode.com/problems/longest-palindrome/

const longestPalindrome = s => {

    let pairs = 0
    let setPairs = new Set();
    
    for (const char of s){
        if (setPairs.has(char)){
            setPairs.delete(char);
            pairs++;
        }else{
            setPairs.add(char);
        }
    }
    
    let totalLetters = pairs*2;
    if (setPairs.size > 0){
        totalLetters+=1;
    }
    return totalLetters;
}


const s = 'abccccdd';
const res = longestPalindrome(s);