
var targetIndices = function(nums, target) {
    let n=nums.toSorted((a, b) => a - b);
    let res=[];

    for (let i=0; i<n.length; i++) {
        if (n[i]==target) {
            res.push(i);
        }
    }

    return res;
};
