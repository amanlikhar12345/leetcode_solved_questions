class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        l=[]
        for i in sentences :
            w=i.split()
            l.append(len(w))
        return max(l)