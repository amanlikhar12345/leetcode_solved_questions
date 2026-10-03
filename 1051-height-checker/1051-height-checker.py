class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s=sorted(heights)
        res=0
        for i in range(len(s)):
            if heights[i]!=s[i]:
                res+=1
        return res



