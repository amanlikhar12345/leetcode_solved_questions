class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        a = 0
        for i in range(len(s)):
            a += abs(i- t.index(s[i]))
        return a