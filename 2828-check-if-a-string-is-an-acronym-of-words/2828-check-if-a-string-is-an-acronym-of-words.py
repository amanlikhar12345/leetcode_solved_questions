class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(words)!=len(s):
            return False
        else:
            j=0
            for i in words:
                if s[j]!=i[0]:
                    return False
                j+=1
            else:
                return True

            return True