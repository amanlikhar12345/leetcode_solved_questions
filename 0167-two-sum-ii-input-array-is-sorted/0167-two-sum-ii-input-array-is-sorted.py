class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        res=[]
        while True:
            if numbers[i]+numbers[j]==target:
                a,b=i+1,j+1
                print(a,b)
                res.append(a)
                res.append(b)
            
                return res

            elif numbers[i]+numbers[j]>=target:
                j-=1
            else:
                i+=1