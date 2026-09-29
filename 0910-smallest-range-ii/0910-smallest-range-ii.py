class Solution(object):
    def smallestRangeII(self, nums, k):
        s=sorted(nums)
        ans=s[-1]-s[0]

        for i in range(len(s)-1):
            minimum=min(s[0]+k,s[i+1]-k)
            maximum=max(s[i]+k,s[-1]-k)

            ans=min(ans,maximum-minimum)

        return ans