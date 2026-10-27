class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq=0
        for i in range(0,len(nums)): 
            for j in range(i+1,len(nums)+1):
                a=nums[i:j]
                b=len(set(a))
                sq+=(b**2)

        return sq