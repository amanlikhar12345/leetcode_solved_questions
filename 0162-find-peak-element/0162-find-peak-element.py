class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums.index(max(nums))

    #     class Solution(object):
    # def findPeakElement(self, nums):
    #     left,right = 0, len(nums)-1
    #     last = 0
    #     while left<=right:
    #         mid = (left + right)//2
    #         if nums[mid] >= nums[right]:
    #             last = mid
    #             right -=1
    #         else: left += 1
        
    #     return last