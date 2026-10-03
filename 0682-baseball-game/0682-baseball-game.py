class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res=[]
        for i in operations:
            if i not in ["C", "D", "+"]:
                res.append(int(i))
            elif i=='C':
                res.pop()
            elif i=="D":
                res.append(int(res[-1]*2))
            elif i=="+":
                res.append(int(res[-1]) + int(res[-2]))
        return sum(res)
