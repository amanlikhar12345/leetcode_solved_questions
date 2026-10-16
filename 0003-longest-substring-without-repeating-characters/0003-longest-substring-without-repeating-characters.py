# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         res=[]

#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
#                 if len(s[i:j])==len(set(s[i:j])):

#                     res.append(s[i:j])
#         c=sorted(res,key=len)
#         return len(c[-1])

        
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         res = 0

#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
#                 if len(s[i:j])==len(set(s[i:j])):
#                     res=max(res,len(s[i:j]))

#         return res

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        res = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right
            res = max(res, right - left + 1)

        return res

