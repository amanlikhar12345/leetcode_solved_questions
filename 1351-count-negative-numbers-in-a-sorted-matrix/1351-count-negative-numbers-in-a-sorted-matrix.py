class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c=0
        for row in range (len(grid)):
            for col in range (len(grid[row])):
                if grid [row][col]<0:
                    c+=1
        return c