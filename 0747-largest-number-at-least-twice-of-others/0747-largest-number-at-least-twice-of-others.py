class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=nums.index(max(nums))
        m=max(nums)
        for i in range (len(nums)):
            if nums[i]*2 > m  and i!=n:
                return -1
        return n