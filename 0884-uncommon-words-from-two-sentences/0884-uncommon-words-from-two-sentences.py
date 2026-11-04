class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        r=[]
        words=s1.split()+s2.split()
        for w in words:
            if words.count(w)==1:
                r.append(w)
        return r