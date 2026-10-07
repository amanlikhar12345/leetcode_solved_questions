class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=[]
        for i in s:
            if i in "AEIOUaeiou":
                v.append(i)
        v=sorted(v)

        j=0
        res=''
        for i in s:
            if i in "AEIOUaeiou":
                res+=v[j]
                j+=1
            else:
                res+=i
        return res
