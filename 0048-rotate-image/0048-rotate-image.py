class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        import copy 
        m = copy.deepcopy(matrix[:])
        for i in range(len(m)):
            for j in range(len(m[i])):
                matrix[i][j]=m[len(m[j])-1-j][i]
        return matrix