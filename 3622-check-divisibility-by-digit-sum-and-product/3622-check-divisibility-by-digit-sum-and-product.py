class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        m = 1
        p = n
        while n > 0:
            rem = n%10
            s += rem
            m *= rem
            n = n//10
        if p % (s+m) == 0:
            return True
        else:
            return False