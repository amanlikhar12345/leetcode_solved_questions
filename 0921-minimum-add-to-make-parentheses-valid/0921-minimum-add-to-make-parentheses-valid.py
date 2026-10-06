class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0
        for i in range(len(s)):
            if s[i]=='(' :
                l+=1
            elif s[i]==')' and l > 0:
                l-=1
            elif s[i]==')' and l == 0:
                r+=1
        print(l)
        return l+r



