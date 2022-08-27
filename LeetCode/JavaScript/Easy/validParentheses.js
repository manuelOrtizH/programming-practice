// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/valid-parentheses/

const isValid = s => {
    if (s.length == 1 ){ return false; }
    const stack = []; // "stack" 
    const mapSymbols = new Map();
    mapSymbols.set('}', '{');
    mapSymbols.set(')', '(');
    mapSymbols.set(']', '[');
    let i = 0;
    while (i < s.length){
        const size = stack.length;
        const symbol = s[i];
        if (symbol == '{' || symbol == '(' || symbol == '['){
            stack.push(symbol);
        }else{
            const top = stack[size-1];
            if (top == mapSymbols.get(symbol)){
                // POP AND GO ON
                stack.pop();
            }else{
                return false;
            }
        }
        
        i++;
    }
    
    
    return (stack.length == 0 ) ? true : false;
    
};