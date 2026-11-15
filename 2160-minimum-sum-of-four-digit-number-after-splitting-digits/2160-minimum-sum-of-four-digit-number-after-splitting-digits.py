class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """

        n=sorted(str(num))
        n1=n[0]+n[2]
        n2=n[1]+n[3]
        return int(n1)+int(n2)