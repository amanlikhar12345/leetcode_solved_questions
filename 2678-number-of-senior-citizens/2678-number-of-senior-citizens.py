class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        res=0
        for i in details:
            if int(i[11:13])>60:
                res+=1
        return res