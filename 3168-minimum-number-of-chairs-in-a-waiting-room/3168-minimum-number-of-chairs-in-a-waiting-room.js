/**
 * @param {string} s
 * @return {number}
 */
var minimumChairs = function(s) {
    stack=[]
    maxCount=0
    for (const i of s){
        if (i=="E"){
            stack.push("E")
        }
        else {
            stack.pop()
        }
        if (stack.length>maxCount){
            maxCount=stack.length
        }
    }
    return maxCount
};