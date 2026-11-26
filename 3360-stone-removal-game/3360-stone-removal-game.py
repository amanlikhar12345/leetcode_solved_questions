class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=10
        t=0
        while n >= i:
            n-=i
            i-=1
            t+=1

        return t%2==1