class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        a=sorted(nums)
        return a[-k]