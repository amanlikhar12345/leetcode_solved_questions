class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=min(nums)
        b=max(nums)
        res=[]
        for i in range(s,b+1):
            if i not in nums:
                res.append(i)

        return res