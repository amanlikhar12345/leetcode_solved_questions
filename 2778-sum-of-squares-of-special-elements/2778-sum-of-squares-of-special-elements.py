class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                res.append(nums[i])
        r=0
        for i in res:
            r+=i*i
        return r