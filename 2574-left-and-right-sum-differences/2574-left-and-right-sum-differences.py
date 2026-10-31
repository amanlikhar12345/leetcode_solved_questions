class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            l=sum(nums[0:i])
            r=sum(nums[i+1:])
            res.append(abs(l-r))
        return res