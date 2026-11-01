class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import itertools
        return ["".join(i) for i in itertools.permutations("123456789"[:n])][k-1]