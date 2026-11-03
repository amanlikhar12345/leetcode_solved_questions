class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = max(nums)
        count = 0
        for i in nums:
            count += b-i
        return count