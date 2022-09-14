//Manuel Ortiz at 2022
//Extracted from: https://leetcode.com/problems/plus-one/

const plusOne = digits => {
    let i = digits.length - 1;
    while (i >= 0){
        if (digits[i] < 9){
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
        i--;
    }
    
    return [1].concat(digits);
    
    
};