class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        pro=1
        s=0
        for i in str(n):
            pro*=int(i)
            s+=int(i)
        return pro-s