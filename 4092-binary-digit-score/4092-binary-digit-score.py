class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s11=bin(a)
        a=s11[2:]
        s12=bin(b)
        b=s12[2:]

        s1=a.count("1")
        s2=b.count("1")

        if s1 >= s2:
            return int(s1)*int(s2)
        else:
            return int(s2)/int(s1)
        