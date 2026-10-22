/**
 * @param {string} s
 * @return {boolean}
 */
var checkString = function(s) {
    r=Array.from(s).sort().join("")
    return r==s
};