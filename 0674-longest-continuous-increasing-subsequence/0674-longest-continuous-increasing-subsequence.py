class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = 1
        length = 1
        while(j<n):
            if(nums[j]>nums[j-1]):
                length = max(length,j-i+1)
            else:
                i=j
            j+=1
        return length 