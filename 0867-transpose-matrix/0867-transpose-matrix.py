class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m=[]
        for i in range (len(matrix[0])):
            row =[]
            for j in range (len(matrix)):
                row.append(0)
            m.append(row)
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                m[j][i]=matrix[i][j]
        return m