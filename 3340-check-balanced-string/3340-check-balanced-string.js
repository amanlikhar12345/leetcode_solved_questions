/**
 * @param {string} num
 * @return {boolean}
 */
var isBalanced = function(num) {
    pos1=0
    pos2=0
    for (let i=0;i<num.length;i++){
        if (i%2==0){
            pos1+=Number(num[i])
        }
        else{
            pos2+=Number(num[i])
        }
    }
    return pos1==pos2;
};