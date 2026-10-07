
class Solution(object):
    def findDuplicate(self, nums):

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        # slow = nums[0]
        # fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]

        #     if slow == fast:
        #         break

        # slow = nums[0]

        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow

'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                return i
        

'''


'''class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1

        for i in range(len(nums)):
            c=nums.count(nums[l])
            c1=nums.count(nums[r])
            if c > 1 or c1 >1:
                return i
            l+=1
            r-=1
            '''
           
