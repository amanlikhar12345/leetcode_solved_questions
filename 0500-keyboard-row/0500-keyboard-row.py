class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first="qwertyuiop"
        second="asdfghjkl"
        third="zxcvbnm"
        res=[]
        for i in words:
            m=i
            i=i.lower()
            f=0
            s=0
            t=0
            for j  in i:
                if j in first:
                    f+=1
                elif j in second:
                    s+=1
                else:
                    t+=1
            if len(i)==f or len(i)==s or len(i)==t:
                res.append(m)
        return res