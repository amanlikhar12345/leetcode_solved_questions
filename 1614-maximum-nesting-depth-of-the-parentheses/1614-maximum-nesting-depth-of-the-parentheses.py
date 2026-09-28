class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=0
        maxd=0
        for ch in s:
            if ch=="(":
                d+=1
                maxd=max(maxd,d)
            elif ch==")":
                d-=1
        return maxd