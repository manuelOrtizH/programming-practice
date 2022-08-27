// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

const minAddToMakeValid = s => {
    const stack = [];
    let i = 0;
    let counter = 0;
    
    while (i < s.length) {
        const symbol = s[i];
        const stackSize = stack.length;  
        
        if (stackSize == 0 || symbol == '(') {
            stack.push(symbol);
            counter++;
        }else {
            const peek = stack[stackSize-1];
            if (peek == '('){
                stack.pop();
                counter--;
            }else{
                stack.push(symbol);
                counter++;
            }
            
        }
        i++;
    }
    
    return counter;
    
};