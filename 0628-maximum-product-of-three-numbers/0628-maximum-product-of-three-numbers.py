class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=sorted(nums)
        return max([n[-1]*n[-2]*n[-3],n[0]*n[1]*n[-1]])