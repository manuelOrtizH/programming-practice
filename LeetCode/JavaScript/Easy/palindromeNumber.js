// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/palindrome-number/

const isPalindrome = x => {
    if (x < 0){ return false; }
    const numOfZeros = parseInt(Math.log10(x));
    if (numOfZeros == 0){ return true;}
    const getDigit = div => Math.floor((x/div) % 10);
    let i = 0;
    let left = 10**numOfZeros;
    let right = 1;
    while (i < numOfZeros+1){
        if (getDigit(left) != getDigit(right)){
            return false;
        }
        
        left/=10;
        right*=10;
        i+=1
    }

    return true;

}

const x = 121;
const res = isPalindrome(x);
console.log(res);