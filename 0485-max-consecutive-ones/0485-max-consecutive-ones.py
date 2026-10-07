class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        r=''
        for i in nums:
            
            if i==1:
                r+=str(i)
            else:
                res.append(len(r))
                r=''
        res.append(len(r))
        print(res)
        return max(res)
                