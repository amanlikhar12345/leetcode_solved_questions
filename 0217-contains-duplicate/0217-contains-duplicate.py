# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         for i in nums:
#             if nums.count(i)>1:
#                 return True
#                 break
#         else:
#             return False
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False