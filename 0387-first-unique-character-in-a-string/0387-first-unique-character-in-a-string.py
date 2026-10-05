class Solution(object):
    def firstUniqChar(self, s):
        d = {}

        for i in s:
            d[i] = d.get(i, 0) + 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1
        # for i in range(len(s)):
        #     if s.count(s[i])==1:
        #         return i
        # else:
        #     return -1
