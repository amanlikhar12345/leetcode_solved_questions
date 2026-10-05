class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        # r=first+" "+second
        # text=text.replace(r,)
        res=[]
        s=text.split()
        for i in range(len(s)-2):
            if s[i]==first:
                if s[i+1]==second:
                    res.append(s[i+2])
        return res