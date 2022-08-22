// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/longest-palindromic-substring/


const expandFromMiddle = (s, left, right) => {
    if (s == null || left > right ){ return 0; }
    
    while (left >= 0 && right < s.length && s.charAt(left) == s.charAt(right) ){
        left--;
        right++;
    }
    return (right - 1) - (left + 1) + 1;
}

const longestPalindrome = (s) => {
    if (s == null || s.length < 1){ return ""; }

    let start = 0;
    let end = 0;

    for (let i = 0; i<s.length; i++){
        
        
        const len1 = expandFromMiddle(s, i, i);
        
        const len2 = expandFromMiddle(s, i, i+1);
        
        const len = Math.max(len1, len2);
        
        if (len > end - start) {
            start = i - Math.floor((len - 1) / 2);
            end = i + Math.floor(len/2);
        }
    }
    return s.substring(start, end+1);

}

const str = "cbbd"
const res = longestPalindrome(str);
console.log(res);
