/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    res=["999","888","777","666","555","444","333","222","111","000"]
    for (let i of res){
        if (num.includes(i)){
            return i
        }
    }
    return ""
};