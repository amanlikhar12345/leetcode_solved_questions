/**
 * @param {string} s
 * @return {number}
 */
var firstMatchingIndex = function(s) {
    n=Math.floor(s.length/2)
    for (let i=0;i<=n;i++){
        if (s[i]==s[s.length-i-1]){
            return i
        }
    }
    return -1
};