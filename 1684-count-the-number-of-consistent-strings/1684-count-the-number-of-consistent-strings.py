class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in words:
            s=set(i)
            for j in s:
                if j not in allowed:
                    break
            else:
                c+=1
        return c

        
