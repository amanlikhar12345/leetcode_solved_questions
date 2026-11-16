class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # m=True
        # ma=True
        # for i in range(1,len(nums)):
        #         if nums[i] < nums[i-1] :
        #             m=False
        #         if nums[i] > nums[i-1] :
        #             ma=False
        # return m or ma 
        n = sorted(nums)
        if n == nums or n[::-1] == nums:
            return True
        else:
            return False 