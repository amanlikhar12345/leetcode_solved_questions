class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=set(s)
        if len(s)<2:
                return ""
        for i in range(len(s)):
            if s[i].lower() in st and s[i].upper() in st :
                pass
            else:
                x=self.longestNiceSubstring(s[i+1:])
                y=self.longestNiceSubstring(s[:i])
                if len(x) > len(y):
                    return x
                else:
                    return y
        return s