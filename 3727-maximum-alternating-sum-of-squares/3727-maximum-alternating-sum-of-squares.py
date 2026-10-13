class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i]*=nums[i]
        nums.sort()
        even=nums[0:len(nums)//2]
        odd=nums[len(nums)//2:]

        return sum(odd)-sum(even)