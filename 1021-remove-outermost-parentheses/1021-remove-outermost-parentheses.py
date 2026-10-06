class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=0
        res=""
        for i in range(len(s)):
            if s[i]=="(":
                l+=1
                if l>1:
                    res+=s[i]
            else:
                l-=1
                if l>0:
                    res+=s[i]
        return res
