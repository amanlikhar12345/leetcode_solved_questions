class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        max_l=0

        h={0: -1}

        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                c-=1

            if c in h:
                l=i-h[c]
                max_l=max(max_l, l)
            else:
                h[c]=i

        return max_l