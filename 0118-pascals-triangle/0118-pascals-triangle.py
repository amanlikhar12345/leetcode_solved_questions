class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result=[]

        

        for i in range(numRows):
            m=[]
            if i==0:
                m.append(1)
            elif i==1:
                m.append(1)
                m.append(1)
            else:
                m.append(1)
                for j in range(1,i):
                    m.append(result[i-1][j-1]+result[i-1][j])
                m.append(1)
            result.append(m)
        return result
