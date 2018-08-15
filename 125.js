/**
 * @param {string} s
 * @return {boolean}
 */
var palindromeRecur = function(s) {
    if (s === '' || s.length === 1) {
        return true;
    }
    
    return s[0] === s[s.length - 1] && palindromeRecur(s.substring(1, s.length - 1));
}


var isPalindrome = function(s) {
    let alpha = s.replace(/\W/g, '').toLowerCase();
    return palindromeRecur(alpha);
};

