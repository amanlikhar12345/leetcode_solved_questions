class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g=max(nums)
        s=min(nums)
        res=1
        for i in range(1,s+1):
            if g%i==0 and s%i==0:
                res=i
        return res  